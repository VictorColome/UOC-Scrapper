import csv
from datetime import date
from pathlib import Path


class DataExporter:

    def export_articles_to_csv(self, category_name, articles):
        """
        Export articles from a given category to CSVs
        :param category_name: category name
        :param articles: list of articles
        :return: create CSV files in sample/csv
        """
        self.export_attributes_to_csv(category_name, articles)
        self.export_specifications_to_csv(category_name, articles)

    def export_attributes_to_csv(self, category_name, articles):
        """
        Export articles' attributes from a given category to CSV
        :param category_name: category name
        :param articles: list of articles
        :return: create CSV file in sample/csv
        """
        Path("csv/").mkdir(parents=True, exist_ok=True)
        file_name = 'csv/' + category_name + '_articles_attributes_' + str(date.today()).replace('-', '') + '.csv'
        with open(file_name, mode='w', encoding="utf-8", newline='\n') as articles_file:
            csv_writer = csv.writer(articles_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["Nombre", "Precio", "IVA", "PVP", "Descuento", "Rating"])
            row = []
            for article in articles:
                row.append(article.name)
                row.append(article.price)
                row.append(article.no_iva)
                row.append(article.pvp)
                row.append(article.discount)
                row.append(article.rating)
                csv_writer.writerow(row)
                row = []

    def export_specifications_to_csv(self, category_name, articles):
        """
        Export articles' specifications from a given category to CSV
        :param category_name: category name
        :param articles: list of articles
        :return: create CSV file in sample/csv TODO JSON?
        """
        Path("csv/").mkdir(parents=True, exist_ok=True)
        file_name = 'csv/' + category_name + '_articles_specifications_' + str(date.today()).replace('-', '') + '.csv'
        with open(file_name, mode='w', encoding="utf-8", newline='\n') as articles_file:
            csv_writer = csv.writer(articles_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = []
            for article in articles:
                row.append(article.features)
                csv_writer.writerow(row)
                row = []
