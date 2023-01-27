#Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

print("Введите число от 20 чтобы узнать числа кратные 20 и 21")

def my_list(num):
    return [el for el in range(20, num + 1) if el % 20 == 0 or el % 21 == 0]

print(my_list(int(input())))