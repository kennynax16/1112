import requests
from bs4 import BeautifulSoup
import csv
import os
import fake_useragent

HOST = 'https://kinobar.vip/'
URL = 'https://kinobar.vip/'
ua = fake_useragent.UserAgent()
HEADERS ={
    "User-Agent" : ua.random
}


def get_html(url,params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r




def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_='main_news')
    movie = []
    for item in items:
        movie.append({
            'top': item.find('h2', class_='zagolovok').find_next('b').get_text(),
            'link': item.find('h2', class_='zagolovok').find_next('a').get('href'),
            'descrip': item.find('div', class_='mn_story').get_text(strip=True),

        })
    return movie

def parser():
    PAGENATION = input('Укажите количество страниц для парсинга:')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        movie = []
        for page in range(1,PAGENATION):
            print(f'Парсим страницу :{page}')
            html = get_html(URL, params={'page': page})
            movie.extend(get_content(html.text))
            print(movie)
        else:
            print('Error')

parser()