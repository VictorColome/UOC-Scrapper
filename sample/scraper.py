import traceback

import requests
# Needed for parsing the website HTML
from bs4 import BeautifulSoup
# Used for mimicking the browser
from fake_useragent import UserAgent

from sample.article import Article
from sample.data_exporter import DataExporter
from sample.feature import Feature
from sample.feature import Specification


class Category:
    """
    Class containing the information regarding categories of items
    """
    name = ""
    loc = ""
    lastmod = ""
    changefreq = ""
    priority = ""

    def __str__(self):
        return "\nname=" + self.name + \
               "\nloc=" + self.loc + \
               "\nlastmod=" + self.lastmod + \
               "\nchangefreq=" + self.changefreq + \
               "\npriority=" + self.priority


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

        categories = self.scrap_categories()

        # for x in range(len(categories)):
        #     print(categories[x])

        for category in categories:
            articles_to_scrap = self.scrap_category(category.loc)
            if articles_to_scrap is None:  # If it is a parent category, skip it
                print("Skip parent category " + category.loc)
                continue

            print("Processing category " + category.loc)
            for article_to_scrap in articles_to_scrap:
                articles.append(self.scrap_article(self.host + article_to_scrap))
            data_exporter = DataExporter()
            data_exporter.export_articles_to_csv(category.name, articles)

    # DONE: Carlos
    def scrap_categories(self):
        """
        Scrap all categories from the sitemap https://www.pccomponentes.com/sitemap_categories.xml
        :return: list of categories
        """
        page = requests.get("https://www.pccomponentes.com/sitemap_categories.xml", headers={'User-Agent': self.ua})
        soup = BeautifulSoup(page.text, features="html.parser")
        # Let's find first all the URLs present in the page.
        cat_list = soup.find_all('url')
        categories = []
        for cat in cat_list:
            # We create the new Category...
            newcat = Category()
            # ... and extract the basic data
            newcat.loc = cat.find_all('loc')[0].get_text()
            newcat.lastmod = cat.find_all('lastmod')[0].get_text()
            newcat.changefreq = cat.find_all('changefreq')[0].get_text()
            newcat.priority = cat.find_all('priority')[0].get_text()
            newcat.name = newcat.loc.split('/')[len(newcat.loc.split('/')) - 1]
            categories.append(newcat)
            print('New category read ' + str(newcat))
        # print(categorias)
        return categories

    # DONE: Victor
    def scrap_category(self, category_url):
        """
        Scrap a given category
        :param category_url: category url from where to scrap
        :return: list of articles
        """
        print("Scrap category " + category_url)
        article_urls = []
        i = 2  # 0 and 1 appears in robots.txt as disallowed, so start at 2
        page = requests.get(category_url + "?page=" + str(i), headers={'User-Agent': self.ua})
        soup = BeautifulSoup(page.content, features="html.parser")
        # If it is a parent category, return None
        if len(soup.findAll("body", {"class": "familia-secundaria"})) == 0:
            return None
        while page.status_code != 404:
            article_urls = article_urls + list(map(self.__get_url, soup.findAll("div", {"class": "js-article-info"})))
            i += 1
            # TODO Delete or change ?page functionality or add wait timer
            if i == 3:
                break
            page = requests.get(category_url + "?page=" + str(i), headers={'User-Agent': self.ua})
            soup = BeautifulSoup(page.content, features="html.parser")
        return article_urls

    def __get_url(self, article_info):
        """
        Lambda function to retrieve data-url from article's information
        :param article_info: article's information
        :return: 'data-url' content
        """
        return article_info['data-url']

    def scrap_article(self, article_url):
        """
        Scrap a single article
        :param article_url: article url from where to scrap
        :return: article
        """
        article = Article()
        page = requests.get(article_url, headers={'User-Agent': self.ua})
        soup = BeautifulSoup(page.content, features="html.parser")
        self.__scrap_article_attributes(article, soup)
        self.__scrap_article_specifications(article, soup)
        return article

    # DONE: Victor
    def __scrap_article_attributes(self, article, soup):
        """
        Scrap article's attributes
        :param article: article
        :param soup: BeautifulSoup instantiation
        """
        article.name = soup.find("div", {"class": "articulo"}).find('strong').string
        price_info = soup.find("div", {"id": "precio-main"})
        article.price = '' if price_info is None else price_info['data-price']
        article.pvp = '' if price_info is None else price_info['data-baseprice']
        article.discount = '' if price_info is None else price_info['data-discount']
        no_iva = soup.find("b", {"class": "no-iva-base"})
        article.no_iva = '' if no_iva is None else float(no_iva.string.replace(',', '.'))
        article.rating = float(soup.find("div", {"class": "rating-stars"})['style'].split(':')[1].split('%')[0])

    # DONE: Carlos
    def __scrap_article_specifications(self, article, soup):
        """
        Scrap article's specifications
        :param article: article
        :param soup: BeautifulSoup instantiation
        """
        try:
            feat_item = soup.find("div", {"id": "ficha-producto-caracteristicas"})
            feat = Feature()

            if feat_item.find('<h2>Características:</h2>'):
                feat_list = feat_item.find_all('ul')[0]
                spec_list = feat_item.find_all('ul')[1]
            else:
                spec_list = feat_item.find_all('ul')[0]

            if feat_item.find('<h2>Características:</h2>'):
                feat.characteristics = []
                for feat in feat_list:
                    feat.characteristics.append(feat.text)

            feat.specifications = []
            for spec in spec_list:
                spec_ind = Specification()
                spec_ind.specs = []
                for i, spec_grp in enumerate(spec):
                    if i == 0:
                        spec_ind.name = str(spec_grp)
                    else:
                        # There are 2 main types of articles. This is where we differentiate between them
                        if spec_ind.name.find("strong") == -1:
                            # In one case, there is a list of specifications...
                            for spec_item in spec_grp:
                                try:
                                    spec_ind.specs.append(str(spec_item.text))
                                except Exception as ex:
                                    spec_ind.specs.append(spec_item)
                        else:
                            # ... while in the other case there is just one item
                            try:
                                spec_ind.specs.append(str(spec_grp.text))
                            # In some cases, there is structure, just text storing this item
                            except Exception as ex:
                                spec_ind.specs.append(spec_grp)

                feat.specifications.append(spec_ind)

            # Here we get the URL to the item (if any)
            url = feat_item.find("div", {"class": "ficha-producto-caracteristicas__url-fabricante m-t-2"})
            if url is not None:
                feat.manufacturer_url = url.find("a").get("href")
            article.features = feat
        except Exception as err:
            # There are some articles that are of a third kind: they only contain a list of specifications.
            # Since there are few (164 out of 2250: 7%), we just ignore them
            traceback.print_tb(err.__traceback__)
            print("Error leyendo el artículo: " + article.name)
