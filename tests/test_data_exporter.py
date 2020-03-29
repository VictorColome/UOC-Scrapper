import csv
import random
import unittest
from datetime import date

from sample.article import Article
from sample.data_exporter import DataExporter


class TestDataExporter(unittest.TestCase):

    # TODO: Victor
    def test_export_attributes_to_csv(self):
        data_exporter = DataExporter()
        articles = self.__generate_dummy_articles()
        data_exporter.export_attributes_to_csv('category_test', articles)
        self.__read_attributes_csv()

    # TODO: Carlos
    def test_export_specifications_to_csv(self):
        pass

    def test_import_attributes_from_csv(self):
        data_exporter = DataExporter()
        data_exporter.import_attributes_from_csv('../sample/csv/placas-base_articles_attributes_20200329.csv')

    def __generate_dummy_articles(self):
        articles = []
        for i in range(10):
            article = Article()
            article.name = 'name' + str(i)
            article.discount = 21
            article.no_iva = 100 + random.randrange(100)
            article.pvp = 150 + random.randrange(100)
            article.price = 200 + random.randrange(100)
            article.rating = 1 + random.randrange(5)
            articles.append(article)
        return articles

    def __read_attributes_csv(self):
        file_name = 'csv/articles_attributes_' + str(date.today()).replace('-', '') + '.csv'
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if len(row) == 0:
                    continue
                print(f'Column names are {", ".join(row)}')


if __name__ == '__main__':
    unittest.main()
