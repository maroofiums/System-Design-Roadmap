import sqlite3

conn = sqlite3.connect("iris.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sepallength REAL,
    sepalwidth  REAL,
    petallength REAL,
    petalwidth REAL,
    species TEXT
)
""")

conn.commit()
conn.close()