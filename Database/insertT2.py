import sqlite3

con=sqlite3.connect('mycompany.db')
cObj=con.cursor()

# cObj.execute("INSERT INTO employees VALUES(1,'Suddip',75000,'IT','Manager')")
# con.commit()

# cObj.execute("INSERT INTO employees VALUES(?,?,?,?,?)",(2,'Rahin',50000,'Marketing','Senior Manager'))
# con.commit()

# cObj.execute("UPDATE employees SET department='Sales' WHERE id=2")
# con.commit()

# cObj.execute("UPDATE employees SET department=? WHERE id=?",('HR',2))
# con.commit()

# cObj.execute("INSERT INTO employees VALUES(3,'Anik',30000,'IT','Junior Manager')")
# con.commit()

# cObj.execute("INSERT INTO employees VALUES(4,'Sammo',75000,'HR','Manager')")
# con.commit()

# cObj.execute("INSERT INTO employees VALUES(5,'Enamul',75000,'Marketing','Manager')")
# con.commit()

# cObj.execute("INSERT INTO employees VALUES(6,'Maliha',75000,'Sales','Manager')")
# con.commit()

# cObj.execute("DELETE FROM employees WHERE name=?",('Anik',))
# con.commit()

# cObj.execute("DELETE FROM employees")
# con.commit()


cObj.execute("SELECT * FROM employees")
result=cObj.fetchall()
#print(result)

for i in result:
    print(i)

cObj.close()
con.close()