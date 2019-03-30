import requests
import csv
import sys

from bs4 import BeautifulSoup

def is_facturable_sns(presentacion):
  for elem in presentacion.find_all('li'):
    if 'Facturable SNS' in elem.text:
      return True
  return False

def get_codigo_nacional(presentacion):
  for elem in presentacion.find_all('li'):
    if 'Código Nacional' in elem.text:
      return elem.find('span').text.strip()

def get_titulo(presentacion): 
  return presentacion.find('li', {'class':'title'}).text.strip()
    
param = sys.argv[1]
vademecum_url = "https://www.vademecum.es"
search_url = vademecum_url + "/buscar?q=" + param

page = requests.get(search_url)
soup = BeautifulSoup(page.content, "html.parser")

medicamentos = soup.find_all('a', {'title':'medicamento'})

resultList = []
resultList.append(["Medicamento", "URL", "Presentación", "Código Nacional"])

for m in medicamentos:
  detail_page = requests.get(vademecum_url + m['href'])
  detail_soup = BeautifulSoup(detail_page.content, "html.parser")
  presentaciones = detail_soup.find_all('ul', {'class':'pricing-table'})
  for presentacion in presentaciones:
  	if is_facturable_sns(presentacion):
  	  resultList.append([m.text.strip(), vademecum_url + m['href'], get_titulo(presentacion), get_codigo_nacional(presentacion)])

with open('result.csv', 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  for resultItem in resultList:
    writer.writerow(resultItem)