# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint  # экономим память :)


SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_value_ind = 0
max_value_ind = 0
print(f'первоначальный список {array}')

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

array[max_value_ind], array[min_value_ind] = array[min_value_ind], array[max_value_ind]
print(f'индекс минимального значения {min_value_ind}')
print(f'индекс максимального значения {max_value_ind}')
print(f'список после перестановки макс и мин значений {array}')
