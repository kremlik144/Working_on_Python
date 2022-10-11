'''1. В файле находится N натуральных чисел, записанных через пробел. Среди чисел
не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
1 2 3 4 5 7 8 9 --> 6'''

# with open('seminar_5.txt', 'w') as data:
#     data.writelines('1 2 3 4 5 7 8 9')
# with open('seminar_5.txt', 'r') as data:
#     string = data.readline()

# string = list(map(int, string.split()))

# for i in range(1, len(string)):
#     if string[i] - 1 != string[i-1]:
#         result_number = string[i-1] + 1
# print(f'отсутствующее число = {result_number}')




'''2.Напищите программу, удаляющую из текста все слова, содержащие "абв" <-- filter()'''

# text_ = 'ааа ббб ааабв бабв ввв'
# print(f'Старая строка - {text_}')
# text_ = text_.split()

# result_text = list(filter(lambda e: 'абв' not in e, text_))
# result_text = ' '.join(result_text)
# print(f'Отфильрованная строка - {result_text}')