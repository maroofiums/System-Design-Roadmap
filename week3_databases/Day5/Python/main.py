import sqlite3

conn = sqlite3.connect("ml_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount REAL
)
""")

conn.commit()

cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'Ali')")
cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'Sara')")

cursor.execute("INSERT OR IGNORE INTO orders VALUES (101, 1, 500)")
cursor.execute("INSERT OR IGNORE INTO orders VALUES (102, 2, 900)")
cursor.execute("INSERT OR IGNORE INTO orders VALUES (103, 1, 200)")

conn.commit()

print("\n--- INNER JOIN RESULT ---")

cursor.execute("""
SELECT users.name, orders.amount
FROM users
INNER JOIN orders
ON users.user_id = orders.user_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

print("\n--- LEFT JOIN RESULT ---")

cursor.execute("""
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders
ON users.user_id = orders.user_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
