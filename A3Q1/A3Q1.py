# COMP 3005B Winter24 Assignment #3 Question #1
# Name: Rami Jadayel, Student Number: 101134687

import sys
import psycopg

conn = None

def connectToDB():
    global conn
    if conn is None:
        dbname = input("Enter the database name: ") or "a3p1"
        password = input("Enter the database password: ") or "greetings"
        user = input("Enter the database user: ") or "ta"
        host = input("Enter the database host: ") or "localhost"
        port = input("Enter the database port: ") or "5432"
            
        try:
            print("\nAttempting to connect to PostgreSQL database...")
            db = {
                "dbname": dbname,
                "user": user,
                "password": password,
                "host": host,
                "port": port
            }
            conn = psycopg.connect(**db)
        except psycopg.DatabaseError as e:
            print("Unable to connect to the database. Exiting...")
            print(f"Error: {e}")
            sys.exit(1)

        successful_connection = f"Connected to the PostgreSQL database: '{dbname}' on {host}:{port}"
        print(successful_connection)
        print(f"{'-' * len(successful_connection)}\n")
    return conn
                                  
def formatResultStrings(first_name: str, last_name: str, email: str) -> tuple[str, str, str]:
    '''
    HELPER FUNCTION (getAllStudents())
    Formats first_name, last_name, and email strings such that they fit within the specified column 
    widths in the output table. Extra characters are replaced with "..." indicate string truncation.
    '''
    if len(first_name) > 20:
        first_name = first_name[:17] + "..."
    if len(last_name) > 20:
        last_name = last_name[:17] + "..."
    if len(email) > 30:
        email = email[:27] + "..."
    return first_name, last_name, email

def getAllStudents():
    '''
    FROM ASSIGNMENT SPECIFICATION:
    Retrieves and displays all records from the students table
    '''
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students ORDER BY student_id ASC;")
        rows = cur.fetchall()
        print("Displaying all records from the students table:")
        print(f"{'ID:':<5} | {'First name:':<20} | {'Last name:':<20} | {'Email:':<30} | {'Enrollment Date:':<15}")
        for row in rows:
            student_id, first_name, last_name, email, enrollment_date = row
            first_name, last_name, email = formatResultStrings(first_name, last_name, email)
            print(f"{student_id:<5} | {first_name:<20} | {last_name:<20} | {email:<30} | {enrollment_date}")
        print()

def addStudent(first_name: str, last_name: str, email: str, enrollment_date: str):
    '''
    FROM ASSIGNMENT SPECIFICATION: 
    Inserts a new student record into the students table
    '''
    with conn.cursor() as cur:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                    (first_name, last_name, email, enrollment_date))
        cur.execute("SELECT * FROM students WHERE email = %s", (email,))
        student_id, first_name, last_name, email, enrollment_date = cur.fetchone()
        print(f"Added student to the database.\n++ Student ID: {student_id}\n++ Name: {first_name} {last_name}\n++ Email: {email}\n++ Enrollment date: '{enrollment_date}'\n")
        conn.commit()

def updateStudentEmail(student_id: int, email: str):
    '''
    FROM ASSIGNMENT SPECIFICATION: 
    Updates the email address for a student with the specified student_id
    '''
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        row = cur.fetchone()
        if row is None:
            print(f"Invalid input. No student with ID '{student_id}' exists.\n")
            return
        student_id, first_name, last_name, old_email, _ = row
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))
        conn.commit()
        print(f"Updated email for Student ID {student_id} from ...\n   [OLD] {old_email} -> \n   [NEW] {email}\n")
    
def deleteStudent(student_id: int):
    '''
    FROM ASSIGNMENT SPECIFICATION: 
    Deletes the record of the student with the specified student_id
    '''
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        row = cur.fetchone()
        if row is None:
            print(f"Invalid input. No student with ID '{student_id}' exists.\n")
            return
        student_id, first_name, last_name, email, enrollment_date = row
        print(f"Deleted student from the database.\n-- Student ID: {student_id}\n-- Name: {first_name} {last_name}\n-- Email: {email}\n-- Enrollment date: '{enrollment_date}'\n")
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()

def main():
    connectToDB()
    user_input = input("Choose an option:\n  [1] Display all students\n  [2] Add a student\n  [3] Update a student's email\n  [4] Delete a student via student ID\n  [0] Exit\n>>>")
    match user_input:
        case '0':
            print("Exiting...\n")
            sys.exit(0)
        case '1':
            getAllStudents()
            main()
        case '2':
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            email = input("Enter the student's email: ")
            enrollment_date = input("Enter the student's enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
            main()
        case '3':
            student_id = int(input("Enter the student's ID: "))
            email = input("Enter the student's new email: ")
            updateStudentEmail(student_id, email)
            main()
        case '4':
            try:
                student_id = int(input("Enter the student's ID: "))
            except ValueError:
                print("Invalid input. Please enter a valid student ID.\n")
                main()
            deleteStudent(student_id)
            main()
        case _:
            print("Invalid input. Please try again.\n")
            main()

if __name__ == "__main__":
    main()