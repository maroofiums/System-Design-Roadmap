import sqlite3

# Connect to database
conn = sqlite3.connect("iris.db")
cursor = conn.cursor()

# CREATE
cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    sepallength REAL,
    sepalwidth REAL,
    petallength REAL,
    petalwidth REAL,
    species TEXT
)
""")

# INSERT one row
cursor.execute("""
INSERT INTO data (
    sepallength, sepalwidth, petallength, petalwidth, species
)
VALUES (?, ?, ?, ?, ?)
""", (5.1, 3.5, 1.4, 0.2, "setosa"))

# INSERT multiple rows
cursor.executemany("""
INSERT INTO data (
    sepallength, sepalwidth, petallength, petalwidth, species
)
VALUES (?, ?, ?, ?, ?)
""", [
    (4.9, 3.0, 1.4, 0.2, "setosa"),
    (4.7, 3.2, 1.3, 0.2, "setosa"),
    (4.6, 3.1, 1.5, 0.2, "setosa"),
    (5.0, 3.6, 1.4, 0.2, "setosa"),
    (5.4, 3.9, 1.7, 0.4, "setosa")
])

# READ
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())

# UPDATE
cursor.execute("""
UPDATE data
SET species = 'versicolor'
WHERE id = 1
""")

# DELETE
cursor.execute("""
DELETE FROM data
WHERE id = 2
""")

# Show updated table
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())

# Save changes and close
conn.commit()
conn.close()