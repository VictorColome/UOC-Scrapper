# UOC-Scrapper

## Español
Práctica 1 de Tipología y ciclo de vida de los datos en la UOC por los alumnos Carlos Marcos y Víctor Colomé

### Instalación y Ejecución
Este proyecto usa diferentes librerías, que pueden ser instaladas fácilmente ejecutando el siguiente comando en el 
directorio raíz:
    
    pip install -r requirements.txt

[FALTA LA PARTE DE EJECUCIÓN]

### Descripción
El scraper desarrollado se conecta a una web comercial de productos de electrónica de consumo y extrae de ella las 
categorías y artículos, junto con sus características y especificaciones. Dichos datos se almacenarán en formato CSV y 
se utilizarán más adelante para realizar un análisis estadístico sobre tendencias de algunas de ests características 

### Datos extraídos
Por cada artículo se almacenan los siguientes datos:

1. name
2. price
3. pvp
4. discount
5. no_iva
6. rating
7. features

### Estructura del código
Dentro del proyecto hay 3 carpetas principales:
* sample. Contiene la mayoría de las clases necesarias para el scraper. Es el core del proyecto. Contenido:
    * *csv*. Este directorio es donde se irán guardando los CSVs generados por el scraper
    * *img*. Este directorio contiene las imágenes utilizadas durante el desarrollo del scraper
    * __init__.py Este fichero es el "lanzador" del proyecto, y el que se ejecuta en primer lugar. Contiene la llamada 
    inicial al scraper para que empiece al escaneo.
    * article.py. Este fichero contiene la definición de la clase Article, la cual es el ítem fundamental de información
     de esta práctica
    * data_exporter.py. Este fichero contiene las utilidades de guardado de la estructura de objetos en ficheros CSV, 
    tanto para artículos como para sus objetos contenidos
    * feature.py Este fichero contiene la definición de la clase Feature, la cual forma parte de un Article y almacena 
    las características y especificaciones de cada artículo
    * scraper.py. Esta es la clase principal del proyecto: contiene las definiciones de la clase Scraper y la clase 
    Categoría. Esta última es una agrupación de artículos y la primera contiene los métodos que escanean el sitio web: 
    primero se escanea el XML sitemap_categories para averiguar las categorías y después se va recorriendo cada 
    categoría escaneando los artículos que la conforman. 
* test. Contiene 2 ficheros:
    * test_data_exporter.py. Este fichero genera objetos dummy para poder probar el guardado a disco de las clases 
    descritas en la carpeta sample
    * test_scraper.py. Este fichero permite hacer pruebas sobre las clases de sample
* [PONER AQUI LA DE LAS GRAFICAS]

## English
Practise 1 of UOC subject "Tipología y ciclo de vida de los datos" by students Carlos Marcos and Víctor Colomé

### Installation and Execution
This project uses various libraries, which can be easily installed running the following command in the root directory:

    pip install -r requirements.txt
    
[FALTA LA PARTE DE EJECUCIÓN]

### Description
This scraper retrieves all the articles from a well-known electronic retail website, alongwith their characteristics and
 features. These data are stored in CSV format and used later on for estatistical analysis purposes, aimed to discover 
 temporal trends in the data.

### Retrieved data
Following data is retrieved (for every article):

1. name
2. price
3. pvp
4. discount
5. no_iva
6. rating
7. features

### Project Structure
The project has 3 main folders::
* sample. It contains most of the classes needed for running the scraper. This is the core of the project. Content:
    * *csv*. This is where the generated CSV are stored.
    * *img*. This folder contains the images used during the development
    * __init__.py. This is the "launcher" of the project. This is the first to be executed and contains the initial call
     to the scraper so it can perform the scanning.
    * article.py. This file contains the definition of the "Article" class, which is the fundamental item of information
     for this project.
    * data_exporter.py. This file contains the utilities for saving the objects structure in CSV format, for articles 
    and their structures within.
    * feature.py. This file contains the definition of "Feature" class, which is part of an article and stores both its 
    characteristics and specifications. 
    * scraper.py. This is the main class of the project: it contains the definitions of Scraper and Category classes. 
    The last one is a set of articles and the first one contains the methods in charge of scanning the website: first 
    the XML sitemap_categories.xml is scanned and the list of categories retrieved. Then, iterating over that list, 
    each one of the articles is scraped from the website. 
* test. It contains 2 files:
    * test_data_exporter.py. This file generates dummy objects that can be used to test the classes of sample folder for
     saving data into CSV files.
    * test_scraper.py. This file allows the testing of sample folder classes
* [PONER AQUI LA DE LAS GRAFICAS]
