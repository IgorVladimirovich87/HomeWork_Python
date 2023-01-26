def string_conversion(text: str) -> list:
    text_list = text.replace('+', ' + ').replace('-', ' + -').replace('*', ' * ') \
        .replace(' *  * ', ' ** ').replace('/', ' / ').replace('(', ' ( ') \
        .replace(')', ' ) ').replace(' (  + ', ' ( ').replace('+ - (', '+ -1 * (').split()

    if text_list[0] == '+':
        text_list.pop(0)
    return text_list


def calculate_simple(task_list: list) -> float:
    operations = {
        '+': lambda x, y: float(x) + float(y),
        '*': lambda x, y: float(x) * float(y),
        '/': lambda x, y: float(x) / float(y),
        '**': lambda x, y: float(x) ** float(y)
    }

    for sign in ['**', '/', '*', '+']:
        while sign in task_list:
            i = task_list.index(sign)
            task_list[i] = operations[sign](task_list[i - 1], task_list[i + 1])
            task_list.pop(i - 1)
            task_list.pop(i)

    return task_list[0]


def calculate_middle(task_list: list) -> float:
    while '(' in task_list:
        i = task_list.index('(')
        j = task_list.index(')')
        part_brackets = task_list[i + 1:j]
        task_list = task_list[:i] + [str(calculate_simple(part_brackets))] + task_list[j + 1:]
    return calculate_simple(task_list)


def calculate_hard(task_list: list):
    while ')' in task_list:
        i = task_list.index(')')
        j = len(task_list[:i]) - task_list[:i][::-1].index('(') - 1
        part_parentheses = calculate_simple(task_list[j + 1:i])
        task_list = task_list[:j] + [part_parentheses] + task_list[i + 1:]
    return calculate_simple(task_list)


task_1: str = '(8-6)-3*(2+2)'
task_2: str = '36/6*(2+5-(3+3))+(2+6)'

print(calculate_hard(string_conversion(task_1)))
print(calculate_hard(string_conversion(task_2)))