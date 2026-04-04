# DAY 2 - DATA CLEANING

## Goal

Make raw data usable for machine learning

---

# 1. WHY DATA CLEANING IS IMPORTANT

Real-world data is always messy:

* Missing values
* Wrong values
* Duplicate records

If you don’t clean:

> Model learns garbage → gives wrong predictions

---

# 2. MISSING VALUES

## What?

Some cells in dataset are empty (NaN)

Example:

* Age = missing
* Salary = missing

---

## Why problem?

* Models cannot handle missing values directly
* Leads to incorrect learning

---

## How to detect

```python
df.isnull().sum()
```

---

## Handling Methods

### 1. Drop Missing Values

```python
df = df.dropna()
```

### When to use:

* Few missing rows
* Dataset is large

---

### 2. Fill Missing Values

#### Mean (for numerical)

```python
df["age"] = df["age"].fillna(df["age"].mean())
```

#### Median (better for outliers)

```python
df["income"] = df["income"].fillna(df["income"].median())
```

#### Mode (for categorical)

```python
df["city"] = df["city"].fillna(df["city"].mode()[0])
```

---

## Important Insight

* Mean → sensitive to outliers
* Median → more robust

---

# 3. OUTLIERS (Basic Idea)

## What?

Extreme values

Example:

* Salary = 1,000,000 (others ~50,000)

---

## Why problem?

* Skews model learning
* Affects mean and scaling

---

## Detect (simple way)

```python
df.describe()
```

Look for:

* Very large max values
* Large difference between mean & median

---

## Basic Handling

### Option 1 - Remove

```python
df = df[df["salary"] < 200000]
```

### Option 2 - Cap values

```python
df["salary"] = df["salary"].clip(upper=200000)
```

---

# 4. DATA CONSISTENCY

## What?

Data should be uniform

---

## Common Problems:

* “Male”, “male”, “M” → same meaning
* Extra spaces
* Mixed formats

---

## Fixing

```python
df["gender"] = df["gender"].str.lower().str.strip()
```

---

# 5. DUPLICATES

## What?

Same row repeated

---

## Why problem?

* Bias in training
* Wrong patterns

---

## Detect

```python
df.duplicated().sum()
```

---

## Remove

```python
df = df.drop_duplicates()
```

---

# 6. BASIC CLEANING PIPELINE (IMPORTANT)

This is your Day 2 flow:

```python
# Missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fix consistency
df.columns = df.columns.str.strip().str.lower()
```

---

# 7. OUTPUT OF DAY 2

By end of today:

✔ No missing values
✔ No duplicate rows
✔ Clean, consistent dataset
✔ Outliers handled (basic level)

---

# 8. COMMON BEGINNER MISTAKES

* Dropping too much data
* Ignoring outliers
* Filling categorical with mean (wrong)
* Not checking duplicates

---

# 9. MINDSET

Today you are learning:

> “Data is more important than model”

Good cleaning = better accuracy without changing model

---
