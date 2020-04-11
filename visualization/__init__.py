import os
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

# Constants
CSV_DIRECTORY = '../sample/csv/'
CSV_COLS = ["Name", "Price", "No IVA", "PVP", "Discount", "Rating"]


def store_image(img_name):
    """
    Store image
    :param img_name:
    :return:
    """
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
    df = pd.read_csv(CSV_DIRECTORY + filename)
    print(df.describe())
    df.plot.box(grid=True)
    plt.title(category_name + ' boxplot')
    store_image('img/bp_{}.png'.format(category_name))


def historical_plot_category(category_name, col_2_analyse, init_date, end_date):
    """
    Create linear plot with the historical data of a given column
    :param category_name: Category of the articles
    :param col_2_analyse: Column to analyse
    :param init_date: Initial date
    :param end_date: Final date
    """
    Path("img/").mkdir(parents=True, exist_ok=True)
    dfs = []
    for date in range(init_date, end_date + 1):
        str_date = str(date)
        df = pd.read_csv(CSV_DIRECTORY + category_name + '_articles_attributes_' + str_date + '.csv')
        df['Date'] = datetime(year=int(str_date[0:4]), month=int(str_date[4:6]), day=int(str_date[6:8]))
        df['Date'] = pd.to_datetime(df['Date'])
        dfs.append(df.loc[:, ['Name', col_2_analyse, 'Date']])
    df_prices = pd.concat(dfs)
    print(df_prices)
    df_prices.to_csv('../sample/csv/all_data_'+str(init_date)+'_to_'+str(end_date)+'.csv', index=False, header=True)

    # Vamos a quedarnos únicamente con aquellos artículos cuyos valores cambien en algo, ya que entendemos que
    # esos serán los casos más interesantes que nos interesa resaltar
    names = []
    for name in df_prices['Name'].unique():
        if not content_is_identical(df_prices.loc[df_prices['Name'] == name][col_2_analyse]):
            names.append(name)
    df_prices_variations = df_prices[df_prices['Name'].isin(names)]

#   Una forma algo más "pythonizada" de hacerlo  :-)
#    df_prices_variations = df_prices[df_prices.groupby(['Name', col_2_analyse])['Date'].transform('nunique') > 1]
    df_prices_variations.to_csv('../sample/csv/just_var_'+str(init_date)+'_to_'+str(end_date)+'.csv', index=False, header=True)

    print("Start ploting, might take a while...")

    fig, ax = plt.subplots(1, 1)
    ax.xaxis.set_major_formatter(DateFormatter("%d-%m-%Y"))
    df_prices_variations.groupby('Name').plot(x='Date', y=col_2_analyse, ax=ax)
    ax.get_legend().remove()
    plt.xlabel('Date')
    plt.ylabel(col_2_analyse)
    store_image('img/historical_{}.png'.format(category_name))
    print("Done")


def content_is_identical(iterator):
    """
    Checks whether the content of the given iterator is identical
    :param iterator: iterator
    :return: boolean
    """
    return len(set(iterator)) <= 1


if __name__ == '__main__':
    # Se podría añadir una lista de categorías en un bucle simplemente
    category_name = 'adaptador-usb'  # Por ejemplo
    filename = 'adaptador-usb_articles_attributes_20200406.csv'  # Por ejemplo
    box_plot_category(filename)
    historical_plot_category(category_name, 'Rating', 20200406, 20200410)  # Elegir las fechas y la col que se quieran
