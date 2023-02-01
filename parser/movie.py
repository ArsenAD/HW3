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
        info = list(
            item.find('span', class_="app-shows-card-tooltip").getText().replace('\n', '').replace('\t', '').replace(' ', '').split(","))
        new = {
            # 'photo': item.find('a').get('img'),
            'link': 'https://www.ts.kg'+(item.find('a').get('href')),
            'title': item.find('span', class_="app-shows-card-title").find('a').string,
            'date': info[0],
            'views': item.find('span', class_="app-shows-card-labels").getText().replace('\n', '').replace('0', '').replace(' ', '')

        }
        movies.append(new)
        # pprint(movies)
    return movies
# html = get_html(URL)
# get_data(html.text)


def parser():
    html = get_html(URL)
    movies = []
    if html.status_code == 200:
        html = get_html(URL)
        mov = get_data(html.text)
        movies.extend(mov)

        return movies

    else:
        raise Exception("Error in parser!")


