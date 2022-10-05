
''' 1. Найдите второе вхождение строки в список'''


# lst = ['qwe', 'www', 'www', 'q', 'qwe', 'ere']
# value = 'qwe'
# count = 0

# for i in range(len(lst)):
#     if lst[i] == value:
#         count += 1
#         if count == 2:
#             print(f'Позиция второго вхождения значение "{value}" в список {lst} равна = {i}')
#             break


''' 2. Задайте список. Напишите программу которая определит, присутствует ли в списке строк 
некое число '''

lst = ['qwe', '123,', 123, '324', 'www', 'www', 'q', 'qwe', 'ere']
value = 324

for i in range(len(lst)):
    if str(lst[i]).isdigit() == True:
        if int(lst[i]) == value:
            print(lst)
            print(f'Значение "{value}" есть в списке на позиции {i}')
            break 
else: 
    print('Значения нет')