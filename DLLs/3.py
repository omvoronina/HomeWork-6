# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for i in range(2, 10):
    list = []
    for j in range(2, 101):
        if j % i == 0 and j != i:
            j = 0
            list.append(j)
        else:
            j = j
    print(f'{list.count(0)} чисел кратны {i}')

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

list_1 = [8, 3, 15, 6, 4, 2]
list_2 = [i for i in range(0, len(list_1)) if list_1[i] % 2 == 0]
print(list_2)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#
array = [1, 3, 5, 7, 9, 45, 33, 6]
ind_max, max = array.index(max(array)), max(array)
ind_min, min = array.index(min(array)), min(array)
array[ind_max] = min
array[ind_min] = max
print(array)

# 4. Определить, какое число в массиве встречается чаще всего.

array = input('Введите элементы массива (числа) через пробел  ').split(' ')
list = [array.count(i) for i in array]
print('Чаще всего в массиве встречается число  ' + array[list.index(max([array.count(i) for i in array]))])

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

array = list(map(int, input('Введите элементы массива (числа) через пробел  ').split(' ')))
print(f' Максимальный отрицательный элемент равен  {array[array.index(min(array))]}, а его позиция в массиве равна {array.index(min(array)) + 1}')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

array = list(map(int, input('Введите числа через пробел  ').split(' ')))
print(array)
print(sum([i for i in array if array.index(i) > array.index(min(array)) and array.index(i) < array.index(max(array))]))

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

array = [1, 9, 8, 6, 0, 6, -1, 8]
print(min(array))
array.remove(min(array))
print(min(array))

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []
for i in range(1, 6):
    list = []
    inp = [int(i) for i in input('Введите 3 элемента строки матрицы через пробел  ').split(' ')]
    inp.append(sum(inp))
    print(*inp, )
    matrix.append(inp)
for i in matrix:
    print(*i)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[1, 8, 9, 7],
          [8, 3, 4, 2],
          [7, 3, 2, 1],
          [5, 7, 2, 0]]
transp = [[i[0] for i in matrix],
          [i[1] for i in matrix],
          [i[2] for i in matrix],
          [i[3] for i in matrix]]
print(max([min(i) for i in transp]))

