import csv

def to_csv(filename, data):
  with open(filename, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    for row in data:
      writer.writerow(row)