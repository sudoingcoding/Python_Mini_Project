import sqlite3

con=sqlite3.connect('mycompany.db')
cObj=con.cursor()

cObj.execute("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT,salary REAL,department TEXT,position TEXT)")
con.commit()

def insert_value(id,name,salary,department,position):
    cObj.execute("INSERT INTO employees VALUES(?,?,?,?,?)",(id,name,salary,department,position))
    con.commit()

def update_dept(id,department):
    cObj.execute("UPDATE employees SET department=? WHERE id=?",(department,id))
    con.commit()

def sql_fetch():
    cObj.execute("SELECT * FROM employees")
    result=cObj.fetchall()
    for i in result:
        print(i)

def delete_all():
    cObj.execute("DELETE FROM employees")
    con.commit()

delete_all()

insert_value(1,'Suddip',75000,'IT','Manager')
insert_value(2,'Rahin',50000,'Marketing','Senior Manager')
insert_value(3,'Anik',30000,'IT','Junior Manager')
insert_value(4,'Sammo',75000,'HR','Manager')
insert_value(5,'Enamul',75000,'Marketing','Manager')
insert_value(6,'Maliha',75000,'Sales','Manager')

sql_fetch()

cObj.close()
con.close()