# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint
from timeit import timeit


SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 99
lst = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# lst = [9, 5, -3, 8, 0, 1, -2, 6, 7, -4]

print(f'Первоначальный список {lst}')


def bubble(array):
    n = 1
    while n < len(array):
        shift = 0  # считаем кол-во изменений в массиве
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                shift += 1
        if shift == 0:  # если изменений за цикл не было, то сортировка закончена, нет смысла дальше проверять
            break
        n += 1
    return array


# тестирование на порядке [9, 5, -3, 8, 0, 1, -2, 6, 7, -4]
# print(timeit('bubble(lst)', number=1000, globals=globals()))  # без оптимиз 0.015269753
# print(timeit('bubble(lst)', number=1000, globals=globals()))  # с оптимиз 0.0019130869999999973
print(bubble(lst))
