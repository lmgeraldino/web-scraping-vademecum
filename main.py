from lib.medicamentos import MedicamentosScraper
import lib.utils as utils
import sys

scraper = MedicamentosScraper()
 
param = sys.argv[1]
data = scraper.scrap(param)
utils.to_csv('result/result.csv', data)