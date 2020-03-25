import requests
from bs4 import BeautifulSoup

from sample.article import Article
from sample.data_exporter import DataExporter


class Categoria:
    """
    Class containing the information regarding categories of items
    """
    loc = ""
    lastmod = ""
    changefreq = ""
    priority = ""

    def __str__(self):
        return "\nloc="+self.loc+"\nlastmod="+self.lastmod+"\nchangefreq="+self.changefreq+"\npriority="+self.priority


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

    def scrap_all(self):
        """Scrap every article from every category"""
        articles = []
        categories = self.scrap_categories()

        for x in range(len(categories)):
            print(categories[x])

        for category in categories:
            articles_to_scrap = self.scrap_category(category)
            for article_to_scrap in articles_to_scrap:
                articles.append(self.scrap_article(self.host + article_to_scrap))
            data_exporter = DataExporter()
            data_exporter.export_articles_to_csv(articles)

    # TODO: Carlos
    def scrap_categories(self):
        """Scrap all categories from the sitemap https://www.pccomponentes.com/sitemap_categories.xml"""
        page = requests.get("https://www.pccomponentes.com/sitemap_categories.xml")
        soup = BeautifulSoup(page.text, "html.parser")
        cat_list = soup.find_all('url')
        categorias = []
        for cat in cat_list:
            newcat = Categoria()
            newcat.loc = cat.find_all('loc')[0].get_text()
            newcat.lastmod = cat.find_all('lastmod')[0].get_text()
            newcat.changefreq = cat.find_all('changefreq')[0].get_text()
            newcat.priority = cat.find_all('priority')[0].get_text()
            categorias.append(newcat)

        print(categorias)
        return categorias

    # TODO: Victor
    def scrap_category(self, category_url):
        """Scrap a given category"""
        # https://www.pccomponentes.com/smartphone-moviles?page=41 (971 articulos / 24 por página)
        page = requests.get(category_url + "?page=1")
        i = 1
        articles = []
        while page.status_code != 404:
            soup = BeautifulSoup(page.content, features="html.parser")
            articles = articles + list(map(self.__get_url, soup.findAll("div", {"class": "js-article-info"})))
            i += 1
            # TODO Delete or change ?page functionality
            if i == 2:
                break
            page = requests.get(category_url + "?page=" + str(i))
        return articles

    def __get_url(self, article_info):
        return article_info['data-url']

    def scrap_article(self, article_url):
        """Scrap a single article"""
        article = Article()
        page = requests.get(article_url)
        soup = BeautifulSoup(page.content, features="html.parser")
        self.__scrap_article_attributes(article, soup)
        self.__scrap_article_specifications(article, soup)
        return article

    # TODO: Victor
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

        """Scrap article's specifications and features"""
        article.specifications = soup.find("div", {"id": "ficha-producto-caracteristicas"}).string
        pass
