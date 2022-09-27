''' № 1 Напишите программу которая на вход принимает 2 числа и проверяет, является ли одно число
квадратом другого '''

#x = int(input('Введите число х: '))
#y = int(input('Введите число у: '))

#if(y == x**2):
#    print('Число y является квадратом числа x')
#else:
#    print('Число y НЕ является квадратом числа x')


''' № 2 Напишите программу которая на вход принимает 5 числа и находит максимум из них'''

lst = []
count = 0
while(count < 5):
    number = int(input(f'Введите {count+1} число: '))
    lst.append(number)
    count = count + 1

max_value = lst[0]

for i in range(1,len(lst)):
    if(lst[i] > max_value):
        max_value = lst[i]

print(f'Максимальное из чисел в массиве {lst} = {max_value}')


