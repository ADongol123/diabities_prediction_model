# Diabetes Classification Project

## Overview
This project analyzes the diabetes dataset from Kaggle. The goal is to compare various input features against the outcome of diabetes diagnosis. Visualizations using Matplotlib are employed to provide insights into the data.

## Dataset
- **Source**: Kaggle `https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database`
- **Description**: The dataset contains several medical predictor variables and one target variable, which indicates whether a patient is diabetic or not.

## Features
- Number of Pregnancies
- Glucose Concentration
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

## Methodology
1. **Data Preprocessing**: Data cleaning and normalization techniques were applied to prepare the dataset for training.
2. **Model**: A feedforward neural network was built using PyTorch. The architecture consists of:
   - An input layer that takes 8 features.
   - Two hidden layers with 20 neurons each, activated by the ReLU function.
   - An output layer that provides two outputs corresponding to the binary classification of diabetes.

3. **Loss Function**: CrossEntropyLoss was used to evaluate the model's performance, as it is suitable for multi-class classification problems.
4. **Optimizer**: The Adam optimizer was employed for optimizing the model parameters, known for its efficiency and effectiveness.

## Training and Testing the Model
The model was trained for 1000 epochs. During training:
- The model's predictions were compared against the actual training labels to calculate the loss.
- The optimizer updated the model parameters to minimize the loss.
- Periodic evaluations were made on a separate test set to monitor the model's performance.