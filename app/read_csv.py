import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
                              # separador csv
    reader = csv.reader(csvfile, delimiter=',')
    # nombre de la primera columna (headers)
    header = next(reader)
    data = []
    for row in reader:
      # une a tuplas
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])