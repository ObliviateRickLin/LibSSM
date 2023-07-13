# SSM Library for AD 

## Description

The SSM (Surrogate Safety Measures) Library is a comprehensive library focused on providing surrogate safety measures in self-driving safety analyze. It's primarily based on measures such as Time to Collision (TTC), Gap Time (GT), Encroachment Time (ET), Deceleration Rate (DR), Proportion of Stopping Distance (PSD), Post-Encroachment Time (PET), and Initially Attempted Post-Encroachment Time (IAPT). The objective is to provide a tool that allows for a more in-depth analysis of traffic conflicts, focusing not only on frequency but also on severity.

| Metric | Description | Status |
| --- | --- | --- |
| Surrogate Conflict Measure |  |  |
| Gap Time (GT) | Time lapse between completion of encroachment by turning vehicle and the arrival time of crossing vehicle if they continue with same speed and path. |  |
| Encroachment Time (ET) | Time duration during which the turning vehicle infringes upon the right-of-way of through vehicle. |  |
| Deceleration Rate (DR) | Rate at which crossing vehicle must decelerate to avoid collision |  |
| Proportion of Stopping Distance (PSD) | Ratio of distance available to maneuver to the distance remaining to the projected location of collision. |  |
| Post-Encroachment Time (PET) | Time lapse between end of encroachment of turning vehicle and the time that the through vehicle actually arrives at the potential point of collision. |  |
| Initially Attempted Post-Encroachment Time (IAPT) | Time lapse between commencement of encroachment by turning vehicle plus the expected time for the through vehicle to reach the point of collision and the completion time of encroachment by turning vehicle. |  |
| Time to Collision (TTC) | Expected time for two vehicles to collide if they remain at their present speed and on the same path. |  |



## Motivation
I have been doing research about the deterministic safety meastures about AD for a long time. SSM proves to be a mature yet traditional way to measure the driving safety conditions. More widespread use means that we can help understand and improve the generalization of these traditional metrics to make them suitable for more complex scenarios. At the same time, I noticed that these traditional metrics are being used in conjunction with some neural network architectures. Therefore, I believe that this work can also reduce some of the repetitive code development tasks and allow more authors to focus on the furture development and application itself.

## Installation

For now, you can install this library by cloning the repository:

```bash
git clone https://github.com/your_username/ssm-library.git
cd ssm-library
```

In the future, we plan to package this library and make it available on PyPI.

## Usage
After installation, you can import and use the library in your Python projects as follows:

```python
from ssm_library import your_module

# use the module here
```

## Contributing

Contributions are welcomed! Please read the contributing guidelines to get started.

## Notice
This document is still under development. Contact 120090527@link.cuhk.edu.cn if you have any advice.

## License

The SSM library is licensed under the terms of [INSERT LICENSE HERE].
