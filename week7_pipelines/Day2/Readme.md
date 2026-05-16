# Day 2 - Advanced Feature Engineering

## Overview

This day focuses on advanced feature engineering techniques used in real-world machine learning pipelines. The goal is to transform raw data into meaningful features that improve model performance.

Feature engineering is often more important than the model itself, as it directly impacts how well the model can learn patterns from data.

---

## Objectives

By the end of this module, you will understand and apply:

* Date-time feature extraction
* Text feature basics
* Binning (discretization)
* Log transformation
* Outlier handling
* Polynomial feature generation

---

## Key Concepts

### 1. Date-Time Feature Extraction

Real-world datasets often contain timestamps that must be broken into meaningful components.

Common extracted features:

* Year
* Month
* Day
* Day of week
* Hour

These features help models capture time-based patterns such as seasonality or trends.

---

### 2. Text Feature Basics

Machine learning models cannot directly interpret raw text. Simple transformations include:

* Text length
* Word count
* Keyword presence indicators

These features help capture basic structure and meaning from text data.

---

### 3. Binning (Discretization)

Binning converts continuous numerical values into categorical groups.

Example:

* Age → Child, Adult, Senior

Binning helps reduce noise and capture non-linear relationships.

---

### 4. Log Transformation

Used to reduce skewness in data distributions.

Common use cases:

* Income
* Population
* Price data

Log transformation helps stabilize variance and improve model learning.

---

### 5. Outlier Handling

Outliers can distort model performance and training stability.

Common techniques:

* IQR-based filtering
* Value clipping (capping)
* Statistical threshold removal

Proper handling improves model robustness.

---

### 6. Polynomial Features

Polynomial features allow linear models to capture non-linear relationships by creating feature interactions such as:

* x
* x²
* x³

This increases model flexibility without changing the model type.

---

## Practice Task

Use a messy dataset from Kaggle or UCI repository and perform the following:

### Required Feature Engineering

* Extract date-time features (if applicable)
* Create text-based features (length, counts, keywords)
* Handle outliers using statistical methods

---

## Mini Task

Train a machine learning model twice:

### Model 1: Baseline

* Minimal preprocessing
* Raw features only

### Model 2: Feature Engineered

* Apply all advanced feature engineering techniques

---

## Evaluation

Compare both models using:

* Accuracy (classification)
* RMSE or R² (regression)

Analyze the difference in performance.

---

## Goal

Understand how advanced feature engineering improves model performance by converting raw data into structured, meaningful representations.

---

## Outcome

After completing this module, you should be able to:

* Transform raw datasets into structured feature sets
* Identify useful vs noisy transformations
* Improve model performance through feature engineering
* Understand real-world ML preprocessing workflows
