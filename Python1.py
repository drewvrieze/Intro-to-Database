import psycopg2
import os



try:
    conn = psycopg2.connect(dbname =os.environ['DBNAME'],user=os.environ['DBUSER'],host=os.environ['DBHOST'],password=os.environ['DBPASSWORD'])
    curs = conn.cursor()
except:
    print("I am unable to connect to the database")


# Figure out how to do venv.drivers



def addStudent():
    first = input("First Name: ")
    last = input("Last Name: ")
    major = input("Major: ")
    phone = input("Phone: ")
    query = f"""insert into students (id,first,last,phone,major) values ('{first}','{last}','{phone}');"""
    #print(query)
    curs.execute(query)
    conn.commit()
    pass

def deleteStudent():
    print("Enter the id information for the student")
    id = input("Id: ")
    query = f""" delete from students where id = {id};"""
    curs.execute(query)
    conn.commit()

def showStudent():
    print("Enter the id of the student")
    id = input("Id: ")
    query = f""" select first, last, phone, major from students where id={id};""" 
    curs.execute(query)
    rows = curs.fetchall()
    print(rows)
    print(f"First: {rows[0][0]} Last: {rows[0][1]}")
    print(f"Phone: {rows[0][2]} Major: {rows[0][3]}")

def showStudents():
    query = f""" select id, first, last, phone, major from students;""" 
    curs.execute(query)
    rows = curs.fetchall()
    print(rows)
    for row in rows:
        print(f"ID: {row[0]}")
        print(f"First: {rows[1]} Last: {rows[2]}")
        print(f"Phone: {rows[3]} Major: {rows[4]}")

def updateStudent():
    id = input("Enter the student ID: ")
    first = input("First Name: ")
    last = input("Last Name: ")
    major = input("Major: ")
    phone = input("Phone: ")
    query = f"""update students set first='{first}', last = '{last}', phone = '{phone}', major = '{major}' where id = {id};"""
    curs.execute(query)
    conn.commit()
    print(query)

choice="1"
while (choice!='0'):
    print("1) Add a student")
    print("2) Delete a student")
    print("3) Show a student")
    print("4) Update a student")
    print("5) Show all Students")
    print("0) Quit")
    choice = input("Type the number for your choice: ")
    if (choice == '1'):
        addStudent()
    if (choice == '2'):
        deleteStudent()
    if (choice == '3'):
        showStudent()
    if (choice == '4'):
        updateStudent()
    if (choice == '5'):
        showStudents()




    