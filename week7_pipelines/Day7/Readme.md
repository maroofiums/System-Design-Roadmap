# Day 7 - Test + Review Day

## Overview

This day focuses on reviewing and validating everything learned throughout the Data Pipelines module.

The objective is to independently build a complete machine learning pipeline without relying on notes or step-by-step guidance.

This simulates real-world ML engineering scenarios where developers must design preprocessing systems, feature workflows, storage systems, and reusable pipelines independently.

---

# Test Yourself

Build a complete machine learning pipeline from scratch.

Your system should include:

```text 
Raw Dataset
→ Data Cleaning
→ Feature Engineering
→ Preprocessing
→ Model Training
→ Save Artifacts
→ Prediction
```

---

# Required Tasks

## 1. Load Dataset

Use either:

* Seaborn datasets
* Kaggle datasets
* UCI datasets

Example:

```python 
import seaborn as sns

df = sns.load_dataset("titanic")
```

---

## 2. Clean Data

Handle:

* Missing values
* Incorrect types
* Duplicate rows

Example:

```python 
df.drop_duplicates(inplace=True)

df["age"] = df["age"].fillna(df["age"].median())
```

---

# 3. Engineer Features

Create meaningful features such as:

## Family Size

```python 
df["family_size"] = df["sibsp"] + df["parch"] + 1
```

---

## Age Groups

```python 
pd.cut()
```

---

## Fare-Based Features

```python
fare_per_person
```

Goal:
Convert raw data into stronger predictive signals.

---

# 4. Train Model

Use:

* RandomForest
* Logistic Regression
* XGBoost (optional)

Example:

```python
RandomForestClassifier()
```

Train the model using:

* Pipeline
* ColumnTransformer

---

# 5. Save Artifacts

Save:

## Model

```python 
joblib.dump()
```

Example file:

```text 
pipeline.pkl
```

---

## Processed Dataset

Save using:

```python 
to_parquet()
```

Example:

```text 
processed_data.parquet
```

---

# Review Questions

## 1. Why use pipelines?

Pipelines automate preprocessing and modeling workflows while reducing repetitive code and preventing preprocessing inconsistencies.

Benefits:

* Cleaner architecture
* Easier deployment
* Reusable workflows
* Reduced human error

---

## 2. Why Parquet over CSV?

Parquet provides:

* Better compression
* Faster analytical queries
* Columnar storage
* Lower storage usage

CSV is simpler but inefficient for large-scale analytics and ML systems.

---

## 3. What causes data leakage?

Data leakage occurs when information from test data accidentally influences training.

Example mistakes:

* Fitting scalers before train-test split
* Using future information during training
* Target leakage

Leakage causes unrealistic model performance.

---

## 4. What is a feature store?

A feature store is a centralized system that stores reusable engineered features for:

* Training
* Validation
* Inference
* Production systems

It ensures consistency across ML workflows.

---


## 1. README

Include:

* Project overview
* Workflow explanation
* Technologies used
* Results

---

## 2. Architecture Diagram

Example:

```text 
Raw Data
→ Feature Engineering
→ Pipeline
→ Model
→ Saved Artifacts
→ Prediction
```

---

## 3. Results Section

Add:

* Accuracy
* Metrics
* Observations
* Feature engineering insights

---

# Goal

Ensure you can independently design and build production-style machine learning data pipelines.

---

# Outcome

After completing Day 7, you should understand:

* End-to-end ML workflows
* Pipeline automation
* Feature engineering systems
* Model serialization
* Efficient storage formats
* Production ML architecture
