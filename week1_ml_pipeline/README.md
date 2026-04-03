# WEEK 1 - ML PIPELINE BASICS

## Goal

Understand end-to-end ML workflow:
Data → Features → Model → Evaluation

---

# DAY 1 - Dataset Understanding + Setup

## Concepts

* What is a dataset?
* Rows vs columns
* Features vs target (label)
* Problem framing (classification vs regression)

## Tasks

* Load dataset (Pandas)
* Inspect data:

  * `.head()`
  * `.info()`
  * `.describe()`
* Identify:

  * Target column
  * Feature columns

## Output

* Basic understanding of dataset structure

---

# DAY 2 - Data Cleaning (Core Step)

## Concepts

* Missing values
* Outliers (basic idea)
* Data consistency

## Tasks

* Handle missing values:

  * drop OR fill (mean/median)
* Check duplicates
* Basic cleaning

## Output

* Cleaned dataset ready for ML

---

# DAY 3 - Encoding Categorical Data

## Concepts

* Machine learning only understands numbers
* Label Encoding vs One-Hot Encoding

## Tasks

* Convert categorical columns:

  * Label Encoding (binary / ordinal)
  * One-hot Encoding (nominal)

## Output

* Fully numeric dataset

---

# DAY 4 - Feature Scaling

## Concepts

* Why scaling is needed
* Different ranges affect model performance

## Methods

* Standardization (Z-score)
* Normalization (Min-Max)

## Tasks

* Apply scaling on numerical features
* Keep target unchanged

## Output

* Scaled dataset

---

# DAY 5 - Train/Test Split

## Concepts

* Why we split data
* Overfitting vs generalization

## Ratio

* 80% train / 20% test (common)

## Tasks

* Split dataset using `train_test_split`
* Separate:

  * X_train, X_test
  * y_train, y_test

## Output

* Ready-to-train datasets

---

# DAY 6 - Model Training

## Concepts

* How ML learns patterns
* Basic models:

  * Linear Regression
  * Logistic Regression
  * Decision Tree

## Tasks

* Train at least 2 models
* Fit on training data
* Predict on test data

## Output

* Trained ML model(s)

---

# DAY 7 - Evaluation + Save Model

## Concepts

* How we measure performance

### Metrics:

* Accuracy (classification)
* Precision / Recall (basic idea)
* RMSE (regression)

## Tasks

* Evaluate model
* Compare models
* Select best model
* Save model using `.pkl`

## Output

* Final trained model saved

---

# FINAL WEEK 1 PROJECT

## Loan Prediction System (Local ML Project)

### Includes:

* Clean dataset
* Feature engineering basics
* Trained ML model
* Evaluation report
* Saved `.pkl` file

---

# END RESULT OF WEEK 1

After this week, you will understand:

* Full ML workflow
* Data preprocessing pipeline
* Model training process
* Basic evaluation logic

---