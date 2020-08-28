'''
import sqlite3

dbase = sqlite3.connect('Our_data.db') # open a database file 
print ('Database opened')
 
dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
   ID INT PRIMARY KEY NOT NULL,
   NAME TEXT NOT NULL,
   DIVISION TEXT NOT NULL,
   STARS INT NOT NULL)''')
print ('Table created')

def insert_records(ID, NAME,DIVISION,STARS):

    dbase.execute(''' INSERT INTO employee_records(ID, NAME,DIVISION,STARS)
            VALUES(?,?,?,?)''',(ID, NAME,DIVISION,STARS))

    dbase.commit()
    print ('REcord inserted')
##insert_records(6,'Bob','hardware',4)

def read_data():
    data = dbase.execute('''SELECT ID, NAME,DIVISION,STARS FROM employee_records''')
    for record  in data:
        print ('ID : '+str(record[0])+'\n')
        print ('NAME : '+str(record[0])+'\n')
        print ('DIVISION : '+str(record[0])+'\n')
        print ('STARS : '+str(record[0])+'\n\n')
        
read_data()        


dbase.close()
print ('Database closed')

'''    





import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute('''  CREATE TABLE customer (
        first_name text,
        last_name text,
        email text)''')
conn.commit()

conn.close()
