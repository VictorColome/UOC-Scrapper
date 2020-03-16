import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        pass

    @staticmethod
    def scrap():
        page = requests.get("https://www.wikipedia.org/")
        print(page)
        soup = BeautifulSoup(page.content, features="html.parser")
        print(soup.prettify())
