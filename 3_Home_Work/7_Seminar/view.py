# Модуль вывода интерфейса
import controller

# считывание значения режима работы
def working_mode():
    return input('Приветствую Вас в программе "Телефонный Справочник"\n'
                 'Введите ЦИФРУ операции, которую хотите выполнить:\n'
                 '\t (1) Просмотр текущих записей\n'
                 '\t (2) Добавление записи\n'
                 '\t (3) Экспорт текущих записей\n'
                 '\t (4) Импорт записей из файла\n'
                 'Введите выбранный режим: ' 
                 )

# вывод всех записей режима (1)
def print_mode_1(lst):
    print('\nТекущие записи: \n')
    for list_txt in lst:
        print('\t',list_txt, end= ' ')
    controller.duration_of_work()

# отчет о выполнении работы режима (2)
def progress_report():
    print('\tКонтакт добавлен в справочник!')
    controller.duration_of_work()

    