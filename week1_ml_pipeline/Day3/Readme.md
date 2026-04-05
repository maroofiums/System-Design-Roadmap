# DAY 3 - ENCODING CATEGORICAL DATA

## Goal

Convert text (categories) into numbers so ML models can understand them.

---

# 1. WHY ENCODING IS REQUIRED

## Key idea:

Machine Learning models only understand numbers.

But real data looks like:

* "Male", "Female"
* "Pakistan", "India"
* "Yes", "No"

---

## Problem:

If you pass text directly:

> Model will fail or give incorrect results

---

# 2. TYPES OF DATA

## Numerical Data

* Age = 25
* Salary = 50000

## Categorical Data

* Gender = Male/Female
* City = Karachi/Lahore

---

# 3. LABEL ENCODING

## What?

Converts categories into numbers

Example:

* Male → 0
* Female → 1

---

## When to use:

* Binary data (Yes/No)
* Ordinal data (Low < Medium < High)

---

## Code:

```python id="label_enc_01"
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["gender"] = le.fit_transform(df["gender"])
```

---

## Example:

| Gender | Encoded |
| ------ | ------- |
| Male   | 1       |
| Female | 0       |

---

## Important Warning:

Label encoding may introduce fake order:

* Karachi = 0
* Lahore = 1
* Islamabad = 2 ❌ (this order is meaningless)

---

# 4. ONE-HOT ENCODING

## What?

Creates separate column for each category

---

## Example:

City column:

| City    |
| ------- |
| Karachi |
| Lahore  |

Becomes:

| Karachi | Lahore |
| ------- | ------ |
| 1       | 0      |
| 0       | 1      |

---

## When to use:

* Nominal data (no order)
* Cities, countries, colors

---

## Code:

```python id="onehot_01"
df = pd.get_dummies(df, columns=["city"])
```

---

# 5. LABEL vs ONE-HOT

| Type             | When               | Risk                       |
| ---------------- | ------------------ | -------------------------- |
| Label Encoding   | Binary / ordinal   | May create fake order      |
| One-Hot Encoding | Nominal categories | Safe but increases columns |

---

# 6. PRACTICAL TASK FLOW

---

## Step 1 - Identify categorical columns

```python id="cat_cols"
df.select_dtypes(include="object").columns
```

---

## Step 2 - Apply encoding

### Binary columns → Label Encoding

```python id="label_apply"
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df["gender"] = le.fit_transform(df["gender"])
```

---

### Multi-category columns → One-Hot

```python id="onehot_apply"
df = pd.get_dummies(df, columns=["city"])
```

---

# 7. OUTPUT OF DAY 3

By end of today:

✔ No text columns left
✔ All data converted into numbers
✔ Dataset ready for scaling + ML models

---

# 8. COMMON MISTAKES

* Using Label Encoding for cities/countries ❌
* Forgetting to encode target if needed
* Not checking new columns after One-Hot

---

# 9. MINDSET

Today’s key idea:

> “ML models don’t understand words - only patterns in numbers”

Encoding is the bridge between real world and machine learning.

---
