import mysql.connector
from mysql.connector import Error
import database_creds


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=database_creds.host,
            user=database_creds.user,
            passwd=database_creds.passwd,
            database=database_creds.database
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
