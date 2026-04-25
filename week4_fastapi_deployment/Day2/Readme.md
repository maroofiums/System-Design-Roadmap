# Day 2 - Request Body + Input Validation

## Goal

Learn how to safely receive user input in FastAPI using **POST requests**, **JSON body**, and **Pydantic validation**.

By end of today, your API can accept structured data like a real ML service.

---

# 1. Why GET is Not Enough

Yesterday:

```http
GET /
```

Good for reading data.

But for ML prediction, login forms, registration, user input:

We need to **send data to server**.

That is where **POST** comes in.

---

# 2. What is POST Request?

POST = Send data to server.

Example:

```http
POST /predict
```

With body:

```json
{
  "age": 22,
  "income": 50000
}
```

Meaning:

“Use this data.”

---

# 3. What is Request Body?

Body = hidden data sent inside request.

Unlike URL params, body is cleaner for larger structured data.

Example:

```json
{
  "name": "Maroof",
  "skills": ["Python", "ML"]
}
```

---

# 4. What is Pydantic?

Pydantic is used by FastAPI to:

* Validate input types
* Ensure required fields exist
* Convert data when possible
* Return clean errors automatically

Example:

If age should be integer:

```python
age: int
```

If user sends `"abc"` → error.

---

# 5. Build First Input Model

Create:

```python
from pydantic import BaseModel

class UserInput(BaseModel):
    age: int
    income: float
```

## Meaning:

API expects:

* age must be integer
* income must be number

---

# 6. Full FastAPI Code

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    age: int
    income: float

@app.post("/predict")
def predict(data: UserInput):
    return data
```

---

# 7. How It Works

When user sends:

```json
{
  "age": 21,
  "income": 45000
}
```

FastAPI creates:

```python
data.age
data.income
```

And returns:

```json
{
  "age": 21,
  "income": 45000
}
```

---

# 8. Run Server

```bash
uvicorn main:app --reload
```

---

# 9. Test in Docs

Open:

```text
http://127.0.0.1:8000/docs
```

You’ll see interactive Swagger docs.

Try POST `/predict`

Enter:

```json
{
  "age": 23,
  "income": 80000
}
```

---

# 10. Access Values Inside Function

Update:

```python
@app.post("/predict")
def predict(data: UserInput):
    return {
        "age_received": data.age,
        "income_received": data.income
    }
```

---

# 11. Validation Errors

## Case 1: Wrong Type

Send:

```json
{
  "age": "hello",
  "income": 50000
}
```

Response:

```json
{
  "detail": "validation error"
}
```

(FastAPI gives full structured error)

---

## Case 2: Missing Field

Send:

```json
{
  "age": 20
}
```

Error because `income` missing.

---

# 12. Why This Matters for ML

ML model needs numeric clean input.

Bad input can crash model.

So validation protects system.

Example:

```text
age = "banana"
income = null
```

Should be rejected.

---

# 13. Better Example for ML

```python
@app.post("/predict")
def predict(data: UserInput):
    score = data.age * 100 + data.income * 0.1

    return {
        "prediction": score
    }
```

Now input becomes output logic.

---

# 14. Add More Fields

```python
class UserInput(BaseModel):
    age: int
    income: float
    experience: int
```

Then JSON:

```json
{
  "age": 24,
  "income": 70000,
  "experience": 2
}
```

---

# 15. Folder Structure

```text
project/
 ├── main.py
```

---

# 16. Practice Tasks

## Task 1

Create `/student` route:

```python
name: str
marks: float
```

---

## Task 2

Create `/loan` route:

Input:

```json
{
  "income": 50000,
  "credit_score": 700
}
```

Return same data.

---

## Task 3

Add field:

```python
married: bool
```

Try:

```json
true
false
```

---

# 17. Common Errors

## Error:

```text
NameError: BaseModel
```

Fix:

```python
from pydantic import BaseModel
```

---

## Error:

422 Unprocessable Entity

Means invalid request body.

Usually:

* wrong JSON
* missing field
* wrong type

---

# 18. Outcome Today

You now understand:

* POST requests
* JSON request body
* Pydantic models
* Input validation
* Structured data receiving
* Safe backend design

---

# 19. Real Industry Insight

Every serious backend uses validation.

Without validation:

```text
Users break APIs
Hackers abuse APIs
Models crash
```

With validation:

```text
Clean + professional system
```

---
