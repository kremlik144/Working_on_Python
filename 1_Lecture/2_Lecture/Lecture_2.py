
'''colors = ['reed', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)
data.close()'''

# 'a'- открытие для добавления данных 
# 'w'- открытие для записи данных 
# 'r'- открытие для чтения данных 

# либо так, акрытие программы происходит самостоятельно 

'''with open('file.txt', 'a') as data:
    data.write('line1 \n')
    data.write('line2 \n')'''


# Чтение файлов 

'''path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close'''



# Вызов функции из отдельного файла 

'''import fun_c as h  # h - замененное название функции для обращения в дальнейшем 

print(h.f(1))'''


# Вызов функции с неограниченным количеством аргументов 

'''def concatenation(*params):           # для этого ставим знак '*' перед аргументом
    res: str = ''
    for item in params:
        res += item
    return res

print(concatenation('a', 's', 'd', 'w'))    # asdw
print(concatenation('a', '1'))              # a1
#print(concatenation(1, 2, 3, 4))           # TupeEror тк тип данных указали str = '' '''




# Кортежи - своеобразный неизменяемый список

'''a = (1, 2, 3, 4)      # общий вид 
print(a)              # вывод всего кортежа
print(a[0])           # вывод отдельного элемента (индексация как и везде)

for item in a:                 # вывод кортежа посредством цикла
    print(item, end = '---') '''



# Словари - неупорядоченные коллекции произвольных обьектов с доступом по ключу

'''dictionary = {}     # обьявление 
dictionary = \
    {
        'up': '1',
        'left': '2',
        'down': '3',
        'right': '4'
    }
print(dictionary) # выводит весь словарь с обозначениями {'up': '1', 'left': '2', 'down': '3', 'right': '4'}
print(dictionary['left'])  # выводит элемент по ключу те - '2'
# замена значения
dictionary['up'] = 'new'
# типы ключей могут отличаться 
for k in dictionary.keys():   # выведет все ключи(.keys) / значения(.values) словаря 
    print(k) '''




# Множества

'''colors = {'red', 'green', 'blue'} # обьявление множества
print(colors)  # {'red', 'blue', 'green'}
colors.add('gray') # добавляет 'gray' в конец множества
colors.remove('red') # или (.discard)удалит указанный элемент из множества
colors.clear()       # очищает множество'''

#  операции со множествами 

'''a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = a.copy()        # .copy() копирует {1, 2, 3, 4, 5}
u = a.union(b)      # .union() {1, 2, 3, 4, 5, 6, 7} добавляет в множ. а - множ. b НО те элементы, которых нет в 'a'
i = a.intersection(b)   # пересечение множеств
y = a.difference(b)     # выводит значения, которых нет в множестве 'b'

s = frozenset(a)        # замороженное(неизмен.) множество '''







