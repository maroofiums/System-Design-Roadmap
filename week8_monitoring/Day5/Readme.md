# Day 5 - Concept Drift

# What is Concept Drift?

Concept drift happens when the relationship between input and output changes over time.

The model still receives similar data, but the meaning of patterns changes.

As a result:

* Old learned patterns become outdated
* Accuracy drops
* Predictions become unreliable

---

# Example

## Spam Detection in 2024

Spam words:

```text id="wb35tx"
FREE MONEY
WIN CASH
CLICK NOW
```

---

## Spam Detection in 2026

Spammers evolve:

```text id="4jw0rq"
Fr33 M0ney
Cl1ck Fast
100% Gu@ranteed
```

The old model no longer understands new spam patterns.

This is concept drift.

---

# Core Idea

The relationship changes:

```text id="h6vl7w"
Input → Output
```

The mapping learned during training becomes outdated.

---

# Difference Between Data Drift and Concept Drift

| Type          | Meaning                           |
| ------------- | --------------------------------- |
| Data Drift    | Input distribution changes        |
| Concept Drift | Input-output relationship changes |

---

# Example Comparison

## Data Drift

Training:

```python id="2dtt4q"
Age = 20-40
```

Production:

```python id="7ck4ri"
Age = 60-90
```

Inputs changed.

---

## Concept Drift

Inputs may stay similar, but labels/patterns change.

Example:

Old fraud behavior differs from modern fraud behavior.

---

# Why Concept Drift Happens

| Cause                 | Example                |
| --------------------- | ---------------------- |
| User behavior changes | New shopping habits    |
| Market changes        | Stock trends shift     |
| Attack evolution      | New spam/fraud methods |
| Social changes        | Language evolves       |
| Seasonal patterns     | Demand changes         |

---

# Detecting Concept Drift

Unlike data drift, concept drift is harder to detect.

We usually monitor:

* Accuracy
* Precision
* Recall
* Prediction behavior

---

# Common Detection Methods

# 1. Accuracy Monitoring

Track model accuracy over time.

Accuracy = \frac{Correct\ Predictions}{Total\ Predictions}

If accuracy continuously drops, concept drift may exist.

---

# 2. Sliding Window Evaluation

Compare recent performance against older performance.

Example:

| Window       | Accuracy |
| ------------ | -------- |
| Last Month   | 95%      |
| Current Week | 71%      |

Large drop indicates drift.

---

# 3. Recent-vs-Old Performance

Compare:

* Historical accuracy
* Current accuracy

---

# Practice Project

Goal:

* Train model on old data
* Test on changed data
* Observe accuracy degradation

---

# Install Requirements

```bash id="o8vzgi"
pip install pandas scikit-learn
```

---

# Step 1 - Create Old Dataset

# train.csv

```csv id="lb7k4q"
feature,label
1,0
2,0
3,0
4,1
5,1
6,1
```

---

# Step 2 - Create Changed Dataset

# production.csv

```csv id="d8tdfb"
feature,label
1,1
2,1
3,1
4,0
5,0
6,0
```

Notice:

* Input values remain similar
* Labels changed completely

This simulates concept drift.

---

# Step 3 - Build Performance Monitor

# performance_monitor.py

```python id="jlwm0g"
import pandas as pd

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

# Load training data
train_df = pd.read_csv("train.csv")

X_train = train_df[["feature"]]

y_train = train_df["label"]

# Train model
model = LogisticRegression()

model.fit(X_train, y_train)

# Load production data
prod_df = pd.read_csv("production.csv")

X_prod = prod_df[["feature"]]

y_prod = prod_df["label"]

# Predict
predictions = model.predict(X_prod)

# Calculate accuracy
accuracy = accuracy_score(
    y_prod,
    predictions
)

print(f"Accuracy: {accuracy:.2f}")

# Drift detection threshold
threshold = 0.60

if accuracy < threshold:

    print(
        "\nWARNING: Concept Drift Detected"
    )

else:

    print("\nModel Performance Stable")
```

---

# Run Project

```bash id="jlwmnd"
python performance_monitor.py
```

---

# Example Output

```text id="ol2i9q"
Accuracy: 0.00

WARNING: Concept Drift Detected
```

---

# Rolling Accuracy Monitoring

Instead of checking once, production systems monitor accuracy continuously.

Example:

| Day       | Accuracy |
| --------- | -------- |
| Monday    | 94%      |
| Tuesday   | 92%      |
| Wednesday | 81%      |
| Thursday  | 70%      |

Trend indicates concept drift.

---

# Simple Rolling Accuracy Example

```python id="3k2x3m"
accuracies = [
    0.95,
    0.93,
    0.90,
    0.82,
    0.75
]

rolling_accuracy = (
    sum(accuracies) / len(accuracies)
)

print(
    f"Rolling Accuracy: {rolling_accuracy}"
)
```

---

# Real-World Production Monitoring

Companies continuously track:

* Accuracy
* Precision
* Recall
* Confidence scores
* User feedback

When performance drops:

```text id="1z4z4d"
Retrain model
```

---

# What You Learned Today

# Concepts

* Concept drift
* Pattern evolution
* Performance degradation
* Accuracy monitoring

---

# Practical Skills

* Train simple classifier
* Monitor accuracy
* Detect concept drift
* Build performance monitoring pipeline

---

# Why Concept Drift Matters

A model can become useless even if:

* API works perfectly
* Infrastructure is healthy
* Data format looks normal

Because:

```text id="bq1bwv"
The world changes
```

Production ML systems must continuously adapt.

---

# Homework

Improve monitor:

Add:

* Precision tracking
* Recall tracking
* Accuracy history storage
* Visualization dashboard

---

# Mini Challenge

Create:

* Mild concept drift
* Moderate concept drift
* Severe concept drift

Then observe:

* Accuracy changes
* Drift warnings
* Rolling accuracy behavior
