import csv
from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class DataExporter:

    def export_articles_to_csv(self, category_name, articles):
        self.export_attributes_to_csv(category_name, articles)
        self.export_specifications_to_csv(category_name, articles)

    def export_attributes_to_csv(self, category_name, articles):
        Path("csv/").mkdir(parents=True, exist_ok=True)
        file_name = 'csv/' + category_name + '_articles_attributes_' + str(date.today()).replace('-', '') + '.csv'
        with open(file_name, mode='w', encoding="utf-8", newline='\n') as articles_file:
            csv_writer = csv.writer(articles_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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
        Path("csv/").mkdir(parents=True, exist_ok=True)
        file_name = 'csv/' + category_name + '_articles_specifications_' + str(date.today()).replace('-', '') + '.csv'
        with open(file_name, mode='w', encoding="utf-8", newline='\n') as articles_file:
            csv_writer = csv.writer(articles_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = []
            for article in articles:
                row.append(article.features)
                csv_writer.writerow(row)
                row = []

    # TODO: Improve. Create new class?
    def import_attributes_from_csv(self, filename):
        Path("img/").mkdir(parents=True, exist_ok=True)
        df = pd.read_csv(filename, header=None, names=["Name", "Price", "No IVA", "PVP", "Discount", "Rating"])
        print(df.describe())
        df.plot.box(grid='True')
        plt.savefig('img/foo.png')
