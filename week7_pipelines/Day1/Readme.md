# Day 1 - Feature Engineering Fundamentals 

This project demonstrates the fundamental steps of **feature engineering** using the Titanic dataset from Seaborn.

The goal is to transform raw, messy data into clean, machine-learning-ready features.

---

## Project Workflow

Raw Dataset
→ Handle Missing Values
→ Encode Categorical Features
→ Scale Numerical Features
→ Train Model

---

## Dataset

Dataset used: **Titanic Dataset**

Loaded using:

```python
sns.load_dataset("titanic")
```

Selected features:

* `survived` → Target variable
* `pclass`
* `sex`
* `age`
* `fare`
* `embarked`

---

## Feature Engineering Steps

### 1. Handling Missing Values

Missing values in numerical columns were filled using median:

```python
df["age"] = df["age"].fillna(df["age"].median())
```

Missing values in categorical columns were filled using mode:

```python
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
```

---

## 2. Encoding Categorical Features

Categorical values such as `sex` and `embarked` were converted into numerical format using `LabelEncoder`.

```python
from sklearn.preprocessing import LabelEncoder
```

---

## 3. Feature Scaling

Numerical columns were standardized using `StandardScaler`.

genui{"math_block_widget_always_prefetch_v2":{"content":"z = \frac{x-\mu}{\sigma}"}}

```python
from sklearn.preprocessing import StandardScaler
```

Scaled columns:

* Age
* Fare

---

## 4. Model Training

A basic Logistic Regression model was trained after preprocessing.

Algorithm used:

Logistic Regression

---

## Technologies Used

* Python
* Pandas
* Seaborn
* Scikit-learn

---

## Learning Outcomes

After completing this project, I learned:

* Why raw data is rarely model-ready
* Handling missing values
* Encoding categorical features
* Feature scaling
* Basic feature engineering workflow
* Preparing datasets for machine learning models

---


## Final Result

Successfully converted raw Titanic dataset into a clean dataset ready for machine learning training.
