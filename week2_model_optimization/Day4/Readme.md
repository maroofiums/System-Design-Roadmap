# 🟢 DAY 4 - Hyperparameter Tuning (Deep Understanding)

## 🎯 Core Idea

> Model performance is not fixed - it depends heavily on **hyperparameters**

---

# 🧠 1. What are Hyperparameters?

## 🔹 Definition

Hyperparameters are **settings you choose before training**

They control:

* Model complexity
* Learning behavior

---

## 🔹 Example (Random Forest)

```python
n_estimators → number of trees  
max_depth → depth of each tree  
```

---

## 🧠 Key Insight

> Model = Algorithm + Hyperparameters

---

# 🧠 2. Why Default is NOT Optimal

## 🔹 Problem

Libraries give **generic defaults**

But:

* Every dataset is different
* Optimal settings change

---

## 🔹 Example

| max_depth | Result       |
| --------- | ------------ |
| 2         | Underfitting |
| 10        | Good         |
| None      | Overfitting  |

---

## 🧠 Insight

> Hyperparameters control **bias–variance tradeoff**

---

# 🧠 3. Grid Search (Core Concept)

## 🔹 Idea

Try **all combinations** of parameters

---

## 🔹 Your Example

```python
params = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10]
}
```

---

## 🔹 Combinations Tried

```text
(50, 5)
(50, 10)
(100, 5)
(100, 10)
```

---

## 🧠 What happens internally?

For each combination:

1. Train model
2. Apply cross-validation
3. Compute mean score

---

## 🧠 Insight

> GridSearch = **CV + parameter search**

---

# ✍️ YOUR TASK - With Understanding

## Step 1: Run Grid Search

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

params = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10]
}

grid = GridSearchCV(
    RandomForestClassifier(),
    params,
    cv=5,
    scoring="accuracy"
)

grid.fit(X, y)

print("Best Params:", grid.best_params_)
print("Best Score:", grid.best_score_)
```

---

# 🧠 Step 2: Understand Output

## 🔹 Example Output

```text
Best Params: {'max_depth': 10, 'n_estimators': 100}
Best Score: 0.86
```

---

## 🔹 What it means

* These parameters gave the **best average CV performance**
* Not luck → **systematic search**

---

# 🧠 4. Most Important Thinking (DON’T SKIP)

## ❓ What is "Search Space"?

Search space = all possible combinations

---

### 🔹 Small Search Space

```python
[50, 100]
[5, 10]
```

✅ Fast
❌ Might miss best values

---

### 🔹 Large Search Space

```python
[50, 100, 200, 300]
[3, 5, 10, 20]
```

✅ Better results
❌ Slower

---

## 🧠 Insight

> Tuning = **balancing search quality vs computation cost**

---

# 🧠 5. Real Engineer Thinking

Instead of:
❌ “Let me try random values”

You think:
✅ “Let me define a smart search space and evaluate systematically”

---

# 🧠 6. Common Mistake (Avoid This)

❌ Tuning on test set
✔ Always use:

* Training + Cross-validation

---

# 🧠 7. Advanced Insight (Important)

## 🔹 Over-Tuning Problem

If search space is too large:

* Model adapts to validation folds
* Can overfit CV itself

---

## 🧠 Solution

* Keep search reasonable
* Use domain knowledge

---

# ✅ OUTPUT (What you must write)

---

## 🔹 Best Parameters

* n_estimators: 2
* max_depth: 100

---

## 🔹 Best CV Score

* Accuracy: ___

---

## 🔹 Understanding

* Hyperparameters control model behavior
* Grid search tests combinations systematically
* Cross-validation ensures reliable evaluation

---

# 🧠 FINAL MINDSET SHIFT

Before:
❌ “Model is bad”

After:
✅ “Model needs tuning - let me search optimal parameters”

---
