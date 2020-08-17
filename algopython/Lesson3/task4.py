# Определить, какое число в массиве встречается чаще всего.

from random import randint  # экономим память :)


SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_counter = 0
number = 0
# array = [5, 35, -7, 5, 34, 88, -7, 65, -7, 2]
print(f'Первоначальный список {array}')

for i in array:
    counter = 0
    for e in array:
        if i == e:
            counter += 1
            if counter > 1 and max_counter < counter:
                max_counter = counter
                number = e
if max_counter == 0:
    print('Все числа в одном экземпляре')
else:
    print(f'Число {number} встречается {max_counter} раз(а)')
