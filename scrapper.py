from bs4 import BeautifulSoup
import requests

source = requests.get('https://stuff.co.nz').text
# source = requests.get('https://www.nzherald.co.nz').text

soup = BeautifulSoup(source, "xml")
tags = soup.find('app-vertical-article-list')

# print(tags)

# find ArticleName
# articles = tags.find_all('h3')
# for x in articles:
#     print(x.text)

# find hrefs
# for a in tags.find_all('a', href=True):
#     print(a['href'])

# retrieve brief desc
for a in tags.find_all('a', href=True):
    article_link = "https://stuff.co.nz" + a['href']
    print(article_link)

    source2 = requests.get(article_link).text
    soup2 = BeautifulSoup(source2, "xml")
    print(soup2)
    desc = soup.find_all('p')
    break
    # for x in desc:
        # print(x)
        # print('test')
    # print(desc)

# <p class="sics-component__html-injector sics-component__story__intro sics-component__story__paragraph">
