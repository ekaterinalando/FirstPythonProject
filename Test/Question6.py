#6 *Написать программу, которая для произвольного списка находит число / числа,
# наиболее часто встречающееся в данном списке и возвращающее их также в виде списка.
#Примеры:
#[1, 2, 3, 4, 7, 9, 9] → [9]
#[1, 2, 4, 6, 4, 6] → [4,6]

test_list = [1, 2, 3, 4, 4, 5, 5, 5, 8, 8, 8, 9]
empty_dict = {}
for num in test_list:
    empty_dict[num] = test_list.count(num)

result_list = []
for x in empty_dict.keys():
    if empty_dict[x] == max(empty_dict.values()):
        result_list.append(x)

print(result_list)