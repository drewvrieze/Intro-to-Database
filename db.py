# these are the data structures and functions we need from the database
import psycopg2
import os

try:
    conn = psycopg2.connect(
        dbname=os.environ['DBNAME'],
        user=os.environ['DBUSER'],
        host=os.environ['DBHOST'],
        password=os.environ['DBPASSWORD'])
    curs=conn.cursor()
except:
    print("I am unable to connect to the database")

# pure database functionality for a student
def insertStudent(first,last,major,phone):
    query=f"""insert into students 
      (first,last,phone,major) 
      values ('{first}','{last}','{phone}','{major}');"""
    #print(query)
    curs.execute(query)
    conn.commit()

def deleteStudent():
    print("Enter the id information for the student")
    id = input("Id: ")
    query = f""" delete from students where id = {id};"""
    curs.execute(query)
    conn.commit()

def getStudents():
    query=f"""
      select id,first,last,phone from students order by id;"""
    curs.execute(query)
    rows = curs.fetchall()

def changeStudent(id,first,last,major,phone):
    values=""
    comma=False
    if len(first)>0:
        values+=f"first='{first}'"
        comma=True
    if len(last)>0:
        if (comma):
            values+=','
        values+=f"last='{last}'"
        comma=True
    if len(major)>0:
        if (comma):
            values+=','
        values+=f"major='{major}'"
        comma=True
    if len(phone)>0:
        if (comma):
            values+=','
        values+=f"phone='{phone}'"
        comma=True
    if (comma):
      query=f"""update students 
        set {values} 
        where id={id};"""
      curs.execute(query)
      conn.commit() 