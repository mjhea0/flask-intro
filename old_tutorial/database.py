import sqlite3

con = sqlite3.connect("flasktask.db")

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS ftasks")
    cur.execute("CREATE TABLE ftasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)")
    cur.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES("Finish this tutorial", "02/03/2013", 10, 1)')
    cur.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES("Finish my book", "02/03/2013", 10, 1)')

con.close()
