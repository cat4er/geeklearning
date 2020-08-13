# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1OUxSmp4pRZcezHkVGFQxMaz6fyRfmgPF/view?usp=sharing

c = 0
n = 0
num = (input('Введите натуральное число: '))
for i in num:
    if int(i) % 2 == 0:
        c += 1
    else:
        n += 1
print(f'В числе {num} {n} нечетных цифр и {c} четных цифр')

