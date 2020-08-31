# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# MAC OS 10.15.5 (19F101)  x86_64
# Python 3.8.2

from random import randint
from timeit import timeit
import sys

SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100
lst = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Первоначальный список {lst}')


def max_negative(array):
    max_negative_num = 0
    negative_number = 0
    counter = 0
    for i in array:
        if i < 0:
            if counter == 0:
                negative_number = max_negative_num = i
            negative_number = i
            counter += 1
            for e in array:
                if 0 > e > negative_number >= max_negative_num:
                    max_negative_num = e
    if max_negative_num == 0:
        return 'В списке нет отрицательных чисел'
    else:
        return max_negative_num


# print(max_negative(lst))


def max_negative2(array):
    negative = []
    for i in array:
        if i < 0:
            negative.append(i)
    max_negative_num = max(negative)

    _variable = []  # подсчет переменных
    for i in dir():  # возвращает имена из локальной области программы
        if i[0] != '_' and not hasattr(locals()[i], '__name__'):  # отфильтровываем от кишок
            _variable.append(locals()[i])  # ну и добавляем в списко
    print('Использовано памяти через getsizeof: ', memory_usage(_variable))
    print('Использовано памяти через балагрку: ', show(_variable))
    return max_negative_num


# print(max_negative2(lst))


def max_negative3(array):
    n = max(filter(lambda n: n < 0, array))

    _variable = []  # подсчет переменных
    for i in dir():  # возвращает имена из локальной области программы
        if i[0] != '_' and not hasattr(locals()[i], '__name__'):  # отфильтровываем от кишок
            _variable.append(locals()[i])  # ну и добавляем в списко
    print('Использовано памяти через getsizeof: ', memory_usage(_variable))
    print('Использовано памяти через балагрку: ', show(_variable))
    return n


# print(max_negative3(lst))
# тайминг до внедрения подсчета переменных:
# print(timeit('max_negative(lst)', number=1000, globals=globals()))   # 0.0037196599999999996
# print(timeit('max_negative2(lst)', number=1000, globals=globals()))  # 0.001315651000000001
# print(timeit('max_negative3(lst)', number=1000, globals=globals()))  # 0.002341072999999999


def show(x):
    total_memory = 0
    for item in x:
        mem = sys.getsizeof(item)
        if hasattr(item, '__iter__') and not isinstance(item, str):
            if hasattr(item, 'keys'):
                for key, value in item.items():
                    mem += show([key]) + show([value])
            else:
                mem += show(item)
        total_memory += mem
    return total_memory


def memory_usage(array):
    total_memory = 0
    for i in array:
        total_memory = total_memory + sys.getsizeof(i)
    return total_memory


def local_var():
    _variable = []  # подсчет переменных
    for i in dir():  # возвращает имена из локальной области программы
        if i[0] != '_' and not hasattr(locals()[i], '__name__'):  # отфильтровываем от кишок
            _variable.append(locals()[i])  # ну и добавляем в списко
    print('Использовано памяти через getsizeof: ', memory_usage(_variable))
    print('Использовано памяти через балагрку: ', show(_variable))


# тайминг после внедрения  подсчета переменных:
# print(timeit('max_negative(lst)', number=1000, globals=globals()))   # 0.054074985000000006
# print(timeit('max_negative2(lst)', number=1000, globals=globals()))  # 0.04200433199999999
# print(timeit('max_negative3(lst)', number=1000, globals=globals()))    # 0.033799791999999995


print(max_negative(lst))
print(max_negative2(lst))
print(max_negative3(lst))
#
# Использовано памяти через getsizeof:  346
# Использовано памяти через балагрку:  626
# Использовано памяти через getsizeof:  382
# Использовано памяти через балагрку:  802
# Использовано памяти через getsizeof:  212
# Использовано памяти через балагрку:  492

# Вывод: вариант программы №2 оказался самым быстрым по скорости выполнения, но при этом занял наибольшее количество
# памяти, из-за исользования списков и дублирования переменных в них.
# Программа №1 оказалась самой медленной, но при этом сохранила в памяти меньше атрибутов за счет перезаписи.
# Прогамма №3 была несколько медленне, чем №2, но при этом все манипуляции выполняла налету, используя внутристроенные
# функции,сохраняя минимум переменных в памяти.
# Если б мне пришлось выбирать решение для прома, я бы выбрал вариант №3 за простоту и экономию ресурсов
