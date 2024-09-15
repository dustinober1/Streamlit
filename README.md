# Streamlit Projects

This repository contains several data science and machine learning applications developed using Streamlit, a popular Python library for building interactive web applications.

## Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [DNA Count](#dna-count)
  - [EDA Basketball](#eda-basketball)
  - [Leidos Stock](#leidos-stock)
- [Environment Setup](#environment-setup)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository showcases different Streamlit applications, including DNA sequence analysis, exploratory data analysis (EDA) on basketball data, and stock price visualization. Each project is a standalone Streamlit application that can be run locally to explore the respective data science topics.

## Projects

### DNA Count

An interactive Streamlit app that performs DNA sequence analysis. The app takes a DNA sequence as input and provides the count of each nucleotide (A, T, G, C) in the sequence.

[Project Content](https://github.com/dustinober1/Streamlit/tree/main/DNA%20Count)

### EDA Basketball

A Streamlit app for performing exploratory data analysis (EDA) on basketball datasets. It allows users to visualize player statistics, team performance, and other basketball metrics.

[Project Content](https://github.com/dustinober1/Streamlit/tree/main/EDA%20Basketball)

### Leidos Stock

A Streamlit app that visualizes stock price data for Leidos Holdings, Inc. The app provides interactive charts to explore historical stock prices, moving averages, and other financial metrics.

[Project Content](https://github.com/dustinober1/Streamlit/tree/main/Leidos%20Stock)

## Environment Setup

To run the Streamlit apps, you need to set up the required Python environment. You can create a virtual environment and install the necessary dependencies using the `env.yml` file provided in the repository.

1. **Create a virtual environment**:

    ```bash
    conda env create -f env.yml
    ```

2. **Activate the environment**:

    ```bash
    conda activate streamlit-env
    ```

3. **Run a Streamlit app**:

    Navigate to the project directory and run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

   Replace `app.py` with the respective Python file name for the project you want to run.

## Contributing

Contributions are welcome! If you have ideas for improving the apps, adding new features, or any other suggestions, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
