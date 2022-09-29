'''1. Напишите программу, которая принимает на вход вещественное число и
показывает сумму его цифр.
*Пример:*
6782 -> 23
0,56 -> 11'''


'''def summ(number):
    summ_number = 0
    for i in range(len(number)):
        if number[i] != '.':
            summ_number += int(number[i])
    return summ_number
number = input("Введите число N: ")
print(f"Сумма цифр числа {number} = {summ(number)}")'''




'''2. Напишите программу, которая принимает на вход число N и выдает набор
произведений чисел от 1 до N.
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''


'''number = int(input("Введите число N: "))
lst = []
for i in range(1, number+1):
    number_lst = 1 * i
    if len(lst) == 0:
        lst.append(number_lst)
    if i >= 2:
        number_lst = i * lst[len(lst)-1]
        lst.append(number_lst)
print(lst)'''




'''3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их 
сумму, округлённую до трёх знаков после точки.
Для n = 6: 14.072'''


'''number = int(input('Введите число N: '))
summ_numbers = 0
for i in range(1, number + 1):
    result_numbers = (1 + 1 / i) ** i
    summ_numbers += result_numbers
print(round(summ_numbers, 3))'''




'''4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.'''


'''number = int(input("Введите число N: "))
lst = []
size_lst = number * 2 + 1
number_lst = -number 
while len(lst) != size_lst:
    if number_lst < 0:
        lst.append(number_lst)
        number_lst += 1
    if number_lst == 0:
        lst.append(number_lst)
        number_lst += 1
    if number_lst > 0:
        lst.append(number_lst)
        number_lst += 1
x1 = int(input(f'Введите 1-ю позицию. Число от 1 до {len(lst)}: '))
x2 = int(input(f'Введите 2-ю позицию. Число от 1 до {len(lst)}: '))
result = lst[x1 - 1] * lst[x2 - 1]
print(f'Массив - {lst}. Произведение элементов на позициях {x1}, {x2} = {result}')'''




'''5. Реализуйте алгоритм перемешивания списка.'''


'''from random import randint
def mix_list(array):
    new_list = []
    size = len(array) - 1
    for i in range(len(array)):
        new_adress = randint(0, size)
        new_list.append(array[new_adress])
        del array[new_adress]
        size -= 1
    return new_list
old_list = input('Введите элементы массива через запятую: ')
old_list = old_list.split(', ')
print(mix_list(old_list))'''