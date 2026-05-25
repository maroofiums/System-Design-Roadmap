# Day 4 - Data Drift

# What is Data Drift?

Data drift happens when production data becomes different from training data.

The model was trained on one distribution, but real-world input changes over time.

As a result:

* Accuracy decreases
* Predictions become unreliable
* Model performance degrades

---

# Example

## Training Data

```python
Age: 20-40
```

## Production Data

```python 
Age: 60-90
```

The model never learned patterns for older users.

Prediction quality drops.

---

# Core Idea

# Distribution Shift

```text 
Training Data ≠ Production Data
```

This mismatch is called:

* Data Drift
* Covariate Shift
* Distribution Shift

---

# Why Data Drift Happens

## Common Causes

| Cause                 | Example               |
| --------------------- | --------------------- |
| User behavior changes | New shopping habits   |
| Seasonal effects      | Holiday traffic       |
| Market changes        | Price fluctuations    |
| Sensor changes        | Different devices     |
| Population changes    | New user demographics |

---

# Real-World Example

Suppose a fraud detection model was trained in 2024.

By 2026:

* Fraud patterns change
* User spending changes
* Attack techniques evolve

Old training data no longer represents reality.

---

# Detecting Data Drift

We compare:

* Training dataset
* Production dataset

If distributions differ significantly, drift exists.

---

# Statistical Detection Methods

# 1. Mean Comparison

Compare average values.

```math

\mu = \frac{1}{n}\sum_{i=1}^{n} x_i

```

Example:

| Dataset    | Mean Age |
| ---------- | -------- |
| Train      | 30       |
| Production | 75       |

Large difference may indicate drift.

---

# 2. Standard Deviation

Measures spread of data.

```math

\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2}

```

Higher variance may indicate unstable production behavior.

---

# 3. Histograms

Visual comparison of distributions.

Example:

```text 
Train:       #######
Production:  ##
```

---

# 4. KS Test (Kolmogorov-Smirnov Test)

Statistical test for comparing distributions.

It checks whether two datasets come from the same distribution.

---

# Practice Project

Goal:

Compare:

```python 
train.csv
production.csv
```

Check:

* Mean
* Variance
* Distribution differences

---

# Project Structure

```text 
Day4/
│
├── train.csv
├── production.csv
├── drift_detector.py
|__ Readme.md
```

---

# Step 1 - Create Example Datasets

# train.csv

```csv 
age
22
25
30
35
40
28
32
```

---

# production.csv

```csv 
age
65
70
75
80
85
90
72
```

---

# Step 2 - Install Requirements

```bash 
pip install pandas scipy matplotlib
```

---

# Step 3 - Build Drift Detector

# drift_detector.py

```python 
import pandas as pd
from scipy.stats import ks_2samp

# Load datasets
train_df = pd.read_csv("train.csv")

production_df = pd.read_csv(
    "production.csv"
)

# Select feature
train_age = train_df["age"]

production_age = production_df["age"]

# Mean comparison
train_mean = train_age.mean()

production_mean = production_age.mean()

print(f"Train Mean: {train_mean}")

print(
    f"Production Mean: {production_mean}"
)

# Variance comparison
train_var = train_age.var()

production_var = production_age.var()

print(f"Train Variance: {train_var}")

print(
    f"Production Variance: {production_var}"
)

# KS Test
statistic, p_value = ks_2samp(
    train_age,
    production_age
)

print(f"\nKS Statistic: {statistic}")

print(f"P-Value: {p_value}")

# Drift detection
if p_value < 0.05:

    print("\nWARNING: Data Drift Detected")

else:

    print("\nNo significant drift detected")
```

---

# Run Detector

```bash 
python drift_detector.py
```

---

# Example Output

```text 
Train Mean: 30.28
Production Mean: 76.71

Train Variance: 40.90
Production Variance: 70.23

KS Statistic: 1.0
P-Value: 0.00058

WARNING: Data Drift Detected
```

---

# Understanding KS Test

## P-Value Interpretation

| P-Value | Meaning                     |
| ------- | --------------------------- |
| < 0.05  | Significant drift           |
| ≥ 0.05  | No strong evidence of drift |

---

# Visual Drift Detection

You can also compare histograms.

## Add Visualization

```python 
import matplotlib.pyplot as plt

plt.hist(
    train_age,
    alpha=0.5,
    label="Train"
)

plt.hist(
    production_age,
    alpha=0.5,
    label="Production"
)

plt.legend()

plt.show()
```

---

# What You Learned Today

# Concepts

* Data drift
* Distribution shift
* Statistical comparison
* KS Test

---

# Practical Skills

* Compare datasets
* Detect drift
* Compute mean/variance
* Visualize distributions

---

# Why This Matters in Production

Companies continuously monitor drift because:

* Real-world data changes
* User behavior evolves
* Models degrade over time

Monitoring drift is critical for reliable ML systems.

---

# Homework

Improve drift detector:

Add:

* Multiple features
* Automatic threshold alerts
* Drift percentage
* Visualization saving

---

# Mini Challenge

Create datasets with:

* Small drift
* Moderate drift
* Severe drift

Then observe:

* Mean changes
* Variance changes
* KS Test results
