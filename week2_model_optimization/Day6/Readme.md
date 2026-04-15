# 🟢 DAY 6 - Multi-Model System (Build Properly)

## 🎯 Core Idea

> Build once → reuse forever

Not:
❌ Random notebook code
But:
✅ Structured, reusable pipeline

---

# 🧠 1. What You Are Building

A system that:

1. Takes dataset
2. Trains multiple models
3. Evaluates using CV
4. Stores results
5. Selects best model

---

# ⚙️ STEP-BY-STEP IMPLEMENTATION

## 🔹 Step 1 - Imports

```python
import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
```

---

## 🔹 Step 2 - Load Dataset

```python
df = pd.read_csv("your_dataset.csv")

X = df.drop("target", axis=1)
y = df["target"]
```

---

## 🔹 Step 3 - Define Models

```python
def get_models():
    return {
        "logistic": LogisticRegression(max_iter=1000),
        "tree": DecisionTreeClassifier(),
        "forest": RandomForestClassifier()
    }
```

---

## 🔹 Step 4 - Evaluation Function (CORE)

```python
def evaluate_model(model, X, y):
    scores = cross_val_score(model, X, y, cv=5)
    return {
        "mean": scores.mean(),
        "std": scores.std(),
        "scores": scores
    }
```

---

## 🔹 Step 5 - Run Pipeline

```python
def run_pipeline(X, y):
    models = get_models()
    results = {}

    for name, model in models.items():
        result = evaluate_model(model, X, y)
        results[name] = result

    return results
```

---

## 🔹 Step 6 - Execute

```python
results = run_pipeline(X, y)

for name, res in results.items():
    print(f"{name}: Mean={res['mean']:.4f}, Std={res['std']:.4f}")
```

---

# 🧠 2. Why This is Powerful

You now have:

* Reusable evaluation
* Multiple model testing
* Stability tracking (std)

---

# 🧠 3. BEST MODEL SELECTION (IMPORTANT)

```python
def get_best_model(results):
    return max(results, key=lambda x: results[x]["mean"])

best_model_name = get_best_model(results)
print("Best model:", best_model_name)
```

---

# 🧠 4. OPTIONAL (BUT VERY STRONG)

## 🔹 Convert to DataFrame (clean output)

```python
results_df = pd.DataFrame(results).T
print(results_df)
```

---

## 🔹 Sort leaderboard

```python
results_df = results_df.sort_values(by="mean", ascending=False)
print(results_df)
```

---

# 🧠 5. What Makes This “Production Thinking”

You are now:

* Separating logic into functions
* Writing reusable code
* Tracking performance properly

---

# 🧠 6. Common Mistakes (Avoid)

❌ Hardcoding model everywhere
❌ No function structure
❌ Only printing accuracy
❌ Ignoring variance (std)

---

# ✅ FINAL OUTPUT (You MUST have)

### ✔ Working pipeline:

* Loads data
* Runs multiple models
* Uses cross-validation

### ✔ Results:

* Mean accuracy
* Std deviation

### ✔ Best model selected

---

# 🧠 FINAL MINDSET SHIFT

Before:
❌ “Let me try one model”

After:
✅ “Let me build a system that evaluates models properly”

---