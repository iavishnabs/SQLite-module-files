import sqlite3

db = sqlite3.connect('office.db')
csr = db.cursor()

sql_command = '''
CREATE TABLE employees(
id INTEGER PRIMARY KEY,
f_name VARCHAR(20),
l_name VARCHAR(20),
join_date DATE,
salary INTEGER
);
'''
csr.execute(sql_command)

sql_command = '''
INSERT INTO employees VALUES(1,'nima','thomson',2023-05-09,20000);
'''
csr.execute(sql_command)

sql_command = '''
INSERT INTO employees VALUES(2,'riya','thomson',2023-05-09,30000);
'''
csr.execute(sql_command)

sql_command = '''
INSERT INTO employees VALUES(3,'neha','thomson',2023-05-09,10000);
'''
csr.execute(sql_command)

db.commit()
db.close()