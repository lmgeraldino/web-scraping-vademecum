# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:38:58 2019

@author: Sergi Ramirez Mitjans

Bibiliografia:
https://living-sun.com/es/python/699355-extracting-table-info-using-beautifulsoup-bs4-python.html
"""

# Importamos las librerias necesarias
import os

import csv
import requests
from bs4 import BeautifulSoup

import re
import pandas as pd

# -----------------------------------------------------------------------------
# INPUTS:
## Generamos la lista donde introduciremos los datos scrapeados
header_lista = ['CODNAC', 'NOMPROD', 'TIPOFAR', 'NOMGEN', 'LABOR', 'ESTADO', 'FECALTA', 'FECBAJA', 'APORTACION', 'PRINCACT',
                'PRECIO', 'MINPREC', 'CODAGR', 'NOMAGR', 'DIAGHOSP', 'TTOLARADURADA', 'CNTRMEDICO', 'MEDHUERFANO']
lista = []
lista.append(header_lista)

## Generamos la URL de la cuál queremos hacer las consultas
url = 'https://www.mscbs.gob.es/profesionales/nomenclator.do?metodo=verDetalle&prod='

## Creamos la dirección donde guardamos el output
path = 'C:/Users/SergiR/Desktop/'
archivo = 'input.csv' 
file_in = path + archivo

output = "precios_medicamentos.csv"
file_out = path + output

# -----------------------------------------------------------------------------
# CARGA DE DATOS (Solo se usara para eld desarrollo pero no para cuando tengamos
# el archivo csv):
codigos = pd.read_csv(file_in)
codigos = codigos.values
codigos = codigos.tolist()

# Quitamos los [ ] de la lista
codigos = [int(c.replace("[ | ]", "")) for c in codigos]
re.sub("[ ]", codigos)

# -----------------------------------------------------------------------------
# PROCESO: 
## Realizamos el bucle para cada uno de los medicamentos a buscar

for codigo in codigos[0]:
    url_descargar = url + codigos



codigos = '400011'
print (codigos, ":", url_descargar)


# -----------------------------------------------------------------------------
# Nos conectamos a la web que hemos generado
r = requests.get(url_descargar)    
data = r.text

# Generamos el texto que queremos scrapear en lxml
soup = BeautifulSoup(data, 'lxml')

# Nos quedamos con la tabla que queremos obtener su información
tabla_medicamento = soup.findAll("table")

for row in tabla_medicamento:
    # Nos quedamos con todos los valores de la tabla
    cells = row.find_all('td')
    
    # Guadamos cada valor en una variable
    val1 = cells[0].get_text()
    val2 = cells[1].get_text()
    val3 = cells[2].get_text()
    val4 = cells[3].get_text()
    val5 = cells[4].get_text()
    val6 = cells[5].get_text()
    val7 = cells[6].get_text()
    val8 = cells[7].get_text()
    val9 = cells[8].get_text()
    val10 = cells[9].get_text()
    val11 = cells[10].get_text()
    val12 = cells[11].get_text()
    val13 = cells[12].get_text()
    val14 = cells[13].get_text()
    val15 = cells[14].get_text()
    val16 = cells[15].get_text()
    val17 = cells[16].get_text()
    val18 = cells[17].get_text()

    # Generamos la lista de resultados
    lista_resultados = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10,
                        val11, val12, val13, val14, val15, val16, val17, val18]


lista.append(lista_resultados)


# Al final guardamos el csv (NO FUNCIONA)


with open(file_out, 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  for val in lista:
  	writer.writerow(val)