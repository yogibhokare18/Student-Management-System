'''from database import cursor

def search_student():
    n = int(input("How many students do you want to search? "))

    for i in range(n):
        print(f"\nSearch Student {i+1}")

        name = input("Enter Student Name : ")

        cursor.execute(
            "SELECT * FROM students WHERE name=%s",
            (name,)
        )

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("Student Not Found")'''

from database import cursor

def search_student():

    while True:
        student_id = int(input("Enter Student ID : "))

        cursor.execute(
            "SELECT * FROM students WHERE id=%s",
            (student_id,)
        )

        row = cursor.fetchone()

        if row:
            print("\nStudent Found")
            print(f"ID      : {row[0]}")
            print(f"Name    : {row[1]}")
            print(f"Age     : {row[2]}")
            print(f"Course  : {row[3]}")
            print(f"Mobile  : {row[4]}")
        else:
            print("❌ Student Not Found")

        choice = input("\nDo you want to search another ID? (y/n): ").lower()

        if choice != "y":
            break
