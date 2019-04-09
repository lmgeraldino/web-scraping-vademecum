import requests
from bs4 import BeautifulSoup

class PrecioScraper():

  PRECIO_URL = 'https://www.mscbs.gob.es/profesionales/nomenclator.do?metodo=verDetalle&prod='
  DATAFRAME_HEADER = ['Tipo', 'Generico', 'Laboratorio', 'Estado', 'Fecha alta', 'Fecha baja', 'Aportacion beneficiario', 'Principio activo',
                'PVP', 'Precio referencia', 'Menor precio agrupacion homogenea', 'Agrupacion homogenea', 'Diasnostico hospitalario', 'Tratamiento larga duracion', 'Control medico', 'Huerfano']

  def __obtener_valor_celda__(self, celda):
    text = celda.get_text()
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('\r', ' ')
    text = text.strip()
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
      tipofar = self.__obtener_valor_celda__(celda[2])
      nomgen = self.__obtener_valor_celda__(celda[3])
      labor = self.__obtener_valor_celda__(celda[4])
      estado = self.__obtener_valor_celda__(celda[5])
      fecalta = self.__obtener_valor_celda__(celda[6])
      fecbaja = self.__obtener_valor_celda__(celda[7])
      aportacion = self.__obtener_valor_celda__(celda[8])
      princact = self.__obtener_valor_celda__(celda[9])
      pvp = self.__obtener_valor_celda__(celda[10])
      precref = self.__obtener_valor_celda__(celda[11])
      minprec = self.__obtener_valor_celda__(celda[12])
      agrhom = self.__obtener_valor_celda__(celda[13])
      diaghosp = self.__obtener_valor_celda__(celda[14])
      ttolargadurada = self.__obtener_valor_celda__(celda[15])
      cntrmedico = self.__obtener_valor_celda__(celda[16])
      medhuerfano = self.__obtener_valor_celda__(celda[17])
  
      # Generamos el output en formato de lista para incorporar
      lista_res = [tipofar, nomgen, labor, estado, fecalta, fecbaja, aportacion, princact, pvp,
             precref, minprec, agrhom, agrhom, diaghosp, ttolargadurada, cntrmedico, medhuerfano]
      result.append(lista_res)

    return result
