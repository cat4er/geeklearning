# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import triangular


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
lst = [triangular(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Первоначальный список {lst}')


def merge(left_lst, right_lst):
    sorted_lst = []
    left_ind = right_ind = 0

    left_len, right_len = len(left_lst), len(right_lst)  # немного оптимизации по использованию len()

    for i in range(left_len + right_len):
        if left_ind < left_len and right_ind < right_len:
            if left_lst[left_ind] <= right_lst[right_ind]:
                sorted_lst.append(left_lst[left_ind])
                left_ind += 1
            else:
                sorted_lst.append(right_lst[right_ind])
                right_ind += 1
        elif left_ind == left_len:
            sorted_lst.append(right_lst[right_ind])
            right_ind += 1
        elif right_ind == right_len:
            sorted_lst.append(left_lst[left_ind])
            left_ind += 1

    return sorted_lst


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])
    return merge(left_list, right_list)


print(merge_sort(lst))