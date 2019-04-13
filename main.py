from lib.medicamentos import MedicamentosScraper
from lib.precio import PrecioScraper
import lib.utils as utils

scraper = MedicamentosScraper()

medicamentos = ['Humira', 'Revlimid', 'Enbrel', 'MabThera', 'Rituxan', 'Herceptin', 'Eliquis', 'Avastin', 'Xarelto', 'Remicade', 'Januvia', 'Janumet', 'Lantus', 'Prevenar 13', 'Lyrica', 'Opdivo', 'Neulasta', 'Harvoni', 'Tecfidera', 'Stelara', 'Victoza', 'Keytruda', 'Copaxone', 'Genvoya', 'Seretide', 'Advair', 'Epclusa', 'Lucentis', 'NovoRapid', 'Gilenya', 'Botox', 'Truvada', 'Ibrance', 'Simvastatina', 'Aspirina', 'Omeprazol', 'Lexotiroxina sódica', 'Ramipril', 'Amlodipina', 'Paracetamol', 'Atorvastatina', 'Salbutamol', 'Lansoprazol', 'Hidrocloruro de metformina', 'Colecalciferol', 'Bisoprolol fumarato', 'Co-codamol', 'Bendroflumetiazida', 'Citalopram hidrobromuro', 'Amoxicilina', 'Furosemida', 'Amitriptilina hidrocloruro', 'Warfarina sódica', 'Paracetamol', 'Ibuprofeno', 'Lorazepan', 'Prozac', 'Trankimazin', 'Apiretal', 'Clexane', 'Nolotil', 'Adiro', 'Enantyum', 'Sintrom', 'Eutirox', 'Ventolin', 'Orfidal']

print('------------------------------------')
print('robots.txt Vademecum')
print('------------------------------------')
print(utils.get_robots_status_code(MedicamentosScraper.VADEMECUM_URL))
print('------------------------------------')
print('robots.txt MSCBS')
print('------------------------------------')
print(utils.get_robots_status_code(PrecioScraper.BASE_URL))
print('------------------------------------')

result = []
result.append(scraper.dataframe_header)

print('Procesando', len(medicamentos), 'medicamentos...')
print('------------------------------------')
for index, medicamento in enumerate(medicamentos, start = 1):
  print(index, '-', medicamento) 
  result = result +  scraper.scrap(medicamento)

utils.to_csv('result/result.csv', result)
