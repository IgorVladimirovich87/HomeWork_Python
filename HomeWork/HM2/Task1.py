#1. Напишите программу, которая принимает на вход
#вещественное число и показывает сумму его цифр.

n = int(input ("Введите число: "))

sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print ("Сумма чисел:", sum)