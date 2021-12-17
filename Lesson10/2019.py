import csv
import datetime

with open('csv_files/2019.csv', 'r', encoding='utf8') as survey_file:
    csv_reader = list(csv.DictReader(survey_file))
    keyword_lst = []
    for col in csv_reader[0]:
        keyword_lst.append(col)


def get_top_result(data, lines_nr, column_name):
    column_data = []
    result_list = []
    for line in data:
        column_data.append(line[column_name])

    while len(result_list) < int(lines_nr):
        for line in data:
            if line[column_name] == max(column_data) and line not in result_list:
                result_list.append(line)
                column_data.remove(line[column_name])
                break
    return result_list


def print_results(result_data):
    for line in result_data:
        for key, value in line.items():
            print(f'{key}: {value}, ', end='')
        print(' ')
    user_choice = input('Save results? y/n -->')
    if user_choice.lower() == 'y':
        save_results(result_data)
    print(' ')

def save_results(result_data):
    with open('survey_top.txt', 'a', encoding='utf8') as result_file:
        result_file.write(str(datetime.datetime.now()) + '\n')
        for line in result_data:
            for key, value in line.items():
                result_file.write(f'{key}: {value}, ')
            result_file.write('\n')


def main(data):
    while True:
        user_choice = input('1.Score\n2.GDP per capita\n3.Social support\n4.Healthy life expectancy\n'
                            '5.Freedom to make life choices\n6.Generosity\n7.Perceptions of corruption\n0.Exit')
        if user_choice == '0':
            print('Good bye')
            break
        elif user_choice not in '1234567':
            print('Choice is out of range')
            print('Try again')
            continue

        while True:
            try:
                user_top_nr = int(input('How many results?'))
            except:
                print('Please enter number')
            else:
                break

        if user_choice == '1':
            top = get_top_result(data, user_top_nr, 'Score')
            print_results(top)
        elif user_choice == '2':
            top = get_top_result(data, user_top_nr, 'GDP per capita')
            print_results(top)


main(csv_reader)

# result = get_top_result(csv_reader, 5, 'Healthy life expectancy')
# for line in result:
# print(line)
