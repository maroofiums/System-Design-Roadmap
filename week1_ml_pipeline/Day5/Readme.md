# DAY 5 - TRAIN / TEST SPLIT

## Goal

Prepare data so the model can **learn and be tested fairly**

---

# 1. WHY WE SPLIT DATA

## Problem if we don’t split:

If you train and test on same data:

> Model just memorizes → looks perfect but fails in real world

---

## Solution:

Split data into two parts:

* **Training Data** → model learns
* **Testing Data** → model is evaluated

---

## Core Idea:

> Train on past → Test on unseen data

---

# 2. OVERFITTING vs GENERALIZATION

---

## Overfitting

Model memorizes training data:

* Very high training accuracy
* Poor test accuracy

👉 Bad model

---

## Generalization

Model learns patterns:

* Good training accuracy
* Good test accuracy

👉 Good model

---

## Intuition:

> A good model performs well on **new unseen data**

---

# 3. SPLIT RATIO

## Common:

* 80% → Training
* 20% → Testing

---

## Alternatives:

* 70/30
* 90/10 (large datasets)

---

# 4. PRACTICAL TASK

---

## Step 1 - Separate features and target

```python id="split_xy_day5"
X = df.drop("target", axis=1)
y = df["target"]
```

---

## Step 2 - Apply train_test_split

```python id="train_test_split_code"
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
```

---

## Parameters explained:

* `test_size=0.2` → 20% test data
* `random_state=42` → reproducible results

---

# 5. OUTPUT VARIABLES

After splitting:

* `X_train` → features for training
* `X_test` → features for testing
* `y_train` → labels for training
* `y_test` → labels for testing

---

# 6. IMPORTANT CHECK

```python id="shape_check"
print(X_train.shape, X_test.shape)
```

Expected:

* 80% training
* 20% testing

---

# 7. VERY IMPORTANT RULE (CRITICAL)

## Correct ML pipeline order:

1. Split data
2. Fit preprocessing on **training only**
3. Apply same transformation on test

---

## Why?

If you use full data before split:

> Data leakage → model cheats

---

# 8. COMMON MISTAKES

* Training on full dataset ❌
* Forgetting random_state ❌
* Data leakage (very dangerous) ❌
* Scaling before split ❌

---

# 9. OUTPUT OF DAY 5

By end of today:

✔ Dataset split into train/test
✔ Clear understanding of overfitting
✔ Ready for model training

---

# 10. MINDSET

Today you learned:

> “Model performance is not what it learns - but how it performs on unseen data”

---