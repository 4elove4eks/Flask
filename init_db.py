import sqlite3

connection = sqlite3.connect("database.db")
with open('schema.sql') as f:
    connection.executescript()

cursor = connection.cursor()

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
               ('Post', 'Content for the first post'))
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
               ('Second Post', 'Content for the second post'))

posts = cursor.execute('''SELECT * FROM posts'''). fetchall()
for post in posts:
    print(post)

connection.commit()
connection.close()