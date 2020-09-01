# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint

MIN_ITEM = -10
MAX_ITEM = 10
M = 2  # при M = 3 получается массив из 7 чисел, если они отсортированы по возраст то нам нужно эл 3
lst = [randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * M + 1)]
# lst = [1, 5, 3, 9, 7, -7, -7]

print(f'Первоначальный список {lst}')


def median(array):
    for j in range(len(array)):
        more_count = 0
        less_count = 0
        for i in range(len(array)):  # решение не универсальное, работает только для исходного уравнения 2m + 1
            if i == j:
                continue
            elif array[j] >= array[i]:
                more_count += 1
            elif array[j] <= array[i]:
                less_count += 1
        if more_count >= M and less_count >= M:
            return f'Элемент под индексом {j} со значением {array[j]} является медианой массива {array}'


print(median(lst))