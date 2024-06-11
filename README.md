# Spatial Plan Data Analysis

This project is a part of my thesis research on implementing LADM into the automated permit checks pipeline for the case study Estonia. It aims to analyze Estonian spatial plan data semantics using machine learning techniques.

## Overview

The main objective of this project is to extract insights from Estonian spatial plan data using data analysis and machine learning. The project involves several steps including data preprocessing, feature engineering, model training, and evaluation.

### Additional Step: Test Model Script

As an additional step to the main thesis research, a test model script (fme2result.py) has been integrated into the project. This script first runs an FME script to extract input data from real Estonian spatial plan data, then generates synthetic data, creates a training model, and finally tests the input data against the model to predict layer names.

## Usage

1. Run `run_all.py` to create synthetic data for Estonian detailed planning semantics, creating a training model using this and testing the `input.csv` file against the model to predict layer names.
2. Run `fme2result.py` to execute the FME script, generate synthetic data, and test the model against the input data extracted from real Estonian spatial plan data.

## Data Sources

The input data (`input.csv`) used in the `fme2result.py` script is extracted from real Estonian spatial plan data. The data extraction is performed using FME scripts developed during the thesis research. The original data sources are not included in this repository due to privacy and licensing restrictions.

## Links

Main Thesis Research GitHub Repository: [link](https://github.com/simaybtm/xxx)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
