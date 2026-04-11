# 📅 WEEK 2 - Model Optimization (Day-wise Plan)

## 🎯 Weekly Outcome

By the end, you will have:

* Deep understanding of optimization concepts
* A **Multi-Model ML System (project)**
* Clean, reusable evaluation pipeline

---

# 🟢 DAY 1 - Overfitting vs Underfitting

## 🎯 Goal

Understand **why models fail**

---

## 🧠 Concepts (1.5–2 hrs)

* What is learning vs memorization
* Underfitting (too simple)
* Overfitting (too complex)
* Train vs Test performance gap

---

## ✍️ Task (1–2 hrs)

### 1. Train simple vs complex models

```python
from sklearn.tree import DecisionTreeClassifier

# underfitting
model1 = DecisionTreeClassifier(max_depth=1)

# overfitting
model2 = DecisionTreeClassifier(max_depth=None)
```

### 2. Compare:

* Train accuracy
* Test accuracy

---

## 🧠 Focus

* See the **gap**, not just accuracy
* Build intuition: *why did this happen?*

---

## ✅ Output

* Notes + observations:

  * Which model overfit?
  * Which underfit?

---

# 🟢 DAY 2 - Bias vs Variance

## 🎯 Goal

Understand **root cause of errors**

---

## 🧠 Concepts (1.5 hrs)

* Bias = wrong assumptions
* Variance = sensitivity to data
* Relation to overfitting/underfitting

---

## ✍️ Task (1.5 hrs)

Write in your own words:

* Why high bias = underfitting
* Why high variance = overfitting

---

### Mini Experiment

* Train same model on:

  * small dataset
  * slightly different dataset

Observe prediction changes

---

## 🧠 Focus

Think like:

> "Is my model failing because it's dumb or unstable?"

---

## ✅ Output

* Clean written explanation (very important for interviews)

---

# 🟢 DAY 3 - Cross Validation (Core Day)

## 🎯 Goal

Stop relying on **lucky splits**

---

## 🧠 Concepts (1–1.5 hrs)

* Why train/test split is unreliable
* K-Fold Cross Validation
* Mean score as true performance

---

## ✍️ Task (2 hrs)

### Implement CV

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

scores = cross_val_score(model, X, y, cv=5)

print(scores)
print(scores.mean())
```

---

## 🧠 Focus

* Don’t just run → understand:

  * Why multiple splits?
  * Why average?

---

## ✅ Output

* CV working on your dataset
* Mean accuracy noted

---

# 🟢 DAY 4 - Hyperparameter Tuning

## 🎯 Goal

Learn how to **improve models systematically**

---

## 🧠 Concepts (1.5 hrs)

* What are hyperparameters
* Why default is not optimal
* Grid Search idea

---

## ✍️ Task (2 hrs)

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

params = {
    "n_estimators": [50, 100],
    "max_depth": [5, 10]
}

grid = GridSearchCV(RandomForestClassifier(), params, cv=5)
grid.fit(X, y)

print(grid.best_params_)
```

---

## 🧠 Focus

* Understand search space
* Don’t memorize → understand tuning logic

---

## ✅ Output

* Best hyperparameters found
* Notes: *why those worked better*

---

# 🟢 DAY 5 - Model Comparison

## 🎯 Goal

Think like a **decision-maker**

---

## 🧠 Concepts (1 hr)

* No model is universally best
* Always compare

---

## ✍️ Task (2–3 hrs)

Train:

* Logistic Regression
* Decision Tree
* Random Forest

---

### Compare using CV

```python
models = {
    "logistic": LogisticRegression(),
    "tree": DecisionTreeClassifier(),
    "forest": RandomForestClassifier()
}

results = {}

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5)
    results[name] = scores.mean()

print(results)
```

---

## 🧠 Focus

* Which model generalizes best?
* Not just highest score → consistency

---

## ✅ Output

* Comparison table
* Best model identified

---

# 🟢 DAY 6 - PROJECT: Multi-Model System (Build)

## 🎯 Goal

Build **real ML pipeline**

---

## ✍️ Task (3–4 hrs)

### Build system:

1. Load dataset
2. Define multiple models
3. Run cross-validation
4. Store results

---

### Structure

```python
def evaluate_model(model, X, y):
    scores = cross_val_score(model, X, y, cv=5)
    return scores.mean()
```

---

## 🧠 Focus

* Clean code
* Reusability

---

## ✅ Output

* Working pipeline
* Multiple models evaluated

---

# 🟢 DAY 7 - Finalize + Save Best Model

## 🎯 Goal

Make it **complete system**

---

## ✍️ Task (2–3 hrs)

### 1. Select best model

```python
best_model_name = max(results, key=results.get)
```

---

### 2. Train on full data

```python
best_model = models[best_model_name]
best_model.fit(X, y)
```

---

### 3. Save model

```python
import pickle

with open("best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)
```

---

## 🧠 Bonus (Optional but powerful)

* Save results as JSON
* Print leaderboard

---

## ✅ Final Output (VERY IMPORTANT)

You now have:

* Multi-model system
* Cross-validation pipeline
* Tuned model
* Saved `.pkl` file

---
