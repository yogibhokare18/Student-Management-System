from database import conn, cursor

def update_student():
    while True:
        student_id = int(input("Enter Student ID : "))
        course = input("Enter New Course : ")

        cursor.execute(
            "UPDATE students SET course=%s WHERE id=%s",
            (course, student_id)
        )

        conn.commit()

        choice = input("Do you want to update another student? (y/n): ")

        if choice.lower() != "y":
            break

    print("Students Updated Successfully.")