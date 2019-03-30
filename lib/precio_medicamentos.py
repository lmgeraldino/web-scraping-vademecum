# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:38:58 2019

@author: Sergi Ramirez Mitjans

Bibiliografia:
https://living-sun.com/es/python/699355-extracting-table-info-using-beautifulsoup-bs4-python.html
"""
# -----------------------------------------------------------------------------
# Importamos las librerias necesarias
## Paquetes relacionados con las rutas
import os

# Paquetes relacionados con la lectura y escritura de los csv
import csv

# Paquetes relacionados con el scraping
import requests
from bs4 import BeautifulSoup

# Paquetes relacionados con el tratamiento de los datos
import re
import pandas as pd

# Paquetes relacionados con el control del tiempo del proceso
import time
from time import sleep
import progressbar
# from console_progressbar import ProgressBar

# -----------------------------------------------------------------------------
# INPUTS:
## Generamos la lista donde introduciremos los datos scrapeados
header_lista = ['CODNAC', 'NOMPROD', 'TIPOFAR', 'NOMGEN', 'LABOR', 'ESTADO', 'FECALTA', 'FECBAJA', 'APORTACION', 'PRINCACT',
                'PRECIO', 'MINPREC', 'CODAGR', 'NOMAGR', 'DIAGHOSP', 'TTOLARGADURADA', 'CNTRMEDICO', 'MEDHUERFANO']
lista = []
lista.append(header_lista)

## Generamos la URL de la cuál queremos hacer las consultas
url = 'https://www.mscbs.gob.es/profesionales/nomenclator.do?metodo=verDetalle&prod='

## Creamos la dirección donde guardamos el output
path = 'C:/Users/User/Desktop/'
archivo = 'input2.csv' 
file_in = path + archivo

output = "precios_medicamentos.csv"
file_out = path + output

# -----------------------------------------------------------------------------
# CARGA DE DATOS (Solo se usara para eld desarrollo pero no para cuando tengamos
# el archivo csv):
codigos = pd.read_csv(file_in)
codigos = codigos.values.tolist()
codigos = [item[0] for item in codigos]
# codigos = codigos[:round(len(codigos)/2)]

# -----------------------------------------------------------------------------
# ## Generamos los últimos parámetros
nfinal = len(codigos)
nparcial = 1

# -----------------------------------------------------------------------------
# PROCESO:
# printProgressBar(0, nfinal, prefix = 'Progress:', suffix = 'Complete', length = 50)
inicio = time.time()
## Realizamos el bucle para cada uno de los medicamentos a buscar
for i in range(0, len(codigos)):
    # Generamos la url para descargar
    url_descargar = url + str(codigos[i])
    
    # Nos conectamos a la web que hemos generado
    r = requests.get(url_descargar)
    data = r.text
    
    # Generamos el texto que queremos scrapear en lmxl
    soup = BeautifulSoup(data, 'lxml')
    
    # Nos quedamos con la tabla que queremos obtener su información
    tabla = soup.findAll('table')
    
    # Cogemos los datos que queremos para luego guardarlo en csv
    for row in tabla:
        # Generamos un objeto con las celdas de datos de las tablas. Estas celdas
        # contendran la buqueda en el texto 'tabla_medicamentos' aquellos valores
        # que tengan como tag 'td'
        celda = row.find_all('td')
        
        # Guardamos cada valor en una variable
        ## CODNAC:
        val1 = celda[0].get_text()
        val1 = val1.replace('\n', '')
        val1 = val1.replace('\t', '')
        val1 = val1.replace('\r', '')
        val1 = val1.replace(' ', '')
        ## NOMPROD:
        val2 = celda[1].get_text()
        val2 = val2.replace('\n', '')
        val2 = val2.replace('\t', '')
        val2 = val2.replace('\r', '')
        ## TIPOFAR:
        val3 = celda[2].get_text()
        val3 = val3.replace('\t', '')
        val3 = val3.replace('\r', '')
        val3 = val3.replace('\n', '')
        ## NOMGEN:
        val4 = celda[3].get_text()
        val4 = val4.replace('\t', '')
        val4 = val4.replace('\r', '')
        val4 = val4.replace('\n', '')
        ## LABOR:
        val5 = celda[4].get_text()
        val5 = val5.replace('\t', '')
        val5 = val5.replace('\r', '')
        val5 = val5.replace('\n', '')
        ## ESTADO:
        val6 = celda[5].get_text()
        val6 = val6.replace('\t', '')
        val6 = val6.replace('\r', '')
        val6 = val6.replace('\n', '')
        ## FECALTA:
        val7 = celda[6].get_text()
        val7 = val7.replace('\t', '')
        val7 = val7.replace('\r', '')
        val7 = val7.replace('\n', '')
        ## FECBAJA:
        val8 = celda[7].get_text()
        val8 = val8.replace('\t', '')
        val8 = val8.replace('\r', '')
        val8 = val8.replace('\n', '')
        ## APORTACION:
        val9 = celda[8].get_text()
        val9 = val9.replace('\t', '')
        val9 = val9.replace('\r', '')
        val9 = val9.replace('\n', '')
        ## PRINCACT:
        val10 = celda[9].get_text()
        val10 = val10.replace('\t', '')
        val10 = val10.replace('\r', '')
        val10 = val10.replace('\n', '')
        ## PRECIO:
        val11 = celda[10].get_text()
        val11 = val11.replace('\t', '')
        val11 = val11.replace('\r', '')
        val11 = val11.replace('\n', '')
        ## MINPREC:
        val12 = celda[11].get_text()
        val12 = val12.replace('\t', '')
        val12 = val12.replace('\r', '')
        val12 = val12.replace('\n', '')
        ## CODAGR:
        val13 = celda[12].get_text()
        val13 = val13.replace('\t', '')
        val13 = val13.replace('\r', '')
        val13 = val13.replace('\n', '')
        ## NOMAGR:
        val14 = celda[13].get_text()
        val14 = val14.replace('\t', '')
        val14 = val14.replace('\r', '')
        val14 = val14.replace('\n', '')
        ## DIAGHOSP:
        val15 = celda[14].get_text()
        val15 = val15.replace('\t', '')
        val15 = val15.replace('\r', '')
        val15 = val15.replace('\n', '')
        ## TTOLARGADURADA:
        val16 = celda[15].get_text()
        val16 = val16.replace('\t', '')
        val16 = val16.replace('\r', '')
        val16 = val16.replace('\n', '')
        ## CNTRMEDICO:
        val17 = celda[16].get_text()
        val17 = val17.replace('\t', '')
        val17 = val17.replace('\r', '')
        val17 = val17.replace('\n', '')
        ## MEDHUERFANO:
        val18 = celda[17].get_text()
        val18 = val18.replace('\t', '')
        val18 = val18.replace('\r', '')
        val18 = val18.replace('\n', '')
        
    # Generamos el output en formato de lista para incorporar
    lista_res = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11,
             val12, val13, val14, val15, val16, val17, val18] 

    # Incorporamos los valores de resultado en la lista general 
    lista.append(lista_res)
    
    # Imprimimos el porcentaje de completado del sistema
    # printProgressBar(i + 1, nfinal, prefix = 'Progress:', suffix = 'Complete', length = 50)

    # Vamos a realizar un sleep (un parón) cuando llevemos 300 registros descargados
    segundos = 0.5
    if (i % 300 == 0 and i != 0):
        print("\nCodigo número", i, "- Hacemos una pausa de ", segundos, " segundos.\n")
        sleep(segundos)

# Comprobamos el tiempo de ejecución
final = time.time()

# Imprimimos el tiempo que ha transcurrido
print ('\nHa transcurrido ', (final - inicio)/60, 'minutos.\n')

# -----------------------------------------------------------------------------
# GUARDAR EL CSV
## Al final guardamos el csv (NO FUNCIONA)
#with open(file_out, 'w', newline='') as csvFile:
#  writer = csv.writer(csvFile)
#  for val in lista:
#  	writer.writerow(val)