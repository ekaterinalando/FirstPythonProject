world = 'world'

sample_list = [123, 0.784, 'Hello', world, True, None, [1, 2, 3, 4, 5, ['One', 'Two', 'Three']]]

print(sample_list)
print(len(sample_list))
print(sample_list[:3])
print(sample_list[-1][2:4])
print(sample_list[-1][-1][0])

courses = ['Math', 'Physics', 'History', 'Programing', 'Literature']
numbers = [4, 5, 23, 1, 9, 84]

print(courses)

courses[0:2] = 'Biology'

print(courses)