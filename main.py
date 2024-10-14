# name, age, is_student = 'Dmitry', 31, True
# print(name, age, is_student)
#
# print (f'{name}, {age}, {is_student}, {type(name)}, {type(age)}, {type(is_student)}')
#
# name1: str = 'Dmitry'
# print(name1)

# name: str = "Denis"; print(name, type(name))
# name: str = 'Urban'
# print(name)

# date_of_birth = 'November 1992'

homeworks_count: int = 12
hours_count: float = 1.5
name_of_the_course: str = 'Python'
time_for_one_task: int = hours_count / homeworks_count
print(f'Курс: {name_of_the_course}, всего задач: {homeworks_count}, затрачено часов: {hours_count}, среднее время выполнения: {time_for_one_task} часа.')