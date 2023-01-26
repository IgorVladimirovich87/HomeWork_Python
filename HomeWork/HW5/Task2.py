#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

#text = 'abbbyyyyyyycccdddeeektttHHH'
compr_text = '5a3bk14c120d'

# def compression(string: str) -> str:
#     new_string = ''
#     j = -1
#     for i in range(len(string) - 1):
#         if string[i] != string[i + 1]:
#             if (i - j) > 1:
#                 new_string += str(i - j) + string[i]
#             else:
#                 new_string += string[i]
#             j = i
#
#     k = 1
#     count = 1
#     while string[- 1] == string[- 1 - k]:
#         k += 1
#         count += 1
#     if count > 1:
#         new_string += str(count) + string[- 1]
#     else:
#         new_string += string[- 1]
#     return new_string
#
#
# def unpacking(text: str) -> str:
#     new_string = ''
#     string_list = []
#     digit = ''
#     for i in range(len(text)):
#         if text[i].isdigit():
#             digit += text[i]
#         else:
#             if digit:
#                 string_list.append(digit)
#             string_list.append(text[i])
#             digit = ''
#     for i in range(len(string_list)-1):
#         if string_list[i].isdigit():
#             new_string += string_list[i+1] * (int(string_list[i]) - 1)
#         else:
#             new_string += string_list[i]
#     new_string += text[-1]
#     return new_string
#
# print(text)
# print(compression(text))
# print(compr_text)
# print(unpacking(compr_text))

def unpacking(compr_text: str) -> str:
    temp = compr_text[:]
    for i in range(len(compr_text) - 2):
        if compr_text[i].isdigit() and compr_text[i+1].isalpha():
            elem = int(compr_text[i]) * compr_text[i+1]
            change = compr_text[i] + compr_text[i+1]
            temp = temp.replace(change, elem)
        elif compr_text[i].isdigit() and compr_text[i+1].isdigit() and compr_text[i+2].isalpha():
            elem = int(compr_text[i] + compr_text[i + 1]) * compr_text[i + 2]
            change = compr_text[i] + compr_text[i + 1] + compr_text[i + 2]
            temp = temp.replace(change, elem)
        elif compr_text[i].isdigit() and compr_text[i+1].isdigit() and \
                compr_text[i+2].isdigit():
            elem = int(compr_text[i] + compr_text[i + 1] + compr_text[i + 2]) * compr_text[i + 3]
            change = compr_text[i] + compr_text[i + 1] + compr_text[i + 2] + compr_text[i + 3]
            temp = temp.replace(change, elem)
    return temp


print(unpacking(compr_text))
