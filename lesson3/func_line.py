# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.


def print_sum(nums):
    """ отображает сумму чисел из строки"""
    print(f'Сумма введеных чисел {sum(nums)}')


numbers = []
while True:
    """ булевый цикл, который запускает цикл проверки каждого элемента"""
    if numbers: print_sum(numbers)
    num_line = input('Введите числа через пробел и я верну их сумму или Q для заверешния программы: ').split()
    for num in num_line:
        """ проверяем нет ли Флюгегехаймен в строчке"""
        if num == 'Q':
            print_sum(numbers)
            exit()
        try:
            """конвертируем элементы из стороки в число с точкой, для того чтобы и целые числа подходили при вводе и 
            с точкой """
            numbers.append(float(num))
        except ValueError:
            """выводим ошибку, если по-русски читаем плохо"""
            print(f'ERROR: Введено некорректное значение {num}')
