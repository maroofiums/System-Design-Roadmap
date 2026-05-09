# Day 2 - Load Balancing

## Goal

Understand how incoming traffic is distributed across multiple servers to improve reliability, performance, and scalability.

---

## What is a Load Balancer?

A Load Balancer is a system that distributes incoming network traffic across multiple backend servers.

Its main purpose is to:

* Prevent any single server from being overloaded
* Improve system availability
* Increase performance and reliability

### Simple Idea

Instead of one server handling everything:

```text
Users → One Server (overloaded)
```

We distribute traffic:

```text
Users → Load Balancer → Multiple Servers
```

---

## Why Load Balancing is Needed

Without a load balancer:

* One server can crash under heavy traffic
* Response times increase
* System becomes unreliable

With a load balancer:

* Traffic is shared
* System becomes fault-tolerant
* Better resource utilization

---

## Traffic Distribution Strategies

### 1. Round Robin

Requests are distributed sequentially across servers.

```text
Request 1 → Server A
Request 2 → Server B
Request 3 → Server C
Request 4 → Server A
```

### Use case:

* When all servers have similar capacity
* Simple and fair distribution

---

### 2. Least Connections

Traffic is sent to the server with the fewest active connections.

```text
Server A → 10 connections
Server B → 5 connections  ← selected
Server C → 8 connections
```

### Use case:

* When request durations vary
* More efficient for real-time systems

---

### 3. IP Hash

Client IP is used to determine which server handles the request.

```text
User IP → Hash Function → Server Selection
```

### Use case:

* Session consistency
* When user must always hit the same server

---

## System Architecture

Basic scalable system with load balancing:

```text
Users
   ↓
Load Balancer
   ↓   ↓   ↓
API Server 1
API Server 2
API Server 3
```

---

## Real-World Examples

Load balancing is used in large-scale systems such as:

* Web applications
* ML inference APIs
* Streaming platforms

Examples:

* High-traffic APIs
* SaaS products
* Social media platforms

---

## Task

### 1. Run Multiple FastAPI Instances

Start multiple servers locally:

```bash
uvicorn app:app --port 8000
uvicorn app:app --port 8001
uvicorn app:app --port 8002
```

---

### 2. Simulate Load Distribution

Try sending requests manually (Postman or browser):

* Observe how traffic could be split
* Understand how a real load balancer would distribute requests

---

### 3. Think Critically

Answer these:

* What happens if one server goes down?
* How would load balancing improve your ML API?
* Which strategy fits your system best?

---

## Outcome

After this day you should understand:

* What load balancing is
* How traffic is distributed
* Why multiple servers are needed
* Basic system architecture for scalable APIs

---