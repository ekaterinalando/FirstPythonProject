import csv

with open('test.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('test_copy.csv', 'w', encoding='utf8') as csv_wfile:
        csv_writer = csv.writer(csv_wfile, delimiter='-', lineterminator='\n')

        for line in csv_reader:
            print(line)
