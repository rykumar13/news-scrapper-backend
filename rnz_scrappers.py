from bs4 import BeautifulSoup
import requests
from datetime import date
import db_helper as db

connection = db.create_connection()

today = date.today()
category = 'Breaking'
website = 'rnz'

source = requests.get('https://www.rnz.co.nz/').text
soup = BeautifulSoup(source, "lxml")
base_url = 'https://www.rnz.co.nz/'

raw_o_digest_detail_list = soup.find_all(class_='o-digest__detail')
o_digest_detail = raw_o_digest_detail_list[:4]

for x in o_digest_detail:
    namelink = x.find(class_='faux-link')
    name = namelink.text
    url = base_url + namelink.get('href')
    brief = x.find(class_='o-digest__summary').text.strip('\n')

    sql = "INSERT INTO news_site ( ARTICLE_DATE, CATEGORY, WEBSITE, NAME, URL, BRIEF, PICTURE ) VALUES ( %s, %s, %s, " \
          "%s, %s, %s, %s ) "
    val = [(today, category, website, name, url, brief, 'null')]

    cursor = connection.cursor()
    cursor.executemany(sql, val)
    connection.commit()