import csv

with open('../../Lesson10/csv_files/2019.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
