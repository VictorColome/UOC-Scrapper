import csv
from datetime import date
from pathlib import Path


class DataExporter:

    def export_articles_to_csv(self, articles):
        self.export_attributes_to_csv(articles)
        self.export_specifications_to_csv(articles)

    def export_attributes_to_csv(self, articles):
        Path("csv/").mkdir(parents=True, exist_ok=True)
        file_name = 'csv/articles_attributes_' + str(date.today()).replace('-', '') + '.csv'
        with open(file_name, mode='w') as articles_file:
            csv_writer = csv.writer(articles_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = []
            for article in articles:
                row.append(article.name)
                row.append(article.price)
                row.append(article.no_iva)
                row.append(article.pvp)
                row.append(article.discount)
                csv_writer.writerow(row)
                row = []

    def export_specifications_to_csv(self, articles):
        pass