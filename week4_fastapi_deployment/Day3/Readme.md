# Day3 - Iris Flower Classification using Random Forest

A complete Machine Learning project that trains a **Random Forest Classifier** on the famous **Iris Flower Dataset** and saves the trained model for deployment or future inference.

This project demonstrates the full beginner-friendly ML workflow:

- Data Loading
- Train/Test Split
- Model Training
- Evaluation
- Model Serialization
- Deployment Preparation

---

# Project Structure

```text
Day3/
┣ Model/
┃ ┗ iris_model.joblib
┣ Notebook/
┃ ┗ model.ipynb
┗ Readme.md
````

---

# About the Dataset

The **Iris dataset** is one of the most well-known datasets in Machine Learning.

It contains flower measurements from three species of Iris flowers.

## Classes

* Iris Setosa
* Iris Versicolor
* Iris Virginica

## Features

Each flower contains 4 input features:

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

## Dataset Size

* Total Samples: 150
* Classes: 3
* Balanced Dataset

Dataset loaded from Scikit-learn:

```python id="ub8ttn"
from sklearn.datasets import load_iris
```

---

# Project Objective

Train a machine learning classification model that predicts the flower species using the 4 numerical features.

---

# Technologies Used

* Python
* Scikit-learn
* Random Forest Classifier
* Joblib
* NumPy
* Jupyter Notebook

---

# Why Random Forest?

Random Forest is a powerful ensemble algorithm that combines many decision trees.

## Benefits:

* High Accuracy
* Handles Non-linearity
* Less Overfitting than single trees
* Strong default performance
* Great for beginners and production baselines

---

# Machine Learning Workflow

## 1. Import Libraries

```python id="2n2i06"
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
```

---

## 2. Load Dataset

```python id="mz8s7f"
X, y = load_iris(return_X_y=True)
```

Where:

* `X` = Input Features
* `y` = Target Labels

---

## 3. Train/Test Split

```python id="x3crk4"
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

## Why Split Data?

To test model performance on unseen data.

* 80% Training Data
* 20% Testing Data

---

## 4. Create Model

```python id="66j9j0"
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

## Parameters:

* `n_estimators=100` → 100 decision trees
* `random_state=42` → reproducible results

---

## 5. Train Model

```python id="n2ij0k"
model.fit(X_train, y_train)
```

The model learns relationships between flower measurements and species labels.

---

## 6. Make Predictions

```python id="o6q2vl"
y_pred = model.predict(X_test)
```

---

## 7. Evaluate Performance

```python id="uj0c7r"
print(classification_report(y_test, y_pred))
```

Example output:

```text
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       1.00      1.00      1.00         9
           2       1.00      1.00      1.00        11

    accuracy                           1.00        30
```

---

# Understanding Metrics

## Precision

How many predicted positives were correct.

## Recall

How many actual positives were found.

## F1 Score

Balance between precision and recall.

## Accuracy

Overall correct predictions.

---

# Save Trained Model

```python id="iv2llk"
joblib.dump(model, "Model/iris_model.joblib")
```

This stores the trained model file for later use.

---

# Load Model Later

```python id="e8n9k2"
import joblib

model = joblib.load("Model/iris_model.joblib")
```

---

# Predict New Flower

```python id="g7y2kz"
sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample)

print(prediction)
```

Output:

```text
[0]
```

Where:

* 0 = Setosa
* 1 = Versicolor
* 2 = Virginica

---

# Convert Prediction to Flower Name

```python id="4xkp4x"
flower_names = ["Setosa", "Versicolor", "Virginica"]

print(flower_names[prediction[0]])
```

---

# How to Run Project

## Step 1: Install Requirements

```bash id="2c4x49"
pip install scikit-learn joblib notebook
```

## Step 2: Run Notebook

```bash id="8op2ib"
jupyter notebook
```

Open:

```text
Notebook/model.ipynb
```

---

# Use Cases

Although beginner-friendly, this project demonstrates concepts used in:

* Agriculture AI
* Plant Recognition Apps
* Biological Classification
* ML Deployment APIs
* Production Pipelines

---

# Future Improvements

## Model Side

* Hyperparameter Tuning
* Cross Validation
* Feature Importance Analysis
* Compare Multiple Models

## Deployment Side

* FastAPI API
* Streamlit Web App
* Docker Container
* Cloud Deployment

## Engineering Side

* Logging
* Unit Tests
* CI/CD Pipeline

---

# What I Learned

Through this project I practiced:

* Classification Workflow
* Random Forest Algorithm
* Data Splitting
* Performance Metrics
* Model Saving
* Production Readiness

---