from datetime import date
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


def insert_record(connection, category, website, name, url, brief, picture):
    today = date.today()
    try:
        sql = "INSERT INTO NEWS_SITE ( ARTICLE_DATE, CATEGORY, WEBSITE, NAME, URL, BRIEF, PICTURE ) VALUES ( %s, %s, " \
              "%s, " \
              "%s, %s, %s, %s ) "
        val = [(today, category, website, name, url, brief, picture)]
        cursor = connection.cursor()
        cursor.executemany(sql, val)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


def clear_db(connection):
    try:
        sql = "DELETE FROM NEWS_SITE WHERE ID > 0;"
        cursor = connection.cursor()
        cursor.executemany(sql, [()])
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


def get_data(connection):
    try:
        sql = "SELECT JSON_ARRAYAGG(JSON_OBJECT('Id', ID," \
              "'Date', ARTICLE_DATE," \
              "'Category', CATEGORY," \
              "'Website', WEBSITE," \
              "'Name', NAME," \
              "'Url', URL," \
              "'Brief', BRIEF," \
              "'Picture', PICTURE" \
              ")) " \
              "FROM NEWS_SITE;"
        cursor = connection.cursor()
        cursor.execute(sql)
        result_json = cursor.fetchall()
        return result_json
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
