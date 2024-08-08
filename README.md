# AcademicData

<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://pandas.pydata.org/static/img/pandas_white.svg">
  <img alt="Pandas Logo" src="https://pandas.pydata.org/static/img/pandas.svg">
</picture>

This repository contains code and resources for analyzing academic performance using Pandas. The project focuses on generating graphs and metrics related to academic records and marks. It includes functionality for visualizing trends, calculating statistical measures, and creating detailed reports to assess academic progress.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The goal of this project is to develop a system that utilizes Pandas to automatically analyze academic data, generating insightful graphs and metrics. This system aims to visualize academic performance trends, calculate key statistics, and provide detailed reports on students' marks. By offering a clear overview of academic progress, the tool can be valuable for educators, students, and educational administrators, supporting data-driven decisions and enhancing academic evaluation processes.

## Features

- **Data Collection and Cleaning**: Gathering academic records and preprocessing the data to ensure accuracy and consistency.
- **Data Visualization**: Creating charts and graphs to visualize academic performance and trends.
- **Statistical Analysis**: Implementing scripts to calculate key metrics such as averages, distributions, and correlations.
- **Reporting**: Generating detailed reports to summarize academic performance and insights.
  
## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   
    ```sh
    git clone https://github.com/yourusername/repository_name.git
    ```
3. Navigate to the project directory:
   
    ```sh
    cd repository_name
    ```
6. (Optional) Create a virtual environment:

   ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On macOS/Linux use 'python -m venv venv
                                                   source venv/bin/activate'
    ```

5. Select venv as your python interpreter (in VSC):
   
    ```sh
    > Python: Select Interpreter
    .\venv\Scripts\python.exe # On macOS/Linux use './venv/bin/python'
    ```
8. Install the required packages:
   
    ```sh
    pip install -r requirements.txt
    ```

7. If you want to do a pull request which implies adding more dependencias, remember to update the requirements file using:
   
    ```sh
    pip freeze > requirements.txt
    ```

## Usage
There are several Python scripts containing the core code used in the Jupyter notebooks. Users can modify the dataset by editing `dataset.xlsx` and experiment with `analysis.ipynb` to gain insights into their academic performance.


## Contributors
- [![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/rorro6787) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/emilio-rodrigo-carreira-villalta-2a62aa250/) **Emilio Rodrigo Carreira Villalta**


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## Acknowledgements

- Inspired by various Youtube tutorials and resources on the PANDAS documentation




