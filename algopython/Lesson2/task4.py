# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/1OUxSmp4pRZcezHkVGFQxMaz6fyRfmgPF/view?usp=sharing


def another_half(n, q, res):
    if q == 0:
        return res
    else:
        res += n
        n /= -2
        return another_half(n, q - 1, res)


q_ty = int(input('Введите кол-во чисел в последовательности: '))
start = 1
result = 0
print(another_half(start, q_ty, result))
