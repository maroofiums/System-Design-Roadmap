# Day 2 - Retraining Pipeline (ML Automation)

## Overview

In Day 2, we build a complete **machine learning retraining pipeline** using Scikit-learn.
The goal is to structure ML code into modular components and prepare for automation (scheduling + CI/CD in upcoming days).

---

## Objective

By the end of this day, you will:

* Build a modular ML project structure
* Load dataset (Iris)
* Train a model (RandomForestClassifier)
* Evaluate performance
* Save trained model
* Run pipeline from a single entry point

---

## Project Structure

```text
Day2/
│
├── pipeline/
│   └── retrain.py
│
├── src/
│   ├── data_loader.py
│   ├── trainer.py
│   ├── evaluator.py
│   └── model_saver.py
│
└── models/
    └── iris_model.pkl
```

---

## Pipeline Flow

```text
Data Loading
    ↓
Train/Test Split
    ↓
Model Training
    ↓
Evaluation
    ↓
Model Saving
```

---

## Tech Stack

* Python
* Scikit-learn
* Pandas
* Joblib

---

## Core Components

### 1. Data Loader (`src/data_loader.py`)

Loads Iris dataset and splits into train/test sets.

### 2. Trainer (`src/trainer.py`)

Trains a RandomForest model.

### 3. Evaluator (`src/evaluator.py`)

Computes:

* Accuracy
* Precision
* Recall
* F1-score

### 4. Model Saver (`src/model_saver.py`)

Saves trained model using `joblib`.

---

## Main Pipeline (`pipeline/retrain.py`)

Single entry point that:

* Calls all modules
* Runs training pipeline
* Prints evaluation metrics
* Saves model if performance is good

---

## How to Run

From `Day2/` directory:

```bash
python -m pipeline.retrain
```

---

## Key Learning

* How to modularize ML code
* Separation of concerns in ML systems
* Building reusable ML pipelines
* Preparing for automation 

---
