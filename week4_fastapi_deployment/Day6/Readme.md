# Day 6 - Testing API

## Goal

Learn how to test your FastAPI application like a real backend developer using **Swagger Docs**, valid requests, invalid requests, and edge cases.

Today is about confidence:

```text 
If you don’t test it,
you don’t know it works.
```

---

# Why Testing Matters

Without testing:

* Hidden bugs remain
* Wrong predictions go unnoticed
* API crashes in production
* Frontend integration fails

With testing:

* Reliable backend
* Cleaner releases
* Easier debugging
* Professional workflow

---

# What You’ll Learn Today

* Swagger Docs
* Manual endpoint testing
* Valid inputs
* Invalid inputs
* Edge case testing
* Developer mindset

---

# 1. Run Your API

```bash
uvicorn main:app --reload
```

---

# 2. Open Swagger Docs

Visit:

```text 
http://127.0.0.1:8000/docs
```

FastAPI automatically gives interactive API docs.

This is one reason FastAPI is loved.

---

# 3. What You’ll See in Docs

* Available routes
* GET endpoints
* POST endpoints
* Request schema
* Response schema
* “Try it out” button

---

# 4. Example Routes

```text id="m3x8nv"
GET /
GET /health
POST /predict
```

---

# 5. Test Valid Input

Open `POST /predict`

Click:

```text 
Try it out
```

Use:

```json id="k2z8vw"
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Click Execute.

Expected response:

```json
{
  "status": "success",
  "prediction_name": "Setosa"
}
```

---

# 6. Test Invalid Input

Use wrong types:

```json 
{
  "sepal_length": "hello",
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Expected:

```json
422 Validation Error
```

Good sign — validation works.

---

# 7. Test Missing Field

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5
}
```

Expected:

```json
field required
```

---

# 8. Test Edge Cases

Edge cases = unusual but possible inputs.

## Example 1

Very large values:

```json 
{
  "sepal_length": 100,
  "sepal_width": 50,
  "petal_length": 80,
  "petal_width": 20
}
```

---

## Example 2

Very small positive values:

```json 
{
  "sepal_length": 0.1,
  "sepal_width": 0.1,
  "petal_length": 0.1,
  "petal_width": 0.1
}
```

---

## Example 3

Negative values (should fail if validation added)

```json 
{
  "sepal_length": -5,
  "sepal_width": 3,
  "petal_length": 1,
  "petal_width": 0.2
}
```

---

# 9. Test GET Routes

## Home Route

```text 
GET /
```

Expected:

```json 
{
  "status": "success"
}
```

---

## Health Route

```text 
GET /health
```

Expected:

```json
{
  "service": "healthy"
}
```

---

# 10. Learn Response Codes

## Common Codes

```text 
200 = Success
201 = Created
400 = Bad Request
404 = Not Found
422 = Validation Error
500 = Server Error
```

Important for backend interviews.

---

# 11. Real Developer Testing Checklist

```text 
✔ Correct data works
✔ Wrong data blocked
✔ Missing data blocked
✔ Routes reachable
✔ Responses clean
✔ No crashes
```

---

# 12. Bonus: Test with Python requests

```python
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

res = requests.post(url, json=data)

print(res.json())
```

---

# 13. Why Swagger Is Powerful

Instead of manually building frontend first:

```text
You can test backend instantly.
```

That speeds development massively.

---

# 14. Common Mistakes

## API not running

```text 
Connection refused
```

Fix:

```bash 
uvicorn main:app --reload
```

---

## Wrong Port

Use correct URL:

```text 
127.0.0.1:8000/docs
```

---

## JSON Syntax Error

Missing commas or quotes.

---

# 15. Outcome Today

You now know how to test APIs like a real developer.

You can verify:

* Functionality
* Validation
* Stability
* Readiness for frontend use
