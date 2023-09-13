import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS python_programming")
table = """ CREATE TABLE python_programming (
            id INT PRIMARY KEY,
            name TEXT NOT NULL,
            grade INT
        ); """
cur.execute(table)

data = [
    (55, "Carl Devis", 61),
    (66, "Denis Fredrickson", 88),
    (77, "Jane Riachards", 78),
    (12, "Peyton Swayer", 45),
    (2, "Lucas Brooke", 99)
]
cur.executemany("INSERT INTO python_programming VALUES(?, ?, ?)", data)
con.commit()

print("\nQuery 1...")
for row in cur.execute("SELECT * FROM python_programming WHERE grade >= 60 and grade <= 80;"):
    print(row)

print("\nQuery 2...")
cur.execute('UPDATE python_programming SET grade = 65 WHERE name="Carl Devis";')
for row in cur.execute("SELECT * FROM python_programming;"):
    print(row)

print("\nQuery 3...")
cur.execute('DELETE FROM python_programming WHERE name="Denis Fredrickson";')
for row in cur.execute("SELECT * FROM python_programming;"):
    print(row)

print("\nQuery 4...")
cur.execute('UPDATE python_programming SET grade = 10 WHERE id < 55;')
for row in cur.execute("SELECT * FROM python_programming;"):
    print(row)
