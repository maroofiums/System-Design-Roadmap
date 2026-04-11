# 🟢 DAY 1 - Overfitting vs Underfitting (Deep Notes)

## 🎯 Core Idea

A model can fail in **two fundamentally different ways**:

* It **fails to learn** → Underfitting
* It **learns too much (memorizes)** → Overfitting

---

# 🧠 1. Learning vs Memorization

## 🔹 Learning

Model captures **general patterns**

Example:

> “If feature increases → output increases”

✅ Works on new data

---

## 🔹 Memorization

Model remembers **exact training points**

Example:

> “If x = 5.23 → y = 10.91”

❌ Fails on new data

---

## 🧠 Key Insight

> ML is not about fitting training data - it's about **generalizing to unseen data**

---

# 🧠 2. Underfitting (Too Simple)

## 🔹 Definition

Model is **too weak** to capture patterns

## 🔹 Your Example

```python
DecisionTreeClassifier(max_depth=1)
```

This is basically:

* One split only
* Very limited logic

---

## 🔹 Expected Behavior

| Metric         | Value |
| -------------- | ----- |
| Train Accuracy | Low   |
| Test Accuracy  | Low   |

---

## 🔹 Why?

Model cannot represent complexity of data

---

## 🧠 Intuition

> It’s like trying to solve a complex problem with a very dumb rule

---

# 🧠 3. Overfitting (Too Complex)

## 🔹 Definition

Model is **too powerful** → memorizes data

## 🔹 Your Example

```python
DecisionTreeClassifier(max_depth=None)
```

This means:

* Tree grows until pure leaves
* Memorizes dataset

---

## 🔹 Expected Behavior

| Metric         | Value                   |
| -------------- | ----------------------- |
| Train Accuracy | Very High (often ~100%) |
| Test Accuracy  | Lower                   |

---

## 🔹 Why?

Model learns **noise + specific patterns**, not general rules

---

## 🧠 Intuition

> It’s like memorizing past exam questions instead of understanding concepts

---

# 🧠 4. Train vs Test Gap (MOST IMPORTANT)

## 🔹 This is what you MUST focus on

| Case         | Train | Test | Meaning         |
| ------------ | ----- | ---- | --------------- |
| Underfitting | Low   | Low  | Model too weak  |
| Good Fit     | High  | High | Ideal           |
| Overfitting  | High  | Low  | Model memorized |

---

## 🧠 Golden Rule

> **Gap between train and test = sign of overfitting**

---

# ✍️ YOUR TASK - What You Should Actually Do

## Step 1: Train both models

## Step 2: Print results

```python
from sklearn.metrics import accuracy_score

# Train
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)

# Predict
y1_train = model1.predict(X_train)
y1_test = model1.predict(X_test)

y2_train = model2.predict(X_train)
y2_test = model2.predict(X_test)

# Accuracy
print("Underfit Model:")
print("Train:", accuracy_score(y_train, y1_train))
print("Test:", accuracy_score(y_test, y1_test))

print("\nOverfit Model:")
print("Train:", accuracy_score(y_train, y2_train))
print("Test:", accuracy_score(y_test, y2_test))
```

---

# 🧠 WHAT YOU MUST WRITE (IMPORTANT)

Don’t skip this - this is where learning happens.

---

## ✅ Your Observations (write like this)

### 🔹 Underfitting Model

* Train Accuracy: ___
* Test Accuracy: ___
* Conclusion: Model is too simple because __________

---

### 🔹 Overfitting Model

* Train Accuracy: ___
* Test Accuracy: ___
* Conclusion: Model memorized because __________

---

# 🧠 FINAL UNDERSTANDING (LOCK THIS IN)

* Underfitting → model **cannot learn**
* Overfitting → model **learns too much**
* Best model → **balances both**

---
