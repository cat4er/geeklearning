# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
# домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
# для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

from timeit import timeit
import cProfile


def half_rec(n, q):
    res = 0
    if q == 0:
        return res
    res = half_rec(n / -2, q - 1) + n
    return res


print(timeit('half_rec(1, 100)', number=1000, globals=globals()))  # 0.03565647499999999
print(timeit('half_rec(1, 200)', number=1000, globals=globals()))  # 0.04974719300000001
print(timeit('half_rec(1, 400)', number=1000, globals=globals()))  # 0.11921736499999999
print(timeit('half_rec(1, 800)', number=1000, globals=globals()))  # 0.23377471

cProfile.run('half_rec(1, 100)')
#  101/1    0.000    0.000    0.000    0.000 test:4(half_rec)
cProfile.run('half_rec(1, 200)')
#  201/1    0.000    0.000    0.000    0.000 test:4(half_rec)
cProfile.run('half_rec(1, 400)')
#  401/1    0.001    0.000    0.001    0.001 test:4(half_rec)
cProfile.run('half_rec(1, 800)')


#  801/1    0.002    0.000    0.002    0.002 test:4(half_rec)


def half_loop(n, q):
    res = 0
    while q != 0:
        res = n + res
        n /= -2
        q -= 1
    return res


print(timeit('half_loop(1, 100)', number=1000, globals=globals()))  # 0.013732843999999998
print(timeit('half_loop(1, 200)', number=1000, globals=globals()))  # 0.029302651
print(timeit('half_loop(1, 400)', number=1000, globals=globals()))  # 0.04876092
print(timeit('half_loop(1, 800)', number=1000, globals=globals()))  # 0.096378943

cProfile.run('half_loop(1, 100)')
#  1    0.000    0.000    0.000    0.000 test:4(half_loop)
cProfile.run('half_loop(1, 200)')
#  1    0.000    0.000    0.000    0.000 test:4(half_loop)
cProfile.run('half_loop(1, 400)')
#  1    0.000    0.000    0.000    0.000 test:4(half_loop)
cProfile.run('half_loop(1, 800)')
#  1    0.000    0.000    0.000    0.000 test:4(half_loop)


def another_half(n):
    n /= -2
    return n


def sum_half(n, res):
    res = res + n
    return res


def half_loop2(n, q):
    res = n
    for i in range(1, q):
        n = another_half(n)
        res = sum_half(n, res)
    return res


print(timeit('half_loop2(1, 100)', number=1000, globals=globals()))  # 0.030961019
print(timeit('half_loop2(1, 200)', number=1000, globals=globals()))  # 0.047924617999999995
print(timeit('half_loop2(1, 400)', number=1000, globals=globals()))  # 0.094560894
print(timeit('half_loop2(1, 800)', number=1000, globals=globals()))  # 0.194090221

cProfile.run('half_loop2(1, 100)')
#  1    0.000    0.000    0.000    0.000 test:14(half_loop2)
cProfile.run('half_loop2(1, 200)')
#  1    0.000    0.000    0.000    0.000 test:14(half_loop2)
cProfile.run('half_loop2(1, 400)')
#  1    0.000    0.000    0.000    0.000 test:14(half_loop2)
cProfile.run('half_loop2(1, 800)')
#   1    0.001    0.001    0.001    0.001 test:14(half_loop2)


# Замеры проведены для 100, 200, 400, 800
# Выводы:
# Наиболее оптимальный вариант оказался вариант 2 по скорости исполнения,
# т.к. вариант не содержит сложных математических вычислений и логических петель в отличии от рекурсии
# Однако у вариант 3 за счет разделения функций на отдельные блоки имеет преимущество за счет того,
# что другие части программы могут переиспользовать ее части, а значит в будущем возможно избежать повторения кода

