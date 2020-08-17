# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
# между собой (оба являться минимальными), так и различаться.

from random import randint  # экономим память :)

SIZE = 1
MIN_ITEM = - 100
MAX_ITEM = 100
min_value_list = []
MIN_NUMB = 2
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array = [2, 2, 2, 2, 2]  # вероятность низка, программа выдаст два первых значения, которые равны другим
print(f'Первоначальный список {array}')

for q in range(MIN_NUMB):
    min_value_ind = None
    if len(array) >= MIN_NUMB:
        for i in range(len(array) - 1):  # - 1 чтобы не выходить из диапозона
            if i == 0:
                if array[i] < array[i + 1]:
                    min_value_ind = i
                else:
                    min_value_ind = i + 1
            elif array[min_value_ind] > array[i]:
                min_value_ind = i
        min_value_list.append(array.pop(min_value_ind))
    else:
        print(f'В вашем списке не хватает чисел для поиска {MIN_NUMB} минимальных')
        break
else:
    print(f'{MIN_NUMB} минимальных числа вашего списка {min_value_list}')


