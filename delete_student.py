"""from database import conn, cursor

def delete_student():
    while True:
        student_id = int(input("Enter Student ID : "))

        cursor.execute(
            "DELETE FROM students WHERE id=%s",
            (student_id,)
        )

        conn.commit()

        choice = input("Do you want to delete another student? (y/n): ")

        if choice.lower() != "y":
            break

    print("Students Deleted Successfully.")

from database import conn, cursor

def delete_student():
    student_id = int(input("Enter Student ID : "))

    # Delete Student
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))

    # Shift Remaining IDs
    cursor.execute(
        "UPDATE students SET id = id - 1 WHERE id > %s",
        (student_id,)
    )

    conn.commit()

    print("Student Deleted Successfully")

from database import conn, cursor

def delete_student():

    while True:
        student_id = int(input("Enter Student ID : "))

        # Check if ID exists
        cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
        student = cursor.fetchone()

        if student:
            # Delete Student
            cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))

            # Shift Remaining IDs (College Project साठी)
            cursor.execute(
                "UPDATE students SET id = id - 1 WHERE id > %s",
                (student_id,)
            )

            conn.commit()
            print("Student Deleted Successfully.")
        else:
            print("Student ID Not Found!")

        # Ask user
        choice = input("\nDo you want to delete another student? (y/n): ")

        if choice.lower() != "y":
            print("Returning to Main Menu...")
            break"""

from database import conn, cursor

def delete_student():

    while True:
        student_id = int(input("Enter Student ID : "))

        # Check if ID exists
        cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
        student = cursor.fetchone()

        if student:
            # Delete Student
            cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))

            # Shift Remaining IDs (College Project)
            cursor.execute(
                "UPDATE students SET id = id - 1 WHERE id > %s",
                (student_id,)
            )

            conn.commit()
            print("Student Deleted Successfully.")

            # Check if table is empty
            cursor.execute("SELECT COUNT(*) FROM students")
            count = cursor.fetchone()[0]

            if count == 0:
                cursor.execute("ALTER TABLE students AUTO_INCREMENT = 1")
                conn.commit()
                print("Table is empty. Auto Increment Reset to 1.")

        else:
            print("Student ID Not Found!")

        # Ask user
        choice = input("\nDo you want to delete another student? (y/n): ")

        if choice.lower() != "y":
            print("Returning to Main Menu...")
            break