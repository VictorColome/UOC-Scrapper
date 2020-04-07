import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Constants
CSV_DIRECTORY = '../sample/csv/'


def store_image(img_name):
    if os.path.isfile(img_name):
        os.remove(img_name)  # Opt.: os.system("rm "+strFile)
    plt.savefig(img_name)


def box_plot_category(filename):
    """
    Create plot box from a given csv filename
    :param filename: filename
    """
    Path("img/").mkdir(parents=True, exist_ok=True)
    category_name = filename.split('_')[0]
    df = pd.read_csv(CSV_DIRECTORY + filename, header=None, names=["Name", "Price", "No IVA", "PVP", "Discount", "Rating"])
    print(df.describe())
    df.plot.box(grid='True')
    plt.title(category_name + ' boxplot')
    store_image('img/bp_{}.png'.format(category_name))


def historical_plot_category(category_name, init_date, end_date):
    Path("img/").mkdir(parents=True, exist_ok=True)
    prices = []
    for date in range(init_date, end_date + 1):
        filename = category_name + '_articles_attributes_' + str(date) + '.csv'
        df = pd.read_csv(CSV_DIRECTORY + filename, header=None, names=["Name", "Price", "No IVA", "PVP", "Discount", "Rating"])
        prices.append(df['Price'])
    pass


if __name__ == '__main__':
    # Se podría añadir una lista de categorías en un bucle simplemente
    category_name = 'adaptador-usb'  # Por ejemplo
    filename = 'adaptador-usb_articles_attributes_20200406.csv'  # Por ejemplo
    box_plot_category(filename)  # Cambiar por nombre del csv
    #historical_plot_category(category_name, 20200406, 20200407)
