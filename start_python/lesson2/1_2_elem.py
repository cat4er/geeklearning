# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Программа перемешивает элементы в списке')
elem_list = []
while True:
    elem = input('Ввведите список любой елемент, чтобы добавить его в список или start для запуска команды: ')
    if elem == 'start':
        break
    else:
        elem_list.append(elem)

# elem_list = ['Nike', 12, True, len, 17.3, [17, 'RPK']]  # список для тестирования
for el in range(0, len(elem_list), 2):
    if el == (len(elem_list) - 1):
        break
    else:
        elem_list.insert(el, elem_list[el + 1])
        elem_list.pop(el + 2)
print(elem_list)