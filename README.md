# SSM Library

## Description

The SSM (Surrogate Safety Measures) Library is a comprehensive library focused on providing surrogate safety measures in self-driving safety analyze. It's primarily based on measures such as Time to Collision (TTC), Gap Time (GT), Encroachment Time (ET), Deceleration Rate (DR), Proportion of Stopping Distance (PSD), Post-Encroachment Time (PET), and Initially Attempted Post-Encroachment Time (IAPT). The objective is to provide a tool that allows for a more in-depth analysis of traffic conflicts, focusing not only on frequency but also on severity.

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
