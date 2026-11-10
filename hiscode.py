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

def addStudent():
    print("Enter the following information for the new student")
    first=input("First Name: ")
    last=input("Last Name: ")
    major=input("Major: ")
    phone=input("Phone: ")
    insertStudent(first,last,major,phone)

def deleteStudent():
    # Assignment for students to write this code.
    pass

def getStudent(id):
    query=f"""
      select first,last,phone,major,id from students where id={id};"""
    curs.execute(query)
    rows = curs.fetchall()
    return rows[0]

def outputStudent(studentInfo):
    print(f"Id:{studentInfo[4]}")
    print(f"First: {studentInfo[0]} Last:{studentInfo[1]}")
    print(f"Phone: {studentInfo[2]} Major: {studentInfo[3]}")

def showStudent():
    print("Enter the id information for the student")
    id=input("Id: ")
    studentInfo=getStudent(id)
    #print(rows)
    outputStudent(studentInfo)


def getStudents():
    query=f"""
      select id,first,last,phone from students order by id;"""
    curs.execute(query)
    rows = curs.fetchall()

def showStudents():
    students=getStudents()
    for student in students:
        outputStudent(student)

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

def updateStudent():
    print("Enter the following new information for the existing student")
    id=input("Id: ")
    first=input("First Name: ")
    last=input("Last Name: ")
    major=input("Major: ")
    phone=input("Phone: ")
    changeStudent(id,first,last,major,phone)

choice="1"
while (choice!='0'):
    print("!!!!!!MENU!!!!!!")
    print("1) Add a student")
    print("2) Delete a student")
    print("3) Show a student")
    print("4) Update a student")
    print("5) Show all Students")
    print("0) Quit")
    choice=input("Type the number for your choice: ")
    if (choice=='1'): 
        addStudent()
    if (choice=='2'):
        deleteStudent()
    if (choice=='3'):
        showStudent()
    if (choice=='4'):
        updateStudent()
    if (choice=='5'):
        showStudents()

