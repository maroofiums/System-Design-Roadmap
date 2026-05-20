# Day 6 - Final Project: Pipeline System

## Overview

This project builds a complete end-to-end machine learning workflow using Scikit-learn pipelines and production-style preprocessing architecture.

The goal is to automate the entire ML process from raw data to prediction while following real-world machine learning engineering practices.

The project uses the Titanic dataset from [Seaborn Documentation](https://seaborn.pydata.org/generated/seaborn.load_dataset.html?utm_source=chatgpt.com).

---

# Project Goal

Build a production-style ML pipeline that performs:

```text id="jlwm2g"
Raw Dataset
→ Data Preprocessing
→ Feature Engineering
→ Model Training
→ Model Saving
→ Processed Data Storage
→ Prediction on New Data
```

---

# Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* PyArrow
* Seaborn

---

# Project Workflow

## Step 1 - Load Raw Dataset

Dataset loaded using:

```python id="ecpih9"
sns.load_dataset("titanic")
```

The dataset contains passenger information such as:

* Age
* Sex
* Fare
* Passenger class
* Embarked location
* Family information

---

## Step 2 - Data Preprocessing

Preprocessing includes:

### Numerical preprocessing

* Missing value imputation
* Standard scaling

### Categorical preprocessing

* Missing value handling
* One-hot encoding

Implemented using:

```python id="0f6uj3"
Pipeline()
ColumnTransformer()
```

---

# Step 3 - Feature Engineering

Custom engineered features include:

## Family Size

```python id="6gqwoj"
family_size = sibsp + parch + 1
```

Represents total family members aboard.

---

## Fare Per Person

```python id="p7t0qt"
fare_per_person = fare / family_size
```

Represents fare contribution per passenger.

---

## Age Group

Passengers grouped into:

* Child
* Teen
* YoungAdult
* Adult
* Senior

This captures non-linear age relationships.

---

# Step 4 - Model Training

Model used:

```python id="vuw9d4"
RandomForestClassifier
```

The model is trained entirely inside the pipeline architecture.

Benefits:

* Cleaner workflow
* Automated preprocessing
* Reduced human error
* Leakage prevention

---

# Step 5 - Save Model

The trained pipeline is saved using:

```python id="x3gkzy"
joblib.dump()
```

Saved file:

```text id="j1hl6m"
titanic_pipeline.pkl
```

This allows future reuse without retraining.

---

# Step 6 - Save Processed Dataset

Processed features are stored in Parquet format:

```python id="apjnzv"
to_parquet()
```

Saved file:

```text id="u0z5z0"
processed_titanic.parquet
```

Benefits of Parquet:

* Smaller storage size
* Faster analytics
* Efficient columnar storage
* Better production scalability

---

# Step 7 - Predict on New Data

The saved pipeline is reloaded and used for inference on unseen passenger data.

Example workflow:

```text id="4n7r0k"
New Passenger Data
→ Pipeline Preprocessing
→ Model Prediction
→ Survival Output
```

---

# Key Concepts Learned

## 1. ML Pipelines

Automate preprocessing and modeling in a single workflow.

---

## 2. ColumnTransformer

Apply different preprocessing steps to:

* Numerical columns
* Categorical columns

---

## 3. Feature Engineering

Create meaningful features from raw data.

---

## 4. Model Serialization

Save trained pipelines for deployment and reuse.

---

## 5. Efficient Data Storage

Use Parquet for scalable machine learning systems.

---

# Why This Project Matters

This project simulates how real production ML systems are built.

The same architectural ideas are used in:

* MLOps systems
* Recommendation engines
* Fraud detection pipelines
* Real-time ML applications
* Enterprise AI workflows

---

# Final Workflow

```text id="r40mo0"
Raw Dataset
→ Cleaning
→ Feature Engineering
→ Preprocessing Pipeline
→ Model Training
→ Save Pipeline
→ Save Processed Features
→ Predict on New Data
```

---

# Outcome

After completing this project, you should understand:

* End-to-end ML workflow design
* Production-style preprocessing
* Automated ML pipelines
* Feature engineering integration
* Model persistence
* Scalable storage systems
