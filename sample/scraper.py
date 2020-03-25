import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from sample.article import Article
from sample.data_exporter import DataExporter
from sample.feature import Feature
from sample.feature import Specification


class Category:
    """
    Class containing the information regarding categories of items
    """
    loc = ""
    lastmod = ""
    changefreq = ""
    priority = ""

    def __str__(self):
        return "\nloc="+self.loc+\
               "\nlastmod="+self.lastmod+\
               "\nchangefreq="+self.changefreq+\
               "\npriority="+self.priority


class Scraper:
    """
    Scraper for the page pccomponentes(https://www.pccomponentes.com/).
    Scraps among the different categories, retrieving all the articles in each one.

    Attributes:
        host: A string representing pccomponentes' host
    """

    def __init__(self):
        """Return a Scraper with pccomponentes' host"""
        self.host = 'https://www.pccomponentes.com'
        self.ua = UserAgent().chrome

    def scrap_all(self):
        """Scrap every article from every category"""
        articles = []
        categories = self.scrap_categories()[:2]   # TODO: Para limitar el alcance durante las pruebas

        # for x in range(len(categories)):
        #     print(categories[x])

        for category in categories:
            articles_to_scrap = self.scrap_category(category)[:3]   # TODO: Para limitar el alcance durante las pruebas
            for article_to_scrap in articles_to_scrap:
                articles.append(self.scrap_article(self.host + article_to_scrap))
            data_exporter = DataExporter()
            print(articles[0])
            data_exporter.export_articles_to_csv(articles)

    # DONE: Carlos
    def scrap_categories(self):
        """Scrap all categories from the sitemap https://www.pccomponentes.com/sitemap_categories.xml"""
        page = requests.get("https://www.pccomponentes.com/sitemap_categories.xml", headers={'User-Agent': self.ua})
        soup = BeautifulSoup(page.text, features="html.parser")
        cat_list = soup.find_all('url')
        categorias = []
        for cat in cat_list:
            newcat = Category()
            newcat.loc = cat.find_all('loc')[0].get_text()
            newcat.lastmod = cat.find_all('lastmod')[0].get_text()
            newcat.changefreq = cat.find_all('changefreq')[0].get_text()
            newcat.priority = cat.find_all('priority')[0].get_text()
            categorias.append(newcat)

        #print(categorias)
        return categorias

    # TODO: Victor
    def scrap_category(self, category_url):
        """Scrap a given category"""
        i = 2  # 0 and 1 appears in robots.txt as disallowed
        page = requests.get(category_url.loc + "?page=" + str(i), headers={'User-Agent': self.ua})
        articles = []
        while page.status_code != 404:
            soup = BeautifulSoup(page.content, features="html.parser")
            articles = articles + list(map(self.__get_url, soup.findAll("div", {"class": "js-article-info"})))
            i += 1
            # TODO Delete or change ?page functionality
            if i == 3:
                break
            page = requests.get(category_url + "?page=" + str(i), headers={'User-Agent': self.ua})
        return articles

    def __get_url(self, article_info):
        return article_info['data-url']

    def scrap_article(self, article_url):
        """Scrap a single article"""
        article = Article()
        page = requests.get(article_url, headers={'User-Agent': self.ua})
        soup = BeautifulSoup(page.content, features="html.parser")
        self.__scrap_article_attributes(article, soup)
        self.__scrap_article_specifications(article, soup)
        return article

    # DONE: Victor
    def __scrap_article_attributes(self, article, soup):
        """Scrap article's attributes"""
        article.name = soup.find("div", {"class": "articulo"}).find('strong').string
        price_info = soup.find("div", {"id": "precio-main"})
        article.price = price_info['data-price']
        article.pvp = price_info['data-baseprice']
        article.discount = price_info['data-discount']
        article.no_iva = soup.find("b", {"class": "no-iva-base"}).string
        article.rating = float(soup.find("div", {"class": "rating-stars"})['style'].split(':')[1].split('%')[0])

    # TODO: Carlos
    def __scrap_article_specifications(self, article, soup):

        try:
            """Scrap article's specifications and features"""
            featitem = soup.find("div", {"id": "ficha-producto-caracteristicas"})
            feat = Feature()

            listacar = featitem.find_all('ul')[0]
            listaesp = featitem.find_all('ul')[1]

            feat.characteristics = []
            for carac in listacar:
                feat.characteristics.append(carac.text)

            feat.specifications = []
            for espec in listaesp:
                spec_ind = Specification()
                spec_ind.specs = []
                for i, especgrp in enumerate(espec):
                    if i == 0:
                        spec_ind.name = str(especgrp)
                    else:
                        for especitem in especgrp:
                            spec_ind.specs.append(str(especitem.text))
                feat.specifications.append(spec_ind)

            capaurl = featitem.find("div", {"class": "ficha-producto-caracteristicas__url-fabricante m-t-2"})
            if capaurl is not None:
                feat.manufacturer_url = capaurl.find("a").next_element

            article.features = feat
        except:
            print("Error leyendo el artículo: " + article.name)
