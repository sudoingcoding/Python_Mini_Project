import sqlite3

con=sqlite3.connect('mycompany.db')
cObj=con.cursor()

cObj.execute("INSERT INTO employees VALUES(1,'Suddip',75000,'IT','Manager')")
con.commit()

cObj.close()
con.close()