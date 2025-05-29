import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="petato_db"
    )
    print("✅ Connection successful!")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")