'''1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''

# text_ = 'ааа ббб ааабв бабв ввв Абв'
# print(f'Старая строка - "{text_}"')
# text_ = text_.split()

# result_text = list(filter(lambda section_value: 'абв' not in section_value, text_))
# result_text = ' '.join(result_text)
# print(f'Отфильтрованная строка - "{result_text}"')




'''2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом"" '''

# from random import randint

# turn = randint(1,2) 
# number_of_candies = 2021

# def play_game_1(turn, candies):

#     candies_store = {1: 0, 2: 0}
    
#     while candies != 0:
#         print(f'\tВсего конфет: "{candies}"')
#         print(f'Игрок № {turn} сколько конфет возьмете? Введите число от 1 до 28: ', end="")

#         while True:
#             number_candies = int(input())
#             if 1 <= number_candies <= 28: break
#             else: print('Введите корректное значение: ', end='')

#         candies_store[turn] += number_candies
#         candies -= number_candies
#         if candies == 0: print(f'Поздравляю! Выиграл игрок {turn} , забрав последние конфеты!')
        
#         if turn == 1: turn = 2
#         else: turn = 1

#     for key, value in candies_store.items():
#         print(f' Количество конфет игрока № {key} = {value}')
    
#     return '\tИгра завершена!'


# def play_game_2(turn, candies):
#     name_player = input('Игрока №1 зовут Джарвис. А как зовут Вас, игрок №2: ')
#     candies_store = {'Джарвис': 0, name_player: 0}
    
#     while candies != 0:
#         print(f'\tВсего конфет: "{candies}"')
        
#         if turn == 2:
#             print(f'{name_player} сколько конфет возьмете? Введите число от 1 до 28: ', end="")
            
#             while True:
#                 number_candies = int(input())
#                 if 1 <= number_candies <= 28: break
#                 else: print('Введите корректное значение: ', end='')

#             candies_store[name_player] += number_candies
#             candies -= number_candies

#             if candies == 0: print(f'Поздравляю! Выиграл игрок {name_player} , забрав последние конфеты!')
#             turn -= 1
#         else:
#             robot_step = candies % 29
#             candies_store['Джарвис'] += robot_step
#             print(f'Джарвис забрал {robot_step} конфет')
#             candies -= robot_step
#             turn +=1

#             if candies == 0: print('Джарвис выиграл!')
        
#     for key, value in candies_store.items():
#         print(f' Количество конфет игрока {key} = {value}')
    
#     return 'Игра завершена!'


# print('Приветствую вас в игре "Конфеты-2021"! \n'
#       'Правила игры: \t'
#       '1. Право первого хода генерируется случайно. Первым ходит игрок №', turn, '\n\t\t'
#       '2. На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет\n\t\t'
#       '3. Существует 2 режима игры: 1.(человек-человек) 2.(человек-бот)\n\t\t'
#       '4. Все конфеты оппонента достаются сделавшему последний ход.\n'
#       )

# while True:
#     game_mod = int(input('Выберите режим игры, 1 или 2: '))
#     if game_mod == 1: 
#         print(play_game_1(turn, number_of_candies))
#         break
#     elif game_mod == 2:
#         print(play_game_2(turn, number_of_candies))
#         break
#     else: print('Введите корректное значение!')




'''3. Создайте программу для игры в ""Крестики-нолики"".'''

# from random import randint

# # Изначально рандомно определяю очередь первого хода 
# turn = randint(1,2)    

# # Словарь значений каждой клетки игрового поля
# section_value = {1: 1, 2: 2, 3: 3,
#             4: 4, 5: 5, 6: 6,
#             7: 7, 8: 8, 9: 9,
#             }

     
# def result_play(section_value):

#     # Тут пока что только так :D

#     # Анализ результатов по горизонтали
#     if section_value[1] == section_value[2] == section_value[3]: return  section_value[1]
#     elif section_value[4] == section_value[5] == section_value[6]: return  section_value[4]
#     elif section_value[7] == section_value[8] == section_value[9]: return  section_value[7]

#     # Анализ результатов по вертикали
#     elif section_value[1] == section_value[4] == section_value[7]: return  section_value[1]
#     elif section_value[2] == section_value[5] == section_value[8]: return  section_value[2]
#     elif section_value[3] == section_value[6] == section_value[9]: return  section_value[3]

#     # Анализ результатов по диагонали
#     elif section_value[1] == section_value[5] == section_value[9]: return  section_value[1]
#     elif section_value[3] == section_value[5] == section_value[7]: return  section_value[3]

#     else: return False


# def print_field_play(step_, symbol, section_value):
    
#     if step_ == None or step_ != None:
#         if step_ != None: section_value[step_] = symbol

#         print('\t', '-' * 10, '\n', '\t', 
#             section_value[1], '׀', section_value[2], '׀', section_value[3],'\n',
#             '\t', '-' * 10, '\n',
#             '\t', section_value[4], '׀', section_value[5], '׀', section_value[6],'\n',
#             '\t', '-' * 10, '\n',
#             '\t', section_value[7], '׀', section_value[8], '׀', section_value[9],'\n'
#             '\t', '-' * 10, '\n'
#             )
#         return section_value


# def play_game(number_player, section_value):
#     number_try = 0
#     list_do_step = []
#     very_first_player = ('x', number_player)
#     very_first_symbol = 'x'
#     end_txt = 'Игра завершилась :p'
    
#     while number_try != 6:
#         print(f'Игрок № {number_player}, введите "цифру" яйчейки куда хотите сходить: ', end='')
#         step = int(input())

#         # Проверка чтобы игроки не вводили одинаковые номера яйчеек
#         if step in list_do_step: continue

#         print_field_play(step, very_first_symbol, section_value)

#         list_do_step.append(step)

#         # Замена символа после каждого хода игрока
#         if very_first_symbol == 'x': very_first_symbol = 'o'
#         else: very_first_symbol = 'x'

#         # Замена игрока после каждого хода 
#         if number_player == 1: number_player = 2
#         else: number_player = 1

#         # Избежание ложной победы 2-го по "очереди хода" игрока
#         if number_try == 4: result = result_play(section_value)

#         number_try += 1
    
    
#     if result == very_first_player[0]:
#         print(f'Выиграл игрок под номером {very_first_player[1]}! Поздравляю!')
#         return end_txt
#     elif result == False: 
#         print('НИКТО НЕ ВЫИГРАЛ')
#         return end_txt
#     else: 
#         if very_first_player[1] == 1:
#             print(f'Выиграл игрок под номером 2! Поздравляю!')
#             return end_txt
#         elif very_first_player[1] == 2:
#             print(f'Выиграл игрок под номером 1! Поздравляю!')
#             return end_txt
    
    
# print('Приветствую вас в игре "крестики-нолики"! \n'
#       'Правила игры: \t'
#       '1. Право первого хода генерируется случайно. Первым ходит игрок №', turn, '\n\t\t'
#       '2. Выигрывает игрок, 3 элемента которого быстрее совпали по-'
#       'диогонали/вертикали/горизонтали\n\t\t'
#       '3. У каждого игрока только "3" хода\n\t\t'
#       '4. Игроки ходят поочередно, выбирая номер области поля, приведенного ниже\n'
#       )


# print_field_play(None, None, section_value)
# print(play_game(turn, section_value))




'''4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.'''

print()

