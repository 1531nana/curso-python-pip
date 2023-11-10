import read_csv

data = read_csv.read_csv('./app/data.csv')
print(data[0])
dict = {}
for item, value in data.items():
  if 'population' in item:
    dict[item.replace('population', '')] = sum(value)
print(dict)