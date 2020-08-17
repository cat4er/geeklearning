#  В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.

from random import randint  # экономим память :)


SIZE = 5
MIN_ITEM = - 100
MAX_ITEM = 100
min_value_ind = 0
max_value_ind = 0
sum_value = 0
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Первоначальный список {array}')

for i in range(SIZE - 1):  # - 1 чтобы не выходить из диапозона
    if i == 0:
        if array[i] > array[i + 1]:
            min_value_ind = i + 1
            max_value_ind = i
        else:
            min_value_ind = i
            max_value_ind = i + 1
    else:
        if array[max_value_ind] < array[i + 1]:
            max_value_ind = i + 1
        elif array[min_value_ind] > array[i + 1]:
            min_value_ind = i + 1

if max_value_ind > min_value_ind:
    for v in range(min_value_ind + 1, max_value_ind):
        sum_value = sum_value + array[v]
    if max_value_ind - min_value_ind < 2:
        print(f'Элементы {min_value_ind} и {max_value_ind} последовательны, между ними нет элементов')
    else:
        print(f'Сумма элементов в диапозоне между  {min_value_ind} и {max_value_ind} равна {sum_value}')
else:
    for v in range(max_value_ind + 1, min_value_ind):
        sum_value = sum_value + array[v]
    if min_value_ind - max_value_ind < 2:
        print(f'Элементы {max_value_ind} и {min_value_ind} последовательны, между ними нет элементов')
    else:
        print(f'Сумма элементов в диапозоне между {max_value_ind} и {min_value_ind} равна {sum_value}')






