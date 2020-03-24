import csv
import unittest
from datetime import date

from sample.article import Article
from sample.data_exporter import DataExporter


class TestDataExporter(unittest.TestCase):

    # TODO: Victor
    def test_export_attributes_to_csv(self):
        pass

    # TODO: Carlos
    def test_export_specifications_to_csv(self):
        data_exporter = DataExporter()
        article = Article()
        article.name = 'name'
        article.discount = 21
        article.no_iva = 100
        article.pvp = 150
        article.price = 200
        data_exporter.export_attributes_to_csv([article])
        self.__read_file()

    def __read_file(self):
        file_name = 'csv/articles_attributes_' + str(date.today()).replace('-', '') + '.csv'
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                print(f'Column names are {", ".join(row)}')


if __name__ == '__main__':
    unittest.main()
