Bike Sharing Demand — Machine Learning Regression Project
    Overview

This project predicts the number of rented bikes in an hour using weather, seasonality and time-based features.
It replicates a real analytical workflow: exploring the data, building features, training ML models, and evaluating performance.

The project is part of my application to the Vinted Data Science & Analytics Academy, demonstrating end-to-end data processing and model design skills.

    Dataset

Source: Kaggle — Bike Sharing Demand
Files used:

train.csv

test.csv

Rows: 10,886
Target variable: count — number of rented bikes in each hour.
    
    Tools & Libraries

Python

Pandas, NumPy

Scikit-Learn

Matplotlib

Jupyter Notebook

    Step-by-Step Workflow
1. Exploratory Data Analysis (EDA)

Converted datetime column into year, month, hour, weekday

Explored demand patterns:

Rental count peaks around 8:00 and 17:00

Higher demand in warmer temperatures

Bad weather → significantly fewer rentals

Clear weekly and monthly seasonalities


Random Forest performed significantly better than Decision Tree.

    Conclusions

Time-related patterns are the primary drivers of bike demand.

Environmental conditions significantly influence rentals.

Random Forest is an effective model for this task.

This style of analysis directly matches the responsibilities in Decision Science and Data Science roles.