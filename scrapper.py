from bs4 import BeautifulSoup
import requests
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


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection()

today = date.today()
category = 'Breaking'
website = 'stuff'

source = requests.get('https://stuff.co.nz').text
soup = BeautifulSoup(source, "xml")

article_list = soup.find('app-vertical-article-list')
article_names = article_list.find_all('h3')
article_links = article_list.find_all('a', href=True)
article_count = len(article_names)

for x in range(article_count):
    name = article_names[x].text.rstrip()
    print(name)

    url = 'https://stuff.co.nz' + article_links[x]['href']
    print(url)

    source = requests.get('https://stuff.co.nz' + article_links[x]['href']).text
    soup = BeautifulSoup(source, "xml")
    brief = soup.find(
        class_='sics-component__html-injector sics-component__story__intro sics-component__story__paragraph').text
    print(brief)
    print('---')

    sql = "INSERT INTO news_site ( ARTICLE_DATE, CATEGORY, WEBSITE, NAME, URL, BRIEF, PICTURE ) VALUES ( %s, %s, %s, " \
          "%s, %s, %s, %s ) "
    val = [(today, category, website, name, url, brief, 'NULL')]

    cursor = connection.cursor()
    cursor.executemany(sql, val)
    connection.commit()
