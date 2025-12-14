import mysql.connector

try:
    # Connect to MySQL Server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    try:
        cursor.close()
        mydb.close()
    except:
        pass
