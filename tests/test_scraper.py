import unittest

from sample import Scraper


class TestScraper(unittest.TestCase):

    # TODO: Carlos
    def test_scrap_categories(self):
        pass

    # TODO: Victor
    def test_scrap_category(self):
        scraper = Scraper()
        articles = scraper.scrap_category("https://www.pccomponentes.com/smartphone-moviles")
        assert articles is not None
        for a in articles:
            assert a is not None
            print(a)

    def test_scrap_article(self):
        scraper = Scraper()
        print(scraper.scrap_article("https://www.pccomponentes.com/xiaomi-redmi-note-8t-4-64gb-azul-estelar-libre"))
        print(scraper.scrap_article("https://www.pccomponentes.com/xiaomi-redmi-7-3-64gb-rojo-lunar-libre"))


if __name__ == '__main__':
    unittest.main()
