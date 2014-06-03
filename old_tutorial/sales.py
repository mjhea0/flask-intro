import sqlite3 as lite
import sys

sales = (
	('John', 22000),
    ('Derek', 25000),
    ('Lily', 28000),
    ('Josh', 20000),
    ('Keving', 29000),
    ('Kim', 18000),
    ('Ryan', 25000),
	('Henry', 25000),
	('Brian', 19000),
	('Kelly', 29000)
)


con = lite.connect('sales.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS reps")
    cur.execute("CREATE TABLE reps(rep_name TEXT, amount INT)")
    cur.executemany("INSERT INTO reps VALUES(?, ?)", sales)