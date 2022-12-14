

x, y = map(int, input('Введите координаты точки (x,y) через пробел: ').split())
if x > 0 and y > 0:
    print(f'{x = }; {y = } -> 1 четверть')
elif x < 0 and y > 0:
    print(f'{x = }; {y = } -> 2 четверть')
elif x < 0 and y < 0:
    print(f'{x = }; {y = } -> 3 четверть')
elif x > 0 and y < 0:
    print(f'{x = }; {y = } -> 4 четверть')