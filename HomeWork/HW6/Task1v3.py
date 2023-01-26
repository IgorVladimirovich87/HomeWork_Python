

quarter = int(input('Выбирите действие: 1-вычитание: 2 - сложение; 3 - умножение; 4 - деление. ')) 
match quarter:
    case 1:
        x = input("Введите число x: ")
        y = input("Введите число y: ")

        a = float (x)
        b = float (y)
        print (a - b)

    case  2:
        z = input("Введите число x: ")
        w = input("Введите число y: ")

        c = float (z)
        d = float (w)

        print(c + d)
    
    case  3:
        z = input("Введите число x: ")
        w = input("Введите число y: ")
        
        c = float (z)
        d = float (w)
        print(c * d)

    case  4:
        z = input("Введите число x: ")
        w = input("Введите число y: ")
        
        c = float (z)
        d = float (w)
        print(c / d)
    


