'''1 Вычислить число π c заданной точностью d
*Пример:* 
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$'''


# d = float(input('Введите точность d: '))
# size = int(input('Введите количество знаков которое хотите увидеть после ",": '))

# n = 0
# upper_bound = 0
# lower_bound = 0
# flag = False

# while flag == False:
#     n += 1
#     upper_bound = lower_bound + 4 / (2 * n - 1)
#     n += 1
#     lower_bound = upper_bound - 4 / (2 * n - 1)
#     if upper_bound - lower_bound <= d:
#             flag = True
    
# pi_ = (upper_bound + lower_bound) / 2
# pi_ = str(pi_)

# print(f'Число "π" = {pi_[:size+2]} с точностью до d = "{d}" и "{size}" знаками после запятой')


'''2 Задайте натуральное число N. Напишите программу, которая составит
список простых множителей числа N.
*Пример*
- при N=236 -> [2, 2, 59]'''


# number = int(input('Введите натуральное число N: '))
# work_num = number
# result = []
# divisor = 2

# while work_num > 1:
#     if work_num % divisor == 0:
#         result.append(divisor)
#         work_num //= divisor
#     else: divisor += 1

# print(f'При N = {number} --> {result}')


'''3 Задайте последовательность чисел. Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9] -> [2, 4, 5, 9]'''


# value_list = input('Введите элементы списка через запятую: ')
# number_list = value_list.split(', ')
# result = []

# for i in range(len(number_list)):
#     value = number_list[i]
#     if number_list.count(value) == 1:
#         result.append(int(value))

# print(f'Cписок неповторяющихся элементов исходной последовательности --> {result}')


'''4 Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''


# from random import randint

# def generate_ratios(k):
#     ratios = [randint(2, 100) for i in range (k + 1)]
#     return ratios

# def get_polynomial(k, ratios):
#     polynomial = []
#     i_ratios = 0

#     for k in range(k, -1, -1):
#         if k >= 2:
#             polynomial.append(str(ratios[i_ratios]) + '*x^' + str(k) + ' + ')
#             i_ratios += 1
#         if k == 1:
#             polynomial.append(str((ratios[i_ratios])) + '*x' + ' + ')
#             i_ratios += 1
#         if k == 0: polynomial.append(str((ratios[i_ratios])) + ' = 0')

#     return ''.join(polynomial)


# k = int(input('Задайте натуральную степень k: '))
# ratios = generate_ratios(k)
# result_poly = get_polynomial(k, ratios)

# with open('project_4_seminar_4.txt', 'w') as data:
#     data.writelines(result_poly)

# print(f'Многочлен "{result_poly}" записан в файл "project.txt"')


'''5 Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. 
Степени многочленов могут отличаться.'''


# import re
# import itertools

# file1 = 'polynomial_1.txt'
# file2 = 'polynomial_2.txt'
# file_sum = 'sum_polynomials.txt'

# def read_pol(file):
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol

# def convert_pol(pol):
#     pol = pol.replace('= 0', '')
#     pol = re.sub("[*|^| ]", " ", pol).split('+')
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x': i.insert(0, 1)
#         if i[-1] == 'x': i.append(1)
#         if len(i) == 1: i.append(0)
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
#     return pol

# def fold_pols(pol1, pol2):   
#     x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     for i in pol1 + pol2:        
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key = lambda r: r[1], reverse = True)
#     return res

# def get_sum_pol(pol):
#     var = ['*x^'] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0': del (x[0])
#         if x[-1] == '0': del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == '1': 
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))

# def write_to_file(file, pol):
#     with open(file, 'w') as data:
#         data.write(pol)

# pol1 = read_pol(file1)
# pol2 = read_pol(file2)

# pol_1 = convert_pol(pol1)
# pol_2 = convert_pol(pol2)

# pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# write_to_file(file_sum, pol_sum)

# print(pol1)
# print(pol2)
# print(pol_sum)