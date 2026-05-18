# Day 4 - Data Storage Formats

## Overview

In real-world machine learning systems, storing data efficiently is just as important as training models.

Different storage formats affect:

* Storage size
* Read/write speed
* Query performance
* Scalability
* Production workflows

This module focuses on understanding common storage formats used in data engineering and machine learning pipelines.

---

# CSV Limitations

CSV (Comma Separated Values) is simple and widely used, but it has major drawbacks.

### Advantages

* Human readable
* Easy to create
* Supported by almost every tool

### Limitations

* Large file sizes
* Slow loading time
* No schema enforcement
* No compression by default
* Poor performance on large datasets

Example:

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

---

# JSON Usage

JSON is commonly used for:

* APIs
* Nested data
* Configuration files
* Web applications

Example structure:

```json
[
  {
    "name": "Ali",
    "age": 22
  }
]
```

---

## Advantages

* Handles nested structures
* API friendly
* Flexible format

---

## Limitations

* Larger than Parquet
* Slower for analytical workloads
* Less efficient for large datasets

Example:

```python
df.to_json("data.json")
```

---

# Parquet Format

Parquet is a columnar storage format widely used in:

* Big data systems
* Data engineering
* Machine learning pipelines
* Cloud analytics systems

Libraries:

* PyArrow
* FastParquet

Example:

```python
df.to_parquet("data.parquet")
```

---

# Why Parquet is Faster for Analytics

Parquet stores data by columns instead of rows.

### CSV/JSON

```text
Row 1 → all columns
Row 2 → all columns
Row 3 → all columns
```

---

### Parquet

```text
Column A → all values
Column B → all values
Column C → all values
```

This improves:

* Faster column selection
* Better compression
* Faster analytics queries

Example:

If you need only one column:

```python
df["salary"]
```

Parquet reads only that column.

CSV reads everything.

---

# Compression Basics

Compression reduces storage size.

Common compression methods:

* Snappy
* Gzip
* Brotli

Example:

```python
df.to_parquet(
    "data.parquet",
    compression="snappy"
)
```

Benefits:

* Smaller files
* Faster transfer
* Lower storage costs

---

# Practice Task

Save the same dataset in:

* CSV
* JSON
* Parquet

Example:

```python
import pandas as pd

df = pd.read_csv("titanic.csv")

df.to_csv("titanic_output.csv", index=False)
df.to_json("titanic_output.json")
df.to_parquet("titanic_output.parquet")
```

---

# Compare Performance

Measure:

* File size
* Loading speed

---

## File Size Comparison

```python
import os

print(os.path.getsize("titanic_output.csv"))
print(os.path.getsize("titanic_output.json"))
print(os.path.getsize("titanic_output.parquet"))
```

---

## Loading Speed Comparison

```python
import time

start = time.time()
pd.read_csv("titanic_output.csv")
print("CSV:", time.time() - start)

start = time.time()
pd.read_json("titanic_output.json")
print("JSON:", time.time() - start)

start = time.time()
pd.read_parquet("titanic_output.parquet")
print("Parquet:", time.time() - start)
```

---

# Mini Task

Benchmark all three formats and analyze:

* Which file is smallest?
* Which loads fastest?
* Which is best for production systems?

---

# Expected Results

Usually:

| Format  | File Size    | Speed  | Best Use Case          |
| ------- | ------------ | ------ | ---------------------- |
| CSV     | Large        | Slow   | Small datasets         |
| JSON    | Medium/Large | Medium | APIs                   |
| Parquet | Small        | Fast   | Analytics/ML pipelines |

---

# Goal

Understand why modern data systems prefer efficient storage formats like Parquet for large-scale analytics and machine learning workflows.

---

# Outcome

After completing this module, you will understand:

* Storage tradeoffs
* Data engineering basics
* Why Parquet is widely used
* Performance optimization in ML systems

This knowledge becomes very useful in MLOps, big data systems, and production ML pipelines.
