''' 1. напишите программу, которая принимает на вход число N и выводит последовательность из 
N членов 
Пример: N = 5 ; (1, -3, 9, -27, 81)'''


# def func_1(x):
#     for i in range(x):
#         print((-3)**i, end = ' ')

# number = int(input('Введите число N: '))
# func_1(number)


''' 2. Для натурального n создать список, состоящий из элементов последо-и 3n + 1
Для n=6 это [4, 7, 10, 13, 16, 19]'''


# def func_2(count_):
#     list_number = []
#     for i in range(1, count_ + 1):
#         list_number.append(3 * i + 1)
#     return(list_number)

# number = int(input('Введите число N: '))
# print(func_2(number))


''' 3. Напишите функцию, которая принимает 2 строки и выводит сколько раз 2 строка 
является подстрокой 1 строки'''

# line1 = 'ababa'
# line2 = 'aba'
# count = 0

# for i in range(len(line1)):
#     if line2 == line1[i:i + len(line2)]:
#         count += 1
# print(count)