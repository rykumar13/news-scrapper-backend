from bs4 import BeautifulSoup
import requests

source = requests.get('https://stuff.co.nz').text
soup = BeautifulSoup(source, "xml")
tags = soup.find('app-vertical-article-list')

# find ArticleName
# articles = tags.find_all('h3')
# for x in articles:
#     print(x.text)

# find hrefs
# for a in tags.find_all('a', href=True):
#     print('https://stuff.co.nz' + a['href'])

# retrieve brief desc
# for a in tags.find_all('a', href=True):
#     article_link = "https://stuff.co.nz" + a['href']
#     print(article_link)
#
#     source2 = requests.get(article_link).text
#     soup2 = BeautifulSoup(source2, "xml")
#     temp = soup2.find(class_='sics-component__html-injector sics-component__story__intro sics-component__story__paragraph').text
#     print(temp)

# retrieve brief desc
for a in tags.find_all('a', href=True):
    article_link = "https://stuff.co.nz" + a['href']
    print(article_link)

    source2 = requests.get(article_link).text
    soup2 = BeautifulSoup(source2, "xml")
    temp = soup2.find(class_='sics-component__html-injector sics-component__story__intro sics-component__story__paragraph').text
    print(temp)