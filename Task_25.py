# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

def getStrWithCount(lst: list[str]) -> list[str]:
    """Формируем результирующий список с простановкой количеством элементов"""
    res_list = []
    for i in range(len(lst)):
        res_list.append(lst[i]) if lst[i] not in lst[:i] else res_list.append(f"{lst[i]}_{lst[:i].count(lst[i])}")
    return res_list



lst = list(input("введите список через пробел\n").split())
print(*getStrWithCount(lst))
