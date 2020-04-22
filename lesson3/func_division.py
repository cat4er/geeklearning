# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

a = input('Введите число: ')
b = input('Введите число: ')


def f_division(c, d):
    try:
        c = float(c)
        d = float(d)
        k = c / d
        l = d / c
        return k, l
    except ZeroDivisionError:
        print('ERROR: На ноль делить нельзя')
    except ValueError:
        print('ERROR: Введено некорректное значение')




print(f_division(a, b))
