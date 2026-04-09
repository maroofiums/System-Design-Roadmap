# DAY 7 — EVALUATION + SAVE MODEL

## Goal

Measure model performance, choose the best one, and save it for future use.

---

# 1. WHY EVALUATION IS IMPORTANT

After training, question is:

> “Is this model actually good?”

We don’t judge on training data — we use **test data**.

---

# 2. HOW WE MEASURE PERFORMANCE

---

## A) ACCURACY (Classification)

## Formula:

Accuracy = \frac{Correct\ Predictions}{Total\ Predictions}

---

## Meaning:

* How many predictions were correct

---

## Code:

```python id="accuracy_code"
from sklearn.metrics import accuracy_score

acc1 = accuracy_score(y_test, y_pred1)
acc2 = accuracy_score(y_test, y_pred2)

print(acc1, acc2)
```

---

## When to use:

* Balanced datasets

---

# 3. PRECISION & RECALL (Basic Idea)

---

## Precision

Precision = \frac{TP}{TP + FP}

👉 Out of predicted positives, how many are correct

---

## Recall

Recall = \frac{TP}{TP + FN}

👉 Out of actual positives, how many we found

---

## When important:

* Fraud detection
* Medical problems

---

# 4. RMSE (Regression)

If your problem is regression:

RMSE = \sqrt{\frac{1}{n}\sum (y - \hat{y})^2}

---

## Meaning:

* Measures prediction error
* Lower = better

---

# 5. PRACTICAL TASK FLOW

---

## Step 1 — Evaluate Models

```python id="eval_models"
print("Logistic:", accuracy_score(y_test, y_pred1))
print("Decision Tree:", accuracy_score(y_test, y_pred2))
```

---

## Step 2 — Compare

* Which model has higher accuracy?
* Which one generalizes better?

---

## Step 3 — Select Best Model

```python id="select_best"
best_model = model1  # example
```

---

# 6. SAVE MODEL (VERY IMPORTANT)

## Why save?

* So you don’t retrain every time
* Used in APIs (FastAPI later)

---

## Using joblib (recommended)

```python id="save_model"
import joblib

joblib.dump(best_model, "model.pkl")
```

---

## Load later:

```python id="load_model"
model = joblib.load("model.pkl")
```

---

# 7. OUTPUT OF DAY 7

By end of today:

✔ Models evaluated
✔ Best model selected
✔ Model saved as `.pkl`
✔ Ready for deployment (next phase)

---

# 8. COMMON MISTAKES

* Using only accuracy ❌
* Ignoring precision/recall ❌
* Saving wrong model ❌
* Not testing before saving ❌

---

# 9. FINAL WEEK 1 RESULT

You have built:

## Loan Prediction ML System (Local)

Includes:

* Clean dataset
* Encoded features
* Scaled data
* Trained models
* Evaluated results
* Saved `.pkl` model

---

# 10. BIG PICTURE

What you just completed:

```id="pipeline_done"
Data → Cleaning → Encoding → Scaling → Split → Train → Evaluate → Save
```

---

# 11. MINDSET

Now you understand:

> “ML is not about models — it’s about pipeline”

Most beginners only learn models
You learned the **full system flow**

---
