
'''list comprehension -  Улучшенно создание списков путем замены цикла for [i for i in range(x)]'''

# №1
# print(f'New list = {[i for i in range(5)]}')



# № 2 
# from random import randint

# lst = [randint(1, 12) for _ in range(10)]
# print(lst)

# new_lst = [(i, i**2) for i in lst if i % 2 == 0 ]
# print(new_lst)




'''lambda - выражения lambda[параметры]: инструкция'''

# № 1

# sum = lambda a, b: a + b
# print(sum(2,3))

# № 2

# def select_operator(value):
#     if value == 1: return lambda a, b: a + b
#     if value == 2: return lambda a, b: a - b
#     else: return lambda a, b: a * b

# operator = select_operator(1)
# print(operator(10, 6))

# operator = select_operator(2)
# print(operator(10, 6))

# operator = select_operator(3)
# print(operator(10, 6))



'''filter() - функция filter (имя функции пользователя, итеррируемый обьяект - список, строка,
множество, кортеж ....) сохраняет только те элементы для которых функция вернула значение True'''

# def filter_number(x):
#     if x % 2 == 0: return True
#     else: return False

# list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = filter(filter_number, list_number)
# print('Тип данных: ', type(result))
# print('Отфильтрованный список : ', list(result)) # результат работы функции ОБЯЗ-О преобразовывать в тип список, множество, кортеж ...



'''map() - функция  map(функция которую хотим применить, обьект к которой хотим ее применит)
применяется к каждому элементу обьекта'''

# list_number = [1, 2, 3, 4]

# result = map(lambda x: x**2, list_number)

# print(list(result))  #  выводим обязательно в виде типа списка, множ, кортежа




'''zip() - функция  zip(итеррируемый обьек_1, итеррируемый обьек_2) генерирует список кортежей
которые содержат элементы из каждого обьекта'''

# list_number = [1, 2, 3, 4]
# name_list = ['Ivan', 'Maksim', 'Alexey', 'Vladimir']

# result = zip(name_list, list_number)

# print(list(result))




'''enumerate() - функция позволяет перебирать коллекцию элементов, отслеживая индекс текущего 
элемента'''

# name_list = ['Ivan', 'Maksim', 'Alexey', 'Vladimir']

# for index, value in enumerate(name_list):
#     print(f'index - {index}, values - {value}  ')


