# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание кзадаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint  # экономим память :)


SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_negative_num = 0
negative_number = 0
counter = 0
print(f'Первоначальный список {array}')

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
    print('В списке нет отрицательных чисел')
else:
    print(f'Максимальный отрицательный элемент списка {max_negative_num}')

