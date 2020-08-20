#  Написать два алгоритма нахождения i-го по счёту простого числа.
#  Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее
#  простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».


from timeit import timeit


def sieve(n):
    s = n ** 2
    a = [0] * s
    for i in range(2, s):
        a[i] = i
    m = 2
    while m < s:
        if a[m] != 0:
            j = m * 2
            while j < s:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b[n - 1]


print(sieve(10000))
print(timeit('sieve(100)', number=1000, globals=globals()))  # 4.446809378999999
print(timeit('sieve(1000)', number=1000, globals=globals()))  # 659.904268133
# print(timeit('prime(10000)', number=1000, globals=globals()))  # даже не рискнул


def prime(n):
    lst = [2]
    for i in range(3, n ** 2, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        elif len(lst) == n:
            return lst[n - 1]
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            elif i % j == 0:
                break
        else:
            lst.append(i)


print(prime(10000))
print(timeit('prime(100)', number=1000, globals=globals()))  # 0.20413245100000002
print(timeit('prime(1000)', number=1000, globals=globals()))  # 4.496361867
print(timeit('prime(10000)', number=1000, globals=globals()))  # 110.48079933599999

# разница в 146 раз оптимальнее вариант не решета Эратосфена
