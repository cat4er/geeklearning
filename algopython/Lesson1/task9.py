# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# Ссылка на диаграммы: https://drive.google.com/file/d/1Kan7g8csDHBAmjAHwLhqaUU-Xc_Z3rWJ/view?usp=sharing
print('Введите три разных числа.')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a > b:
    if a > c:
        if b > c:
            print(f'Среднее число {b}')
        else:
            print(f'Среднее число {c}')
    else:
        print(f'Среднее число {a}')
else:
    if a > c:
        print(f'Среднее число {a}')
    elif b > c:
        print(f'Среднее число {c}')
    else:
        print(f'Среднее число {b}')