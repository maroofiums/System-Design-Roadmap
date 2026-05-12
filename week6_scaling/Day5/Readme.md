# Day 5 - Database Replication

## Goal

Understand how large-scale systems handle increasing read traffic by distributing database workloads using replication.

---

## What is Database Replication?

Database replication is the process of copying data from one database server to one or more replica servers.

This helps distribute load and improve availability.

---

## Primary Database (Write Operations)

The primary database handles:

* INSERT
* UPDATE
* DELETE

Example:

```text
App → Primary DB → Write Data
```

The primary database is responsible for maintaining the latest version of data.

---

## Replica Database (Read Operations)

Replica databases handle:

* SELECT queries
* Read-heavy workloads

Example:

```text
App → Replica DB → Read Data
```

This reduces pressure on the primary database.

---

## Architecture

```text
                Write Requests
App ------------------------> Primary DB
                                |
                                |
                          Replication
                                |
                                v
                        Replica DB 1
                        Replica DB 2
                        Replica DB 3

                Read Requests
App <------------------------ Replica Databases
```

---

## Why Replication is Needed

Without replication:

* Primary DB handles all reads and writes
* Database becomes overloaded
* Slower application performance

With replication:

* Reads are distributed
* Faster query performance
* Better scalability

---

## Read-Heavy Systems

Replication is commonly used when applications receive far more reads than writes.

Examples:

* Social media feeds
* E-commerce product pages
* Analytics dashboards
* Streaming platforms

Most users read far more than they write.

---

## Eventual Consistency

Replication is not always instant.

There may be a delay between:

```text
Write → Primary DB
      ↓
Replica receives update later
```

This delay is called replication lag.

Users may temporarily see slightly outdated data.

---

## Advantages

* Better read scalability
* Reduced primary DB load
* Higher availability
* Improved performance

---

## Challenges

* Replication lag
* Eventual consistency issues
* More infrastructure complexity

---

## Real-World ML Example

In an ML application:

Primary DB:

* Store user predictions
* Save training logs

Replica DB:

* Fetch analytics dashboards
* View prediction history

This prevents heavy reads from slowing down writes.

---

## Task

### Draw Your Own System Design

Create a diagram for your ML API:

```text
Users
  ↓
FastAPI
  ↓
Primary DB (writes)
  ↓
Replica DBs (reads)
```

Think about:

* What operations are reads?
* What operations are writes?
* Where replication helps your system?

---

## Outcome

After this day you should understand:

* What database replication is
* Difference between primary and replica databases
* Why read-heavy systems need replication
* Eventual consistency challenges

---