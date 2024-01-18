import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", 
    port= "3306",
    user="root", 
    password="mysql@anjala",
    database="testdb"
)
print(mydb)
mycursor= mydb.cursor()
mycursor.execute( "CREATE TABLE IF NOT EXISTS students121 (name VARCHAR(255), age INT, sid INT PRIMARY KEY)")
#mycursor.execute("create database testdb")

#mycursor.execute("show databases")
#for db in mycursor:
#    print(db)


#mycursor.execute( "create table students (name VARCHAR(255), age INT)")
#mycursor.execute("show tables")
#for i in mycursor:
#    print(i)

#sql= "insert into students (name, age) Values (%s, %s)"
#student1= ("rachel", 22)
#mycursor.execute (sql, student1)
#mydb.commit()

#sql= "insert into students (name, age) Values (%s, %s)"
#student1= [("rachel", 22), ("ross", 32), ("phoebe", 32), ("monica", 42), ("chandler", 2), ("joey", 1)]
#mycursor.executeall (sql, student1)
#mydb.commit()

#mycursor.execute("SELECT * FROM students where name= 'ross' ")
#myresult= mycursor.fetchall()
#for result in myresult:
#    print(result)

#mycursor.execute("SELECT * FROM students LIMIT 4 OFFSET 2")
#myresult= mycursor.fetchall()
#for result in myresult:
#    print(result)

#sql= "SELECT * FROM students ORDER BY name DESC"
#mycursor.execute(sql)
#myresult= mycursor.fetchall()
#for r in myresult:
#    print (r)

#sql= "DELETE FROM students WHERE name='rachel'"
#mycursor.execute(sql)
#mydb.commit()

#sql= "drop table if exists students121"
#mycursor.execute(sql)
#mydb.commit()
#
