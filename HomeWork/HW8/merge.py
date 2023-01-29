

import student_info as si
import cabinet_info as cab


def option():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть класс  и место которое занимает  студент \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(Surn)
        print(f"{si.stud_card['ID'][index]}, {si.stud_card['Имя'][index]},{si.stud_card['Фамилия'][index]}\n,{si.stud_card['Дата рождения'][index]}, {si.stud_card['Успеваемость'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        cc = str(input('Введите ID студента для вывода по классам: '))
        if cc in cab.class_card['ID']:
            index = cab.class_card['ID'].index(cc)
            print(f" {cab.class_card['ID'][index]}, {cab.class_card['Номер парты'][index]},{cab.class_card['Ряд'][index]},{cab.class_card['Вид парты'][index]},{cab.class_card['Предмет'][index]}")
        print('\nХотите выполнить другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()
    else:
        print('еще раз')
    exit()


option()  