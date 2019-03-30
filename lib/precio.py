import requests
from bs4 import BeautifulSoup

class PrecioScraper():

  PRECIO_URL = 'https://www.mscbs.gob.es/profesionales/nomenclator.do?metodo=verDetalle&prod='
  DATAFRAME_HEADER = ['NOMPROD', 'TIPOFAR', 'NOMGEN', 'LABOR', 'ESTADO', 'FECALTA', 'FECBAJA', 'APORTACION', 'PRINCACT',
                'PRECIO', 'MINPREC', 'CODAGR', 'NOMAGR', 'DIAGHOSP', 'TTOLARGADURADA', 'CNTRMEDICO', 'MEDHUERFANO']

  def __obtener_valor_celda__(self, celda):
    text = celda.get_text()
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('\r', '')
    text = text.replace(' ', '')
    return text

  def scrap(self, codigo_medicamento):
    result = []
    search_url = self.PRECIO_URL + str(codigo_medicamento)
    
    search_page = requests.get(search_url)
    search_soup = BeautifulSoup(search_page.text, 'html.parser')
    
    # Nos quedamos con la tabla que queremos obtener su información
    tabla = search_soup.find_all('table')

    # Cogemos los datos que queremos para luego guardarlo en csv
    for row in tabla:
      # Generamos un objeto con las celdas de datos de las tablas. Estas celdas
      # contendran la buqueda en el texto 'tabla_medicamentos' aquellos valores
      # que tengan como tag 'td'
      celda = row.find_all('td')
    
      # Guardamos cada valor en una variable
      nomprod = self.__obtener_valor_celda__(celda[1])
      tipofar = self.__obtener_valor_celda__(celda[2])
      nomgen = self.__obtener_valor_celda__(celda[3])
      labor = self.__obtener_valor_celda__(celda[4])
      estado = self.__obtener_valor_celda__(celda[5])
      fecalta = self.__obtener_valor_celda__(celda[6])
      fecbaja = self.__obtener_valor_celda__(celda[7])
      aportacion = self.__obtener_valor_celda__(celda[8])
      princact = self.__obtener_valor_celda__(celda[9])
      precio = self.__obtener_valor_celda__(celda[10])
      minprec = self.__obtener_valor_celda__(celda[11])
      codagr = self.__obtener_valor_celda__(celda[12])
      nomagr = self.__obtener_valor_celda__(celda[13])
      diaghosp = self.__obtener_valor_celda__(celda[14])
      ttolargadurada = self.__obtener_valor_celda__(celda[15])
      cntrmedico = self.__obtener_valor_celda__(celda[16])
      medhuerfano = self.__obtener_valor_celda__(celda[17])
  
      # Generamos el output en formato de lista para incorporar
      lista_res = [nomprod, tipofar, nomgen, labor, estado, fecalta, fecbaja, aportacion, princact, precio,
             minprec, codagr, nomagr, diaghosp, ttolargadurada, cntrmedico, medhuerfano]
      result.append(lista_res)

    return result
