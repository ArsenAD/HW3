from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://www.ts.kg/category/turkish_tv_series"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="app-shows-item-full")
    movies = []
    for item in items:
        info = item.find('span', class_="app-shows-card-tooltip").string.split(', '),
        new = {
            'link': item.find('a').get('href'),
            'title': item.find('span', class_="app-shows-card-title").find('a').string,
            'date': info[0],
            'genre': info[1],
            'views': item.fing('span', class_="app-shows-card-labels").string

        }
        movies.append(new)
    return movies
html = get_html(URL)
get_data(html.text)


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        wheel = []
        html = get_html(URL)
        dong = get_data(html.text)
        wheel.extend(dong)

        return wheel
    else:
        raise Exception("Error in parser!")



