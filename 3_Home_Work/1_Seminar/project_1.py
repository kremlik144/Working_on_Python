''' 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
Пример:   
- 6 -> да
- 7 -> да
- 1 -> нет'''

'''number = int(input('Введите число: '))
week_day = [1, 2, 3, 4, 5]
week_ends = [6, 7]

if number in week_day:
    print(f'День {number} НЕ является выходным ')
elif number in week_ends:
    print(f'День {number} ЯВЛЯЕТСЯ выходным ')'''


'''2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) =
¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''

'''X_ = True
Y_ = True
Z_ = True 
if not(X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
    print(f'№1 Если X = {X_} Y = {Y_} Z = {Z_}, то утверждение True')

X_ = False
Y_ = True
Z_ = True 
if not(X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
    print(f'№2 Если X = {X_} Y = {Y_} Z = {Z_}, то утверждение True')

X_ = False
Y_ = False
Z_ = True 
if not(X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
    print(f'№3 Если X = {X_} Y = {Y_} Z = {Z_}, то утверждение True')

X_ = False
Y_ = True
Z_ = False 
if not(X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
    print(f'№4 Если X = {X_} Y = {Y_} Z = {Z_}, то утверждение True')

X_ = False
Y_ = False
Z_ = False
if not(X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
    print(f'№5 Если X = {X_} Y = {Y_} Z = {Z_}, то утверждение True')

X_ = True
Y_ = False
Z_ = True
if not(X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
    print(f'№6 Если X = {X_} Y = {Y_} Z = {Z_}, то утверждение True')

X_ = True
Y_ = False
Z_ = False
if not(X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
    print(f'№7 Если X = {X_} Y = {Y_} Z = {Z_}, то утверждение True')

X_ = True
Y_ = True
Z_ = False
if not(X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
    print(f'№8 Если X = {X_} Y = {Y_} Z = {Z_}, то утверждение True')'''


'''3.Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''

'''coordinate_x = int(input('Введите координату Х: '))
coordinate_y = int(input('Введите координату Y: '))

if coordinate_x > 0 and coordinate_y > 0:
    print(f'Заданная точканаходится в 1 четверти ')
elif coordinate_x < 0 and coordinate_y > 0:
    print(f'Заданная точканаходится во 2 четверти ')
elif coordinate_x < 0 and coordinate_y < 0:
    print(f'Заданная точканаходится в 3 четверти ')
elif coordinate_x > 0 and coordinate_y < 0:
    print(f'Заданная точканаходится в 4 четверти ')'''


'''4.Напишите программу, которая по заданному номеру четверти, показывает диапазон
возможных координат точек в этой четверти (x и y).'''

'''result = int(input('Введите номер четверти: '))

if result == 1:
    print(f'В заданной четверти значения х > 0 и у > 0')
elif result == 2:
    print(f'В заданной четверти значения х < 0 и у > 0')
elif result == 3:
    print(f'В заданной четверти значения х < 0 и у < 0')
elif result == 4:
    print(f'В заданной четверти значения х > 0 и у < 0')'''


'''5.Напишите программу, которая принимает на вход координаты двух точек и находит
расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21'''

'''from math import sqrt

x1, y1 = int(input('Введите координату Х1: ')), int(input('Введите координату Y1: '))
x2, y2 = int(input('Введите координату Х2: ')), int(input('Введите координату Y2: '))

result = str(sqrt((x2 - x1)**2 + (y2 - y1)**2))
print(f'Расстояние между точками = {result[:4]}')'''