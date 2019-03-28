import requests
import csv
import sys

from bs4 import BeautifulSoup

param = sys.argv[1]
vademecum_url = "https://www.vademecum.es/buscar?q=" + param

page = requests.get(vademecum_url)
soup = BeautifulSoup(page.content, "html.parser")

medicamentos = soup.find_all('a', {'title':'medicamento'})

resultList = []
resultList.append(["Medicamento", "URL"])

for m in medicamentos:
  resultList.append([m.text.strip(), m['href']])

with open('result.csv', 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  for resultItem in resultList:
  	writer.writerow(resultItem)