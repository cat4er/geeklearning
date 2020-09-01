# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.


class OwnError(Exception):
    txt = []

    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        try:
            OwnError.txt.append(int(self.elem))
        except ValueError:
            return 'ERROR: Введен не тот тип, введите целое число'
        else:
            return f'Добавлено число: {self.elem} в список {OwnError.txt}'


line = ''
while True:
    try:
        line = input('Введите целое число для добавления в строку или stop для остановки: ')
        if line == 'stop':
            print(f'Вы создали список из {len(OwnError.txt)} чисел: {OwnError.txt}')
            quit()
        else:
            raise OwnError(line)
    except OwnError as err:
        print(err)