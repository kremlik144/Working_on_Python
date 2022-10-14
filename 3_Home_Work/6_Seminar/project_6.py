'''3.(Семинар 2) Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их 
сумму, округлённую до трёх знаков после точки.
Для n = 6: 14.072'''

                    # было

# number = int(input('Введите число N: '))
# summ_numbers = 0
# for i in range(1, number + 1):
#     result_numbers = (1 + 1 / i) ** i
#     summ_numbers += result_numbers
# print(round(summ_numbers, 3))


                # Стало
                # Когда в начале пути терпеть не мог однострочников, а теперь --> 
                # Предрекали, что ты уничтожишь ситхов, а не примкнешь к ним :D

# print(round(sum([(1 + 1 / i) ** i for i in range(1, int(input('Введите число N: ')) + 1)]), 3))



''' 1.(Семинар 3) Задайте список из нескольких чисел. Напишите программу, которая найдёт 
сумму элементов списка, стоящих на нечётной позиции.
Пример:
 - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

            # было

# value_list = input('Введите элементы списка через запятую: ')
# number_list = value_list.split(', ')
# value_summ = 0
# for i in range(1, len(number_list), 2):
#     value_summ += int(number_list[i]) 
# print(value_summ)


            # улучшение при помощи функции enumerate()

# value_list, result_value = input('Введите элементы списка через запятую: ').split(', '), 0
# for i, value in enumerate(value_list):
#     if i % 2 != 0: result_value += int(value)
# print(f'Сумма элементов списка, стоящих на нечетных позициях =  {result_value}')




'''2.(Семинар 3) Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

                        # Было

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



                # применил list comprehension, убрав старую функцию генерации массива 

# from random import randint

# def multiply(count, lst):
#     result = []
#     reverse_index = -1
    
#     if count % 2 != 0:
#         for i in range(count// 2 + 1):
#             result.append(lst[i] * lst[reverse_index])
#             reverse_index -= 1    
#     else:
#         for i in range(count // 2):
#             result.append(lst[i] * lst[reverse_index])
#             reverse_index -= 1

#     return result 

# number_list = [randint(1, 9) for _ in range(1, int(input('Введите размерность списка: '))+1)]

# print(f'Сгенерированный список: {number_list}\n'
#       f'Произведение пар чисел списка: {multiply(len(number_list), number_list)}')




'''3.(Семинар 4)Задайте последовательность чисел. Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9] -> [2, 4, 5, 9]'''

                    # Было

# value_list = input('Введите элементы списка через запятую: ')
# number_list = value_list.split(', ')
# result = []

# for i in range(len(number_list)):
#     value = number_list[i]
#     if number_list.count(value) == 1:
#         result.append(int(value))

# print(f'Cписок неповторяющихся элементов исходной последовательности --> {result}')



                # улучшение при помощи функции enumerate()

# number_list = input('Введите элементы списка через запятую: ').split(', ')
# result = []

# for index, value in enumerate(number_list):
#     if number_list.count(value) == 1: result.append(int(value))

# print(f'Cписок неповторяющихся элементов исходной последовательности --> {result}')