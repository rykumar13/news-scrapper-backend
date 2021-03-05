from bs4 import BeautifulSoup
import requests

source = requests.get('https://stuff.co.nz').text
# source = requests.get('https://www.nzherald.co.nz').text

soup = BeautifulSoup(source, "xml")
tags = soup.find('app-vertical-article-list')
print(tags)
