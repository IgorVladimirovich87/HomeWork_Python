#3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

def first_let_name(*args):
    names_full = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_full:
            names_full[letter] = [i]
        else:
            names_full[letter] += [i]

    return names_full

print(first_let_name("Иван", "Мария", "Петр", "Илья", "Алина", "Бибочка"))