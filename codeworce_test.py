# # Реализуйте функцию unique_in_order, которая принимает в
# # качестве аргумента последовательность и возвращает список элементов без каких-либо элементов
# # с одинаковым значением рядом друг с другом и сохраняет исходный порядок элементов.

# from random import randint

# def non_repeating_numbers(List):
#     List_1 = []
#     for name in range(len(List)):
#         if name == 0 or List[name] != List[name-1]:
#             List_1.append(List[name])
#     return List_1


# print(non_repeating_numbers('AAAABBBCCDAABBB'))



# # Учитывая два целых числа a и b, которые могут быть 
# # положительными или отрицательными, найдите сумму всех целых чисел между ними и включая их, 
# # и верните ее. Если два числа равны, верните a или b.
# def get_sum(a, b):
#     sun = 0
#     if a != b:
#         if a < b:
#             for i in (range(a, b+1)):
#                 sun = sun + i
#         if a > b:
#             for i in (range(b, a+1)):
#                 sun = sun + i
#         return sun
#     if a == b:
#         return a


# print(get_sum(-1, 2))

# # Завершите решение так, чтобы оно разбило строку на пары из двух символов. 
# # Если строка содержит нечетное количество символов, 
# # то она должна заменить отсутствующий второй символ последней пары символом подчеркивания ('_').
# def solution(s):
#     if len(s) % 2 == 0:
#         result = [s[i:i+2] for i in  range (0, len(s), 2) ]
#     else:
#         s = s + "_"
#         result = [s[i:i+2] for i in  range (0, len(s), 2) ]
#     return result

# print(solution("asdfads"))

