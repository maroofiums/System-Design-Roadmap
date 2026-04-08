# DAY 6 - MODEL TRAINING

## Goal

Train ML models to **learn patterns from data and make predictions**

---

# 1. HOW ML LEARNS PATTERNS

## Core Idea:

Model tries to learn a function:

y = f(X)

* X → features (input)
* y → target (output)
* f → learned pattern

---

## What happens during training:

* Model looks at X and y
* Finds relationships
* Minimizes error
* Stores learned patterns

---

# 2. BASIC MODELS (YOU MUST KNOW)

---

## 1. Linear Regression (Regression)

### Use:

* Predict numbers

Example:

* House price
* Salary

---

## 2. Logistic Regression (Classification)

### Use:

* Predict categories (0/1)

Example:

* Loan approved or not
* Spam detection

---

## 3. Decision Tree (Both)

### Use:

* Works for classification & regression
* Learns decision rules

Example:

* If income > 50k → approve loan

---

# 3. PRACTICAL TASK FLOW

---

## Step 1 - Import Models

```python id="import_models"
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
```

---

## Step 2 - Initialize Models

```python id="init_models"
model1 = LogisticRegression()
model2 = DecisionTreeClassifier()
```

---

## Step 3 - Train (Fit)

```python id="train_models"
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
```

---

## What “fit” means:

> Model learns from training data

---

## Step 4 - Predict

```python id="predict_models"
y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)
```

---

## What “predict” means:

> Model gives output for unseen data

---

# 4. OUTPUT OF DAY 6

By end of today:

✔ At least 2 trained models
✔ Predictions generated
✔ Models ready for evaluation

---

# 5. IMPORTANT INSIGHT

Different models learn differently:

* Logistic Regression → linear relationship
* Decision Tree → rule-based

👉 That’s why results may differ

---

# 6. COMMON MISTAKES

* Training on full dataset ❌
* Using test data for training ❌
* Not comparing models ❌
* Ignoring model assumptions ❌

---

# 7. MINDSET

Today’s key idea:

> “Model is just a function that learns patterns from data”

You are not coding logic - you are letting the model **learn logic**

---