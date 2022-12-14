number = int(input("Введите число дня недели от 1 до 7: "))

if number < 1 or number > 7:
    print ("Вы ввели неверное число, введите число от 1 до 7: ")
elif number > 5:
    print ("Да, это ВЫХОДНОЙ день")
else:
    print ("Нет, это не выходной день")