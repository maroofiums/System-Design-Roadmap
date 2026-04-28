# Day 5 - Error Handling + Clean Responses

## Goal

Make your ML API **professional**, safe, and production-ready by handling errors gracefully and returning clean structured responses.

Today separates:

```text id="2i8t3y"
Beginner API ❌
Professional API ✅
```

---

# Why Error Handling Matters

Without handling:

* App crashes
* Ugly Python traceback
* Confusing errors
* Bad user experience

With handling:

* Clean messages
* Stable API
* Easy debugging
* Better trust

---

# What You’ll Learn Today

* `try / except`
* Invalid input handling
* Missing values
* Response formatting
* Consistent JSON outputs

---

# Bad API Example

```json id="f3lq2o"
500 Internal Server Error
```

User learns nothing.

---

# Good API Example

```json id="s7f2dp"
{
  "status": "error",
  "message": "Invalid numeric input"
}
```

---

# Project Structure

```text id="3g0j9k"
Day5/
┣ app/
┃ ┣ iris_model.pkl
┃ ┗ main.py
┗ Readme.md
```

---

# Full Professional Code

```python id="l7m1pa"
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("iris_model.pkl")

flower_names = ["Setosa", "Versicolor", "Virginica"]

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "API Running"
    }

@app.post("/predict")
def predict(data: IrisInput):
    try:
        features = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]]

        pred = model.predict(features)[0]

        return {
            "status": "success",
            "prediction_class": int(pred),
            "prediction_name": flower_names[pred]
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
```

---

# 1. try / except Explained

## Syntax

```python id="y4m8qp"
try:
    risky_code()
except Exception as e:
    handle_error()
```

Meaning:

* Try normal code
* If error happens, don’t crash
* Return safe response

---

# 2. Clean Success Response

```json id="3fpl5t"
{
  "status": "success",
  "prediction_name": "Setosa"
}
```

Easy for frontend apps.

---

# 3. Clean Error Response

```json id="3s6vup"
{
  "status": "error",
  "message": "Something went wrong"
}
```

---

# 4. Why Response Format Matters

Frontend developers love consistency.

Always return:

```text id="2kwv63"
status
data OR message
```

Then frontend logic becomes simple.

---

# 5. Invalid Input Handling

If user sends:

```json id="a2f9x8"
{
  "sepal_length": "abc"
}
```

FastAPI + Pydantic automatically returns validation error.

This protects API before function runs.

---

# 6. Missing Values

If request misses field:

```json id="db7a2j"
{
  "sepal_length": 5.1
}
```

FastAPI returns:

```json id="h9j5cp"
{
  "detail": "field required"
}
```

---

# 7. Better Custom Validation

```python id="tw7kpi"
from pydantic import BaseModel, Field

class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)
```

Meaning values must be greater than zero.

---

# 8. Add Health Route

```python id="eq1w5v"
@app.get("/health")
def health():
    return {
        "status": "success",
        "service": "healthy"
    }
```

---

# 9. Add Timestamp (Professional)

```python id="qs0m1u"
from datetime import datetime
```

Return:

```json id="l1g7ae"
{
  "status": "success",
  "time": "2026-04-28"
}
```

---

# 10. Common Production Pattern

```json id="k0v7oe"
{
  "status": "success",
  "data": {...}
}
```

or

```json id="a9o2he"
{
  "status": "error",
  "message": "Invalid request"
}
```

---

# 11. Example Final Predict Response

```json id="x1v4zo"
{
  "status": "success",
  "prediction_class": 2,
  "prediction_name": "Virginica"
}
```

---

# 12. Test Cases

## Valid Request

Should predict.

## Wrong Type

```json id="x4i8fd"
{
  "sepal_length": "hello"
}
```

Should fail.

## Negative Values

```json id="p7j1s2"
{
  "sepal_length": -2
}
```

Should fail.

---

# 13. Common Mistake

Returning raw Python error in production.

Bad:

```json id="z8d1qw"
{
  "message": "index out of range..."
}
```

Better:

```json id="m2w6ri"
{
  "status": "error",
  "message": "Prediction failed"
}
```

(Log detailed error internally)

---

# 14. Skills You Gain Today

* Defensive coding
* Stable APIs
* User-friendly responses
* Validation mindset
* Production backend habits

---

# 15. Outcome Today

You now have:

```text id="j5x2rl"
Professional API Structure
```

Instead of demo-only project.

---