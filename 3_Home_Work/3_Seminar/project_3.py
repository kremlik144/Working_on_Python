
'''1. Задайте список из нескольких чисел. Напишите программу, которая найдёт 
сумму элементов списка, стоящих на нечётной позиции.

Пример:
 - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''


# value_list = input('Введите элементы списка через запятую: ')
# number_list = value_list.split(', ')
# value_summ = 0

# for i in range(1, len(number_list), 2):
#     value_summ += int(number_list[i]) 

# print(value_summ)


'''2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''


# from random import randint

# def generation_list(size):              # генерирует список заданной рамерности
#     new_list = []
#     for i in range(size):
#         new_list.append(randint(1, 9))
#     return new_list

# def multiply(count, lst):
#     result = []
#     reverse_index = -1
    
#     if count % 2 != 0:
#         for i in range(count// 2 + 1):
#             result.append(lst[i] * lst[reverse_index])
#             reverse_index -= 1    

#     if count % 2 == 0:
#         for i in range(count // 2):
#             result.append(lst[i] * lst[reverse_index])
#             reverse_index -= 1

#     return result 

# size_list = int(input('Введите размерность списка: '))
# new_list = generation_list(size_list)

# print(f'Сгенерированный список: {new_list}')
# print(f'Произведение пар чисел списка: {multiply(len(new_list), new_list)}')


'''3. Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''


# from random import uniform

# def generation_list(size):     
#     new_list = []
#     for i in range(size):
#         new_list.append(round(uniform(1, 9), 2))
#     return new_list

# def distinction(lst):
#     mx_value = lst[0] - int(lst[0])
#     mn_value = lst[0] - int(lst[0])
    
#     for i in range(len(lst)):
#         number = lst[i] - int(lst[i])
#         if number > mx_value:
#             mx_value = number
#         if number < mn_value:
#             mn_value = number
    
#     mx_value, mn_value = round(mx_value, 2), round(mn_value, 2)

#     result = round(mx_value - mn_value, 2)

#     return result, mx_value, mn_value

# size_list = int(input('Введите размерность списка: '))
# new_list = generation_list(size_list)
# print(new_list)
# result = distinction(new_list)

# print(f'min значение = {result[2]}, max значение = {result[1]}, разность = {result[0]}')


'''4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 '''


# number = int(input('Введите число: '))
# result = ''

# while number > 0:
#     result += str(number % 2)
#     number //= 2

# print('Преобразованное число:', result)


'''5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] '''


# n = int(input('Введите число n: '))

# fib_1 =[1, 1]               # список чисел Фибоначчи c положительным индексом
# fib1 = fib2 = 1

# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     fib_1.append(fib2)


# fib_2 =[0, 1]               # список чисел Фибоначчи c отрицательным индексом
# f1, f2 = 1, -1

# for i in range(2, n+1):
#     f1, f2 = f2, f1 - f2
#     fib_2.append(f1)

# fib_2.reverse()

# print(fib_2 + fib_1)
