
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yogi",
        database="student_db"
    )

    cursor = conn.cursor()

    print("✅ MySQL Connected Successfully!")

except mysql.connector.Error as err:
    print("❌ Error:", err)