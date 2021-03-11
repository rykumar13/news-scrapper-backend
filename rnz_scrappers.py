from bs4 import BeautifulSoup
import requests
from datetime import date
import mysql.connector
from mysql.connector import Error
import database_creds


source = requests.get('https://www.rnz.co.nz/').text
soup = BeautifulSoup(source, "html")

print(soup)
