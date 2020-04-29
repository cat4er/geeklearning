# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

file = open('task5.txt', 'w')
nums = int(input('Сколько чисел нужно записать в файл? '))
for _ in range(0, nums):
    file.write(str(randint(0, 100)) + ' ')
file = open('task5.txt', 'r')
a = file.read().split()
for i in range(0, len(a)):
    a.insert(i, int(a[i]))
    a.pop(i + 1)
print(f'сумма чисел {a} равна {sum(a)}')
