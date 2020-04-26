# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

# задание a и б)
"""бесконечное создание словаря со списком"""
dict_iter = {}

for el in count(3):
    if el > 10:
        break
    c = 0
    text = []
    for elem in cycle('да?'):
        c += 1
        text.append(elem)
        if c == 6:
            break
    dict_iter.update({el: text})
print(dict_iter)
