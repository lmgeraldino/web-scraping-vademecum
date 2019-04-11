from lib.medicamentos import MedicamentosScraper
import lib.utils as utils
import sys

scraper = MedicamentosScraper()

medicamentos = ['Humira', 'Revlimid', 'Enbrel', 'MabThera', 'Rituxan', 'Herceptin', 'Eliquis', 'Avastin', 'Xarelto', 'Remicade', 'Januvia', 'Janumet', 'Lantus', 'Prevenar 13', 'Lyrica', 'Opdivo', 'Neulasta', 'Harvoni', 'Tecfidera', 'Stelara', 'Victoza', 'Keytruda', 'Copaxone', 'Genvoya', 'Seretide', 'Advair', 'Epclusa', 'Lucentis', 'NovoRapid', 'Gilenya', 'Botox', 'Truvada', 'Ibrance', 'Simvastatina', 'Aspirina', 'Omeprazol', 'Lexotiroxina sódica', 'Ramipril', 'Amlodipina', 'Paracetamol', 'Atorvastatina', 'Salbutamol', 'Lansoprazol', 'Hidrocloruro de metformina', 'Colecalciferol', 'Bisoprolol fumarato', 'Co-codamol', 'Bendroflumetiazida', 'Citalopram hidrobromuro', 'Amoxicilina', 'Furosemida', 'Amitriptilina hidrocloruro', 'Warfarina sódica', 'Paracetamol', 'Ibuprofeno', 'Lorazepan', 'Prozac', 'Trankimazin', 'Apiretal', 'Clexane', 'Nolotil', 'Adiro', 'Enantyum', 'Sintrom', 'Eutirox', 'Ventolin', 'Orfidal']

result = []
result.append(scraper.dataframe_header)

for index, medicamento in enumerate(medicamentos, start = 1):
  print('Procesando medicamento:',medicamento, '(', index,'de', len(medicamentos),')') 
  #param = sys.argv[1]
  result = result +  scraper.scrap(medicamento)

utils.to_csv('result/result.csv', result)
