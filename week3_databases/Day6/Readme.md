# 📦 Day6 - Iris ML Pipeline (SQLite + Machine Learning + Model Export)

## 🧠 Overview

This project demonstrates a complete **end-to-end Machine Learning pipeline** using:

* Dataset ingestion (Iris dataset from Scikit-learn)
* Data storage in SQLite database
* SQL-based data retrieval
* Machine Learning model training
* Model evaluation
* Saving trained model as `.pkl`

It simulates a **real-world ML workflow used in production systems**, where data is not loaded from CSV files but from databases.

---

# 📁 Project Structure

```text id="proj1"
📦Day6
 ┣ 📂Database
 ┃ ┗ 📜iris.db
 ┣ 📂Model
 ┃ ┗ 📜model.pkl
 ┣ 📂Python
 ┃ ┣ 📜data_setup.py
 ┃ ┗ 📜train.py
 ┣ 📜Readme.md
 ┗ 📜requirements.txt
```

---

# ⚙️ Tech Stack

* Python 3.x
* SQLite (Database)
* Pandas (Data handling)
* Scikit-learn (ML model)
* Pickle (Model serialization)

---

# 🚀 Project Workflow

## 🔹 Step 1: Data Ingestion

File: `Python/data_setup.py`

### What it does:

* Loads Iris dataset from `sklearn.datasets`
* Converts dataset into a Pandas DataFrame
* Creates SQLite database (`iris.db`)
* Stores data into a structured table

---

## 🔹 Step 2: Model Training

File: `Python/train.py`

### What it does:

* Connects to SQLite database
* Retrieves data using SQL query
* Splits data into training and testing sets
* Trains a Machine Learning model (Random Forest)
* Evaluates model performance
* Saves trained model as `.pkl`

---

# ▶️ How to Run the Project

## 1️⃣ Install Dependencies

```bash id="run1"
pip install -r requirements.txt
```

---

## 2️⃣ Create Database & Insert Data

```bash id="run2"
python Python/data_setup.py
```

---

## 3️⃣ Train Model & Save It

```bash id="run3"
python Python/train.py
```

---

# 💾 Output Files

After execution, the following files are generated:

## 📂 Database

```
Database/iris.db
```

Contains structured Iris dataset stored in SQLite format.

---

## 📂 Model

```
Model/model.pkl
```

Serialized trained machine learning model.

---

# 🧠 Key Learning Outcomes

After completing this project, you will understand:

### 📊 Data Engineering

* How datasets are stored in SQL databases
* How to structure ML-ready tables

### 🧾 SQL for ML

* Querying datasets using SELECT
* Filtering and retrieving training data

### 🤖 Machine Learning Pipeline

* End-to-end training workflow
* Train/test splitting
* Model evaluation

### 💾 Model Deployment Basics

* Saving models using pickle
* Reusing trained models later

---

# 🔥 Real-World Connection

This project replicates how real ML systems work:

```text id="flow1"
Database → SQL Query → DataFrame → ML Model → Saved Artifact (.pkl)
```

Used in:

* Fraud detection systems
* Recommendation engines
* Customer analytics pipelines
* Production ML APIs

---

# 📈 Model Details

* Algorithm: RandomForestClassifier
* Dataset: Iris dataset (3 classes)
* Features: 4 numeric features
* Output: Multi-class classification

---

# 🧪 Example Output

```text id="out1"
Accuracy: 0.96
Model saved as model.pkl
```

---
