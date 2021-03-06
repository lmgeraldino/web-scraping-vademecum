import requests
from bs4 import BeautifulSoup
from .precio import PrecioScraper
from .utils import get_random_user_agent

class MedicamentosScraper():
  
  VADEMECUM_URL = 'https://www.vademecum.es/'
  DAFAFRAME_HEADER = ['Medicamento', 'URL', 'Presentación', 'Código Nacional']

  def __init__(self):
    self.data = []
    self.precio_scraper = PrecioScraper()
    self.dataframe_header = ['Medicamento', 'URL', 'Presentación', 'Código Nacional'] + self.precio_scraper.DATAFRAME_HEADER

  def __is_facturable_sns(self, presentacion):
    for elem in presentacion.find_all('li'):
      if 'Facturable SNS' in elem.text:
        return 'SI' in elem.text
    return False

  def __get_codigo_nacional(self, presentacion):
    for elem in presentacion.find_all('li'):
      if 'Código Nacional' in elem.text:
        return elem.find('span').text.strip()

  def __get_titulo(self, presentacion): 
    return presentacion.find('li', {'class':'title'}).text.strip()

  def get_dataframe_header(self):
    return DATAFRAME_HEADER + self.precio_scraper.DATAFRAME_HEADER

  def scrap(self, medicamento):
    #Se define la URL de búsqueda del medicamento
    search_url = self.VADEMECUM_URL + 'buscar?q=' + medicamento

    #Se realiza la petición con un User-Agent aleatorio para evitar bloqueos
    search_page = requests.get(search_url, headers = {'User-Agent': get_random_user_agent()})
    search_soup = BeautifulSoup(search_page.content, 'html.parser')

    #Se buscan los resultados del listado que sean medicamentos
    medicamentos = search_soup.find_all('a', {'title':'medicamento'})

    resultList = []

    for m in medicamentos:
      medicamento_url = self.VADEMECUM_URL + m['href']

      #Se realiza una nueva petición a la URL de detalle del medicamento para recopilar la información necesaria
      detail_page = requests.get(medicamento_url)
      detail_soup = BeautifulSoup(detail_page.content, 'html.parser')
      presentaciones = detail_soup.find_all('ul', {'class':'pricing-table'})
      for presentacion in presentaciones:
        if self.__is_facturable_sns(presentacion):
          codigo_nacional = self.__get_codigo_nacional(presentacion)
          #Si tiene código nacional y el medicamento está subvencionado, se busca en la web del ministerio
          precios = self.precio_scraper.scrap(codigo_nacional)
          for precio in precios:
            #Se guarda un registro por presentación y precio del medicamento
            resultList.append([m.text.strip(), medicamento_url, self.__get_titulo(presentacion), codigo_nacional] + precio)

    return resultList
