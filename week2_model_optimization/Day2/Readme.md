# DAY 2 - Bias vs Variance

## 1. Core Intuition

Think of a model like a student.

* **Bias = “Dumb model”**

  * Makes strong assumptions
  * Doesn’t learn enough from data
  * Same mistake again and again

* **Variance = “Unstable model”**

  * Learns too much from training data
  * Gets confused when data changes slightly
  * Predictions change a lot

---

## 2. Why High Bias = Underfitting

**In your own words:**

High bias means the model is too simple to capture patterns in data.

* It assumes things like “relationship is linear” even if it’s not
* It ignores important patterns
* So it performs poorly on:

  * training data
  * test data

That is exactly **underfitting**.

**Simple example:**
Trying to fit a straight line on curved data.

---

## 3. Why High Variance = Overfitting

**In your own words:**

High variance means the model is too sensitive to training data.

* It memorizes noise and small details
* Slight change in data → completely different predictions
* So:

  * training accuracy = very high
  * test accuracy = low

That is **overfitting**.

**Simple example:**
A very deep decision tree memorizing every data point.

---

## 4. Interview-Level Summary

You can say this directly:

* High bias causes underfitting because the model is too simple and cannot capture the true pattern.
* High variance causes overfitting because the model is too sensitive to training data and fails to generalize.

---

## 5. Mini Experiment (Important)

We will simulate exactly what you were asked:

* Train same model on:

  * small dataset
  * slightly changed dataset
* Observe prediction difference

---

## 6. Code Example

### Setup

```python
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
```

---

### Create Dataset

```python
# Original dataset
X1 = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y1 = np.array([2, 4, 6, 8, 10])  # perfect linear

# Slightly modified dataset
X2 = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y2 = np.array([2, 5, 5, 9, 11])  # noise added
```

---

### Train Model on Dataset 1

```python
model1 = LinearRegression()
model1.fit(X1, y1)

pred1 = model1.predict(X1)
```

---

### Train Model on Dataset 2

```python
model2 = LinearRegression()
model2.fit(X2, y2)

pred2 = model2.predict(X2)
```

---

### Compare Predictions

```python
print("Model 1 Predictions:", pred1)
print("Model 2 Predictions:", pred2)
```

---

### Visualization

```python
plt.scatter(X1, y1, label="Dataset 1")
plt.plot(X1, pred1, label="Model 1")

plt.scatter(X2, y2, label="Dataset 2")
plt.plot(X2, pred2, linestyle='dashed', label="Model 2")

plt.legend()
plt.show()
```

---

## 7. What You Should Observe

* If model changes **a lot** → high variance
* If model fails to fit both → high bias

---

## 8. Extra: High Variance Demonstration (Better)

Use a more complex model:

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# High variance model
model = make_pipeline(PolynomialFeatures(degree=5), LinearRegression())

model.fit(X1, y1)
pred_high_var = model.predict(X1)
```

Now:

* Even small noise will change curve a lot
* That is **overfitting behavior**

---

## 9. Final Mental Model

Always think like this:

* If model is wrong in same way → **Bias problem**
* If model changes wildly → **Variance problem**

Or your line:

> “Is my model dumb or unstable?”

---

## 10. Clean Written Answer (Use This)

High bias occurs when a model is too simple and makes strong assumptions about the data, preventing it from learning the true underlying pattern. As a result, it performs poorly on both training and test data, which is known as underfitting.

High variance occurs when a model is too complex and learns not only the underlying pattern but also noise in the training data. This makes the model highly sensitive to small changes in data, leading to very good performance on training data but poor generalization to new data, which is known as overfitting.

---