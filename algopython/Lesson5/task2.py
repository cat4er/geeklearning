# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция,
# элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque

HEX_2_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}
NUM_2_HEX = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
             13: 'D', 14: 'E', 15: 'F'}
HEX = 16


def add_null(a, b):
    if len(a) > len(b):
        for i in range(len(a) - len(b)):
            b.appendleft('0')
    elif len(a) < len(b):
        for i in range(len(b) - len(a)):
            a.appendleft('0')
    return a, b


x = list(input('Введите 1-е шестнадцатиричное число: ').upper())
y = list(input('Введите 2-е шестнадцатиричное число: ').upper())
# x = deque('A2')
# y = deque('C4F')


def sum_hex(a, b):
    result = deque()
    remember = 0
    a, b = add_null(a, b)[0], add_null(a, b)[1]
    for i in reversed(range(len(a))):  # идем в обратную сторону
        if HEX_2_NUM[a[i]] + HEX_2_NUM[b[i]] + remember >= HEX:
            result.appendleft(NUM_2_HEX[(HEX_2_NUM[a[i]] + HEX_2_NUM[b[i]] + remember) % HEX])
            if remember == 0:
                remember += 1
        else:
            result.appendleft(NUM_2_HEX[HEX_2_NUM[a[i]] + HEX_2_NUM[b[i]] + remember])
            remember = 0
    return result


print(sum_hex(x, y))


def multi_hex(a, b):
    result = deque()
    remember = 0
    count = 0
    a, b = add_null(a, b)[0], add_null(a, b)[1]
    for i in reversed(range(len(b))):
        subresult = ''
        subresult = subresult + count * '0'
        for y in reversed(range(len(a))):
            if HEX_2_NUM[a[y]] * HEX_2_NUM[b[i]] + remember >= HEX:
                subresult = subresult + (NUM_2_HEX[(HEX_2_NUM[a[y]] * HEX_2_NUM[b[i]] + remember) % HEX])
                remember = HEX_2_NUM[a[y]] * HEX_2_NUM[b[i]] // HEX
            else:
                subresult = subresult + (NUM_2_HEX[HEX_2_NUM[a[y]] * HEX_2_NUM[b[i]] + remember])
                remember = 0
        result.appendleft(subresult[::-1])
        count += 1
    while len(result) != 1:
        result.append(sum_hex(deque(result[0]), deque(result[1])))
        result.popleft()
        result.popleft()
    return result


print(multi_hex(x, y))