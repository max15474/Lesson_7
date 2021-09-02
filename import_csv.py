import csv

car_data = [['brand', 'price', 'year'], ['Volvo', 1.5, 2017], ['Lada', 0.5, 2018], ['Audi', 2.0, 2018]]

with open('example.csv', 'w') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(car_data)
print('Writing complete!')