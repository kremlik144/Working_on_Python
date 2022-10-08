''' 1. Задайте строку из набора чисел. Напишите программу, которая находит наибольшее и наименьшее число'''


# value = input('Введите значения через пробел: ').split()
# for i in value: i = int(i)
# print(f'Max value = {max(value)} / min value = {min(value)}')


'''2. Задайте 2 числа, найдите наименьший общий делитель этих чисел'''

# a, b = int(input('a = ')), int(input('b = '))
# flag = True

# for i in range(2, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         print(f'Наименьший общий делитель = {i}')
#         break

# else: print('Общего делителя нет !')