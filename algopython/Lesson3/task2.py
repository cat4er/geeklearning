# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint  # экономим память :)

SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
even_numbers = []
counter = 0  # счетчик шага
for i in array:
    counter += 1
    if i % 2 == 0:
        even_numbers.append(counter - 1)  # - 1 так как отсчет индекса идет от 0
        # even_numbers.append(array.index(i)) #  если есть дубли в списки, то лажает
print(f'Для списка {array} четные числа находятся под индексами {even_numbers}')
