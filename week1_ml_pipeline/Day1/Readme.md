# DAY 1 - Dataset Understanding + Setup Concepts

## Goal

Understand what a dataset is, how it is structured, and how to load and inspect it using Pandas.

---

## 1. What is a Dataset?

A dataset is a collection of data used to train or test machine learning models.

It is usually organized in a table format:

* Rows represent individual data points (samples)
* Columns represent attributes (features)

---

## 2. Rows vs Columns

### Rows

Each row represents one example in the dataset.
Example: one student, one house, one customer

### Columns

Each column represents a property (feature) of the data.
Example: age, salary, marks, price

---

## 3. Features vs Target (Label)

### Features (X)

Input variables used to make predictions.
Example: study hours, income, area size

### Target (y)

What you want to predict.
Example: exam score, house price, spam or not spam

---

## 4. Problem Framing

### Classification

Predict a category or class:

* Spam or not spam
* Disease yes or no
* Dog vs cat

### Regression

Predict a continuous number:

* House price
* Temperature
* Salary

---

## 5. Loading Dataset (Pandas)

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

---

## 6. Inspecting Data

### View first rows

```python
df.head()
```

### Dataset information

```python
df.info()
```

Shows:

* column names
* data types
* missing values

### Statistical summary

```python
df.describe()
```

Shows:

* mean
* min and max
* standard deviation
* quartiles

---

## 7. Identify Target and Features

### Check columns

```python
df.columns
```

### Define features and target

```python
X = df.drop("target_column", axis=1)
y = df["target_column"]
```

---

## Quick Checklist

* Dataset loaded
* Rows and columns understood
* Features and target identified
* Problem type (classification or regression) defined
* Data inspected using head, info, and describe

---

## Outcome of Day 1

By the end of this day, you should be able to:

* Understand dataset structure
* Load data using Pandas
* Separate features and target
* Identify problem type correctly
