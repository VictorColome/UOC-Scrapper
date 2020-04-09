import os
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Constants
CSV_DIRECTORY = '../sample/csv/'
CSV_COLS = ["Name", "Price", "No IVA", "PVP", "Discount", "Rating"]


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
    df = pd.read_csv(CSV_DIRECTORY + filename, header=None, names=CSV_COLS)
    print(df.describe())
    df.plot.box(grid=True)
    plt.title(category_name + ' boxplot')
    store_image('img/bp_{}.png'.format(category_name))


def historical_plot_category(category_name, init_date, end_date):
    Path("img/").mkdir(parents=True, exist_ok=True)
    """
    df_prices = pd.DataFrame(columns=['Name'])
    for date in range(init_date, end_date + 1):
        filename = category_name + '_articles_attributes_' + str(date) + '.csv'
        df = pd.read_csv(CSV_DIRECTORY + filename, header=None, names=CSV_COLS)
        df1 = df[['Name', 'Price']]
        df1 = df1.rename(columns={'Price': str(date)})
        df_prices = df_prices.merge(df1, on='Name', how='outer')
    df_prices.set_index('Name', inplace=True, drop=True)
    print(df_prices)
    """
    dfs = []
    col_2_analyse = 'Rating'  # 'Price'
    for date in range(init_date, end_date + 1):
        str_date = str(date)
        df = pd.read_csv(CSV_DIRECTORY + category_name + '_articles_attributes_' + str_date + '.csv',
                       header=None, names=CSV_COLS)
        df['Date'] = datetime(year=int(str_date[0:4]), month=int(str_date[4:6]), day=int(str_date[6:8]))
        df['Date'] = pd.to_datetime(df['Date'])
        dfs.append(df.loc[:, ['Name', col_2_analyse, 'Date']])
    df_prices = pd.concat(dfs)
    print(df_prices)

    print("Start ploting, might take a while...")
    fig, ax = plt.subplots(1, 1)
    df_prices.groupby('Name').plot(x='Date', y=col_2_analyse, ax=ax)
    ax.get_legend().remove()
    plt.xlabel('Date')
    plt.ylabel(col_2_analyse)
    store_image('img/historical_{}.png'.format(category_name))
    print("Done")


if __name__ == '__main__':
    # Se podría añadir una lista de categorías en un bucle simplemente
    category_name = 'adaptador-usb'  # Por ejemplo
    filename = 'adaptador-usb_articles_attributes_20200406.csv'  # Por ejemplo
    box_plot_category(filename)
    historical_plot_category(category_name, 20200406, 20200409)  # Elegir las fechas que se quieran
