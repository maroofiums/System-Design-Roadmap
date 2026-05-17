# Day 3 - Building Data Pipelines

## Overview

This module focuses on building automated machine learning pipelines using Scikit-learn.

In real-world machine learning systems, manually cleaning data, encoding features, scaling values, and training models step-by-step becomes inefficient and error-prone.

Pipelines solve this problem by automating the entire workflow.

---

# What is an ML Pipeline?

An ML pipeline is a sequence of automated steps that transforms raw data into predictions.

Typical workflow:

```text
Raw Data
→ Data Cleaning
→ Feature Engineering
→ Encoding
→ Scaling
→ Model Training
→ Prediction
```

Instead of manually repeating these steps every time, pipelines automate the process.

---

# Why Pipelines Matter in Production

Without pipelines:

* Repetitive code
* Higher chance of mistakes
* Difficult deployment
* Harder maintenance
* Risk of inconsistent preprocessing

With pipelines:

* Cleaner code
* Reusable workflows
* Easier deployment
* Consistent preprocessing
* Better scalability

This is heavily used in production ML systems.

---

# Scikit-learn Pipeline

Scikit-learn provides:

```python
from sklearn.pipeline import Pipeline
```

It allows chaining multiple steps together.

Example:

```python
Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])
```

Flow:

```text
Input Data → Scaling → Model → Prediction
```

---

# ColumnTransformer

Real datasets usually contain:

* Numerical columns
* Categorial columns
* Text columns

Different columns require different preprocessing.

Scikit-learn provides:

```python
from sklearn.compose import ColumnTransformer
```

Example:

* Numerical columns → Scaling
* Categorical columns → One Hot Encoding

---

## Example Flow

```text
Age, Salary → StandardScaler
Gender, City → OneHotEncoder
```

Then combine both outputs into one dataset.

---

# Preventing Data Leakage

Data leakage happens when information from test data accidentally influences training.

Example mistake:

```python
scaler.fit(test_data)
```

This leaks test information.

---

## Correct Approach

```python
scaler.fit(train_data)
scaler.transform(test_data)
```

Pipelines automatically prevent this issue during training.

---

# Practice Task

Build:

## Preprocessing Pipeline

Handle:

* Missing values
* Scaling
* Encoding

---

## Model Pipeline

Connect preprocessing with model training.

Example:

```text
Raw Data
→ Missing Value Handling
→ Encoding
→ Scaling
→ Model
```

---

# Full Example Workflow

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("titanic.csv")

# Features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Column selection
numeric_features = ["Age", "Fare"]
categorical_features = ["Sex", "Embarked", "Pclass"]

# Numeric pipeline
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Categorical pipeline
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# Combine pipelines
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

# Full model pipeline
model_pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", RandomForestClassifier())
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model_pipeline.fit(X_train, y_train)

# Predict
predictions = model_pipeline.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
```

---

# Mini Task

Train one complete model using pipeline architecture.

Requirements:

* Handle missing values
* Encode categorical data
* Scale numerical data
* Train model
* Make predictions

---

# Goal

Automate preprocessing workflows and prepare your machine learning systems for production-ready development.

---

# Outcome

After completing this module, you will understand:

* End-to-end ML automation
* Reusable preprocessing workflows
* Proper production practices
* Data leakage prevention
* Scikit-learn pipeline architecture

This is one of the most important skills for real ML engineering and MLOps workflows.
