# DAY 4 - FEATURE SCALING

## Goal

Bring all numerical features to the same scale so ML models perform better.

---

# 1. WHY SCALING IS NEEDED

## Problem in real data:

Features often have different ranges:

* Age → 0 to 100
* Salary → 10,000 to 500,000
* Distance → 0 to 50

---

## Why this is a problem?

Some models get biased toward large values:

> Salary dominates Age just because it has bigger numbers

---

## Result without scaling:

* Poor accuracy
* Slow learning
* Unstable models

---

# 2. WHEN SCALING MATTERS MOST

## Very important for:

* Logistic Regression
* KNN
* SVM
* Neural Networks
* Gradient-based models

## Less important for:

* Decision Trees
* Random Forest

---

# 3. TWO MAIN SCALING METHODS

---

# A) STANDARDIZATION (Z-SCORE)

## Idea:

Convert data so it has:

* Mean = 0
* Standard deviation = 1

---

## Formula:

genui{"math_block_widget_always_prefetch_v2":{"content":"z = \frac{x - \mu}{\sigma}"}}

---

## Meaning:

* x = original value
* μ = mean
* σ = standard deviation

---

## Code:

```python id="std_scaling"
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df[["age", "salary"]] = scaler.fit_transform(df[["age", "salary"]])
```

---

## When to use:

* Data is normally distributed
* Most ML problems (default choice)

---

# B) NORMALIZATION (MIN-MAX SCALING)

## Idea:

Scale data between 0 and 1

---

## Formula:

x' = \frac{x - x_{min}}{x_{max} - x_{min}

---

## Code:

```python id="minmax_scaling"
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[["age", "salary"]] = scaler.fit_transform(df[["age", "salary"]])
```

---

## When to use:

* Neural networks
* Image / bounded data
* When you want fixed range [0,1]

---

# 4. IMPORTANT RULE (VERY IMPORTANT)

## NEVER scale target column

Example:

* y = loan_status ❌ (do NOT scale)

Only scale:

* X (features)

---

# 5. PRACTICAL TASK FLOW

---

## Step 1 - Select numeric columns

```python id="num_cols"
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
```

---

## Step 2 - Apply scaling

### Standardization (recommended)

```python id="apply_scaling"
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df[num_cols] = scaler.fit_transform(df[num_cols])
```

---

## Step 3 - Keep target separate

```python id="split_xy"
X = df.drop("target", axis=1)
y = df["target"]
```

---

# 6. OUTPUT OF DAY 4

By end of today:

✔ All numerical features scaled
✔ Same range for all features
✔ Target column unchanged
✔ Dataset ready for model training

---

# 7. COMMON MISTAKES

* Scaling target column ❌
* Fitting scaler on test data ❌
* Not understanding difference between normalization & standardization
* Applying scaling before train/test split ❌

---

# 8. VERY IMPORTANT ML RULE

## Correct pipeline order:

1. Split data
2. Fit scaler on training data
3. Transform test data

---

# 9. MINDSET

Today you learned:

> “Scaling is not data change - it is data alignment”

It helps models “see features equally”.

---
