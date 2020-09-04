# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
from operator import itemgetter

txt = input('Введите любое слово или предложение для кодировки Хаффманом: ')
# txt = 'beep boop beer!'


def make_counter(string):  # первый шаг. сделать коллекцию по возраcтанию из заданной строки
    string_count = Counter(string)
    return string_count.most_common()[::-1]  # сортируем по возрастанию


# print(make_counter(txt))  # [('!', 1), ('r', 1), ('o', 2), (' ', 2), ('p', 2), ('b', 3), ('e', 4)]


def create_massive(mass):
    while len(mass) != 1:
        mass.append(([mass[0][0], mass[1][0]], mass[0][1] + mass[1][1]))  # добавляем в конец значения после соединения
        mass.pop(0), mass.pop(0)  # удаляем значения, которые уже соединили
        mass.sort(key=itemgetter(1))  # сортируем массив по второму атрибуту кортежа
    return mass[0][0]  # передаем массив без кортежа, дальше он не нужен


# print(create_massive(make_counter(txt)))  # [['b', 'e'], [['o', ' '], ['p', ['!', 'r']]]]
# print(len(create_massive(make_counter(txt))))  # 2


def make_arch_char(mass, step=''):  # функция  умеет с любой глубины достать индекс элемента
    global byte_dict  # создаем глобальный словарь для того, чтобы потом при необходимости декодировать
    for i in range(len(mass)):
        if isinstance(mass[i], str):  # если находим строчное выражение
            _byte_char = {mass[i]: step + str(i)}  # то к ранее добавленным шагам(индексам) добавляем текущеее
            byte_dict.update(_byte_char)  # и отправляем результат в словарь кодирования
            # print(_byte_char)
        if isinstance(mass[i], list):  # если находим вложение (словарь)
            make_arch_char(mass[i], step + str(i))  # то отправляем в функцию повторно, добавляя ранние шаги
    return byte_dict


byte_dict = {}  # глобальный словарик для компрессии и декомпрессии


# print(make_arch_char(create_massive(make_counter(txt))))  # {'b': '00', 'e': '01', 'o': '100', ' ': '101',
# 'p': '110', '!': '1110', 'r': '1111'}


def huffman_coding(string):
    _result_bytes = ''
    _byte_dict = (make_arch_char(create_massive(make_counter(string))))  # запускаем последовательно все функции
    for i in string:
        _result_bytes += (_byte_dict.get(i))  # находим по ключу (букве) и добавляем в результирующую строку бит
    return _result_bytes


dict_byte = {}


def huffman_decoding(string):
    step = ''
    global dict_byte
    dict_byte = {v: k for k, v in byte_dict.items()}  # переворачиваем ключи и значения, создаем словарь декодирования
    _result_text = ''
    for i in string:
        if step not in dict_byte:
            step += i  # так как длина ключа разная, я накопливаю их в переменной до того момента пока не найду
            if step in dict_byte:
                _result_text += (dict_byte.get(step))  # находим по ключу (битам) и добавляем в результирующую строку
                step = ''
    return _result_text


print(huffman_coding(txt))
print(huffman_decoding(huffman_coding(txt)))
