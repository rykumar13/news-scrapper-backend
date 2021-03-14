from bs4 import BeautifulSoup
import requests
from datetime import date
import db_helper as db

connection = db.create_connection()

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
    val = [(today, category, website, name, url, brief, 'null')]

    cursor = connection.cursor()
    cursor.executemany(sql, val)
    connection.commit()
