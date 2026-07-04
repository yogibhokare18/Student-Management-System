'''from database import cursor

def view_students():
    n = int(input("How many students do you want to view? "))

    cursor.execute("SELECT * FROM students LIMIT %s", (n,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)'''

from database import cursor

def view_students():

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    if rows:
        print("\n------ Student List ------")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Mobile: {row[4]}")
    else:
        print("No students found.")