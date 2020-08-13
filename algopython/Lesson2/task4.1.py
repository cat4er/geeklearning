# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/1OUxSmp4pRZcezHkVGFQxMaz6fyRfmgPF/view?usp=sharing


def another_half(n):
    n /= -2
    return n


res = 0
start_n = 1
q = int(input('Введите кол-во чисел в последовательности: '))

while q != 0:
    res = start_n + res
    start_n = another_half(start_n)
    q -= 1
print(res)