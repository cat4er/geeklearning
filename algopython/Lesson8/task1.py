# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9


from hashlib import sha1

txt = input('Введите любое слово или предложение для подсчета подстрок: ')
# txt = 'papa'
# txt = 'a b'
# txt = 'sova'


def sum_subs(string):
    _my_set = set()
    j = 1
    while j != len(string):
        for i in range(0, len(string)):
            if sha1(string[i:i + j].encode('utf-8')).hexdigest() not in _my_set:
                _my_set.add(sha1(string[i:i + j].encode('utf-8')).hexdigest())
        j += 1
    return f'{len(_my_set)}'


print(sum_subs(txt))