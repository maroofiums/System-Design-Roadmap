# Week 7 - Data Pipelines

## Goal

Build real-world ML data systems that can take raw data → process it → store it efficiently → feed it into a model.

By the end of this week, you'll build a **Pipeline System** that includes preprocessing + model integration.

---

# Day 1 - Feature Engineering Fundamentals

## Learn

* What is feature engineering?
* Why raw data is rarely model-ready
* Numerical features

  * Scaling
  * Normalization
  * Standardization
* Categorical features

  * Label Encoding
  * One Hot Encoding
* Handling missing values
* Feature selection basics

## Practice

* Use a dataset from Kaggle/UCI
* Identify numerical + categorical columns
* Apply preprocessing manually using Pandas + Scikit-learn

## Mini Task

Create a preprocessing notebook where:

* Missing values are handled
* Categories are encoded
* Features are scaled

## Goal

Understand how raw features become useful model inputs.

---

# Day 2 - Advanced Feature Engineering

## Learn

* Date-time feature extraction
* Text feature basics
* Binning
* Log transformation
* Outlier handling
* Polynomial features

## Practice

Take a messy dataset and engineer at least:

* Date features
* Text length/count features
* Outlier removal

## Mini Task

Compare model accuracy before vs after feature engineering.

## Goal

Learn how better features improve performance.

---

# Day 3 - Building Data Pipelines

## Learn

* What is an ML pipeline?
* Why pipelines matter in production
* `Pipeline` in Scikit-learn
* `ColumnTransformer`
* Preventing data leakage

## Practice

Build:

* Preprocessing pipeline
* Model pipeline

Example flow:
Raw Data → Cleaning → Feature Engineering → Model → Prediction

## Mini Task

Train one model entirely through pipeline architecture.

## Goal

Automate preprocessing workflow.

---

# Day 4 - Data Storage Formats

## Learn

* CSV limitations
* JSON usage
* Parquet format
* Why Parquet is faster for analytics
* Compression basics

## Practice

Save same dataset in:

* CSV
* JSON
* Parquet

Compare:

* File size
* Loading speed

## Mini Task

Benchmark storage formats.

## Goal

Understand efficient storage systems.

---

# Day 5 - Feature Store Basics

## Learn

* What is a feature store?
* Offline vs online features
* Why companies use feature stores
* Basic tools:

  * Feast
  * Tecton

## Practice

Simulate feature storage:

* Save processed features
* Reuse them later for training

## Mini Task

Create reusable feature dataset.

## Goal

Understand production feature reuse.

---

# Day 6 - Final Project: Pipeline System

## Build

Create an end-to-end pipeline:

### Step 1

Load raw dataset

### Step 2

Preprocess data

### Step 3

Engineer features

### Step 4

Train model

### Step 5

Save model

### Step 6

Save processed dataset in Parquet

### Step 7

Predict on new data

Tools:

* Pandas
* Scikit-learn
* Joblib
* PyArrow

## Goal

Build a production-style ML workflow.

---

# Day 7 - Test + Review Day

## Test Yourself

Build pipeline from scratch without notes:

* Load dataset
* Clean data
* Engineer features
* Train model
* Save artifacts

## Review Questions

* Why use pipelines?
* Why Parquet over CSV?
* What causes data leakage?
* What is a feature store?

## Portfolio Task

Push project to GitHub with:

* README
* Architecture diagram
* Results

## Goal

Ensure you can independently build data pipelines.

---

# End Result of Week 7

You’ll be able to build systems similar to what real ML engineers use:

Raw Data → Features → Storage → Training → Deployment Preparation

This directly prepares you for:

* MLOps
* Production ML
* Recommendation systems
* Large-scale ML infrastructure
