from bs4 import BeautifulSoup
import requests
import db_helper as db


def stuff_scrapper(connection):
    category = 'Breaking'
    website = 'stuff'
    base_url = 'https://stuff.co.nz'
    source = requests.get(base_url).text
    soup = BeautifulSoup(source, "xml")

    article_list = soup.find('app-vertical-article-list')
    article_names = article_list.find_all('h3')
    article_links = article_list.find_all('a', href=True)
    article_count = len(article_names)

    for x in range(article_count):
        name = article_names[x].text.rstrip()
        url = base_url + article_links[x]['href']
        source = requests.get('https://stuff.co.nz' + article_links[x]['href']).text
        soup = BeautifulSoup(source, "xml")
        brief = soup.find(
            class_='sics-component__html-injector sics-component__story__intro sics-component__story__paragraph').text[
                0:250]
        db.insert_record(connection, category, website, name, url, brief, 'NULL')


def rnz_scrapper(connection):
    category = 'Breaking'
    website = 'rnz'
    base_url = 'https://www.rnz.co.nz/'
    source = requests.get(base_url).text
    soup = BeautifulSoup(source, "lxml")

    raw_o_digest_detail_list = soup.find_all(class_='o-digest__detail')
    o_digest_detail = raw_o_digest_detail_list[:4]

    for x in o_digest_detail:
        namelink = x.find(class_='faux-link')
        name = namelink.text
        url = base_url + namelink.get('href')
        brief = x.find(class_='o-digest__summary').text.strip('\n')[0:250]
        db.insert_record(connection, category, website, name, url, brief, 'NULL')


def scoop_scrapper(connection):
    category = 'Breaking'
    website = 'scoop'
    base_url = 'https://www.scoop.co.nz/'
    source = requests.get(base_url).text
    soup = BeautifulSoup(source, "lxml")

    stories = soup.find_all(class_='top-story')[:6]

    for x in stories:
        name = x.find('a', href=True, text=True).text
        url = x.find('a', href=True, text=True)['href']
        source2 = requests.get(url).text
        soup2 = BeautifulSoup(source2, 'lxml')
        paragraphs = soup2.find_all('p')
        brief = paragraphs[2].text.replace('\n', ' ')[0:250]
        db.insert_record(connection, category, website, name, url, brief, 'NULL')


def main():
    connection = db.create_connection()
    db.clear_db(connection)
    stuff_scrapper(connection)
    rnz_scrapper(connection)
    scoop_scrapper(connection)


if __name__ == "__main__":
    main()
