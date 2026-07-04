from database import conn, cursor

def add_student():
    while True:
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        course = input("Enter Course : ")
        mobile = input("Enter Mobile : ")

        sql = "INSERT INTO students(name, age, course, mobile) VALUES(%s, %s, %s, %s)"
        values = (name, age, course, mobile)

        cursor.execute(sql, values)
        conn.commit()

        choice = input("Do you want to add another student? (y/n): ")

        if choice.lower() != "y":
            break

    print("Students Added Successfully.")