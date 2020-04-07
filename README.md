# UOC-Scrapper

## Español
Práctica 1 de Tipología y ciclo de vida de los datos en la UOC por los alumnos Carlos Marcos y Víctor Colomé

### Instalación y Ejecución
Las librerías requeridas para que el scraper funcione son BeautifulSoup y UserAgent. Pueden ser instaladas con los comandos
    pip install pandas
    pip install requests
    pip install lxml
    pip install beautifulsoup4
    pip install fake-useragent

### Descripción
El scraper desarrollado se conecta a una web comercial de productos de electrónica de consumo y extrae de ella las categorías y artículos, junto con sus características y especificaciones. Dichos datos se almacenarán en formato CSV y se utilizarán más adelante para realizar un análisis estadístico sobre tendencias de algunas de ests características 

### Datos extraídos
Por cada artículo se almacenan los siguientes datos:

1. name
2. price
3. pvp
4. discount
5. no_iva
6. rating
7. features

## Inglés
Practise 1 of UOC subject "Tipología y ciclo de vida de los datos" by students Carlos Marcos and Víctor Colomé

### Installation and Execution
The required libraries for the scraper are BeautifulSoup and UserAgent. They can be installed with the following commands:
    pip install pandas
    pip install requests
    pip install lxml
    pip install beautifulsoup4
    pip install fake-useragent

### Description
This scraper retrieves all the articles from a well-known electronic retail website, alongwith their characteristics and features. These data are stored in CSV format and used later on for estatistical analysis purposes, aimed to discover temporal trends in the data.

### Retrieved data
Following data is retrieved (for every article):

1. name
2. price
3. pvp
4. discount
5. no_iva
6. rating
7. features
