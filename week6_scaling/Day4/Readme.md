# Day 4 - Database Optimization

## Goal

Understand how database performance becomes a bottleneck in scalable systems and how to optimize queries and structure for high performance APIs.

---

## Database Bottlenecks

A database becomes a bottleneck when it cannot handle the volume of:

* Reads (SELECT queries)
* Writes (INSERT/UPDATE queries)
* Concurrent connections

### Common causes

* Poor indexing
* Inefficient queries
* Fetching unnecessary data
* High number of connections

---

## Indexing

Indexing improves the speed of data retrieval by allowing the database to find rows faster without scanning the entire table.

### Example

```sql
CREATE INDEX idx_email ON users(email);
```

### Why it works

Instead of scanning every row:

* Database uses index structure (like a lookup table)

### Trade-off

* Faster reads
* Slightly slower writes (because index must also be updated)

---

## Query Optimization

Poor queries can severely impact performance.

### Bad Example

```sql
SELECT * FROM users;
```

### Better Example

```sql
SELECT id, name, email FROM users;
```

### Best Practices

* Select only required columns
* Avoid unnecessary joins
* Filter data early using WHERE clause
* Use LIMIT when possible

---

## Connection Pooling

Connection pooling reuses existing database connections instead of creating a new connection for every request.

### Why it matters

* Creating DB connections is expensive
* Too many connections can crash the database

### Concept

```text
App → Connection Pool → Database
```

Instead of:

```text
App → New Connection → Database (every request)
```

---

## How Databases Fail Under Load

As traffic increases:

* Query latency increases
* Connections get exhausted
* CPU usage spikes
* System slows down

---

## Real-World Impact on ML APIs

In ML systems:

* Each prediction may store logs in DB
* High traffic = massive DB load

If not optimized:

* API response time increases
* ML system becomes unreliable

---

## Task

### 1. Optimize Queries

* Identify slow queries in your application
* Reduce unnecessary data fetching

---

### 2. Avoid SELECT *

Replace:

```sql
SELECT * FROM predictions;
```

With:

```sql
SELECT id, input, result FROM predictions;
```

---

### 3. Add Indexes

Identify frequently queried columns:

* email
* user_id
* created_at

Add indexes where needed.

---

## Outcome

After this day you should understand:

* Why databases become bottlenecks
* How indexing improves performance
* How to write efficient queries
* Why connection pooling is important

---