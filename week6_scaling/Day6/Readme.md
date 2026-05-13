# Day 6 - Database Sharding

## Goal

Understand how massive systems scale databases horizontally by splitting data across multiple servers.

---

## What is Sharding?

Sharding is a database scaling technique where large datasets are divided into smaller pieces called **shards**.

Each shard stores a subset of the total data.

Instead of one huge database:

```text
All Users → One Database (slow)
```

We distribute data:

```text
Users A-M → DB1
Users N-Z → DB2
```

This improves scalability and performance.

---

## Why Sharding is Needed

As applications grow:

* Database size increases
* Query latency increases
* Single server storage becomes limited
* High traffic overloads one database server

Sharding solves this by distributing data across multiple databases.

---

## Database Partitioning

Sharding is a form of **horizontal partitioning**.

Instead of adding more CPU/RAM to one database:

```text
Vertical Scaling → Bigger database server
```

We split the data:

```text
Horizontal Scaling → Multiple database servers
```

---

## Shard Keys

A shard key determines how data is distributed.

Examples:

* User ID
* Geographic region
* First letter of username
* Customer ID

Example:

```text
User IDs 1–1M → Shard 1
User IDs 1M–2M → Shard 2
```

---

## Example Strategies

### Alphabet-based Sharding

```text
Users A-M → DB1
Users N-Z → DB2
```

Simple but may create uneven distribution.

---

### Region-based Sharding

```text
Asia Users → DB1
Europe Users → DB2
US Users → DB3
```

Useful for global applications.

---

### ID-based Sharding

```text
User ID % 3
```

Example:

* User 1 → DB1
* User 2 → DB2
* User 3 → DB3

This often creates better balance.

---

## Challenges of Sharding

* Complex queries across shards
* Rebalancing data
* Choosing bad shard keys
* Increased infrastructure complexity

---

## Real-World Example

Large platforms like entity["company", "Facebook", "social media company"] and entity["company", "Amazon", "e-commerce company"] use database sharding to manage massive user datasets.

---

## ML System Example

For a large ML platform:

```text
Prediction Data:

Users 1–1M → Shard 1
Users 1M–2M → Shard 2
Users 2M–3M → Shard 3
```

This prevents a single database from becoming overloaded.

---

## Task

Design a sharding strategy for your users table.

Think about:

* Which shard key will you use?
* How will data be distributed?
* What happens when users grow rapidly?

Create your own architecture diagram.

Example:

```text
Users
  ↓
API Server
  ↓
Shard Router
 ↓   ↓   ↓
DB1 DB2 DB3
```

---

## Outcome

After this day you should understand:

* What sharding is
* Horizontal database scaling
* How shard keys work
* Challenges of distributed databases

---
