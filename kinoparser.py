import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.kinopoisk.ru/popular/'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

divs = soup.find_all("div", {'class': 'desktop-rating-selection-film-item'})

def find_content():
    for div in divs:
        div_title = div.find('div', {'class': "selection-film-item-meta selection-film-item-meta_theme_desktop"})
        link_text = div_title.find('p').text
        print (link_text)
    return

print(find_content())

