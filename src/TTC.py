from shapely.geometry import Polygon, Point
from shapely.affinity import rotate, translate
import numpy as np

def calculate_rectangle_points(center, length, width, angle):
    """
    This function calculates the points of a rectangle given its center, length, width, and rotation angle.
    
    Args:
        center (tuple): The coordinates of the center of the rectangle.
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        angle (float): The rotation angle of the rectangle in radians.
        
    Returns:
        rectangle (Polygon): A shapely.geometry.Polygon object representing the rectangle.
    """
    dx = length / 2.0
    dy = width / 2.0
    corner_points = [(-dx, -dy), (-dx, dy), (dx, dy), (dx, -dy)]
    rectangle = Polygon(corner_points)
    rectangle = rotate(rectangle, angle, use_radians=True)
    rectangle = translate(rectangle, *center)
    return rectangle

def calculate_T1(center1, center2, length1, width1, length2, width2, velocity1, velocity2, angle1=0, angle2=0):
    """
    This function calculates T1, which is a measure of how close two rectangles are to colliding. 
    
    Args:
        center1 (tuple): The center of the first rectangle.
        center2 (tuple): The center of the second rectangle.
        length1 (float): The length of the first rectangle.
        width1 (float): The width of the first rectangle.
        length2 (float): The length of the second rectangle.
        width2 (float): The width of the second rectangle.
        velocity1 (list): The velocity of the first rectangle.
        velocity2 (list): The velocity of the second rectangle.
        angle1 (float, optional): The rotation angle of the first rectangle in radians. Defaults to 0.
        angle2 (float, optional): The rotation angle of the second rectangle in radians. Defaults to 0.
        
    Returns:
        T1 (float): The T1 measure.
    """
    rectangle1 = calculate_rectangle_points(center1, length1, width1, angle1)
    rectangle2 = calculate_rectangle_points(center2, length2, width2, angle2)

    d_ij = rectangle1.distance(rectangle2)
    direction = np.array(center2, dtype=float) - np.array(center1, dtype=float)
    direction = direction / np.linalg.norm(direction)  # Normalize the direction vector

    dot_d_ij = np.dot(direction, (np.array(velocity1, dtype=float) - np.array(velocity2, dtype=float)))
    if dot_d_ij == 0:
        return float('inf')
    else:
        T1 = d_ij / dot_d_ij
        return T1

def calculate_loom_rates(ego_center, ego_velocity, ego_yaw_rate, ego_length, ego_width, agent_velocity, agent_position):
    """
    This function calculates the loom rates of an ego vehicle with respect to an agent.
    
    Args:
        ego_center (list): The center of the ego vehicle.
        ego_velocity (list): The velocity of the ego vehicle.
        ego_yaw_rate (float): The yaw rate of the ego vehicle.
        ego_length (float): The length of the ego vehicle.
        ego_width (float): The width of the ego vehicle.
        agent_velocity (list): The velocity of the agent.
        agent_position (list): The position of the agent.
        
    Returns:
        loom_rates (list): The list of loom rates.
    """
    loom_rates = []

    # Calculate loom points for the ego vehicle
    loom_points = calculate_loom_points(ego_center, ego_length, ego_width)

    # Calculate linear velocity for each loom point
    for point in loom_points:
        displacement = np.array(point) - np.array(ego_center)
        linear_velocity_point = np.array(ego_velocity) + np.cross(displacement, ego_yaw_rate)

        # Calculate loom rate for each loom point
        relative_position = np.array(agent_position) - np.array(point)
        angular_velocity_1 = np.cross(relative_position, linear_velocity_point)
        angular_velocity_2 = np.cross(relative_position, agent_velocity)
        
        loom_rate = (angular_velocity_1 + angular_velocity_2) / np.linalg.norm(relative_position)**2
        loom_rates.append(loom_rate)

    return loom_rates
