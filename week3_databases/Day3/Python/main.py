import sqlite3

conn = sqlite3.connect("iris.db")
cursor = conn.cursor()

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
cursor.execute("SELECT * FROM data")
print(cursor.fetchall())

print("\n<== Select PetalLength Where PatelLength Greater than 1.5 ==>\n")


cursor.execute("SELECT * FROM data WHERE petallength > 1.5")
print(cursor.fetchall())

conn.commit()
conn.close()