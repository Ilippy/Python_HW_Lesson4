# Задача №29. Общее обсуждение
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.


# Ваня: 1: max_number 2: if n > max_number
n = int(input()) 
max_number = 1000      # max_number = n
while n != 0:
    n = int(input())  
    if max_number > n: # if n > max_number:
        max_number = n
print(max_number)


# Петя: 1: while n != 0:, 2: max_number = n, 3: print(max_number)
n = int(input())
max_number = -1        # max_number = n
while n < 0:           # while n != 0:
    n = int(input())   
    if max_number < n:  
        n = max_number # max_number = n
print(n)               # print(max_number)

# Победил Ваня
print("Ваня совешил 3 ошибки, Петя совершил 5 ошибки")
print("Ваня победил")

n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if n > max_number:
        max_number = n
print(max_number)