import sqlite3

db = sqlite3.connect('office.db')
csr = db.cursor()

csr.execute('SELECT * FROM employees')

data  = csr.fetchall()
print(data)