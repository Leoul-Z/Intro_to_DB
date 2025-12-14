import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (not to a specific database)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close cursor and connection safely
    try:
        if cursor:
            cursor.close()
        if mydb.is_connected():
            mydb.close()
    except:
        pass
