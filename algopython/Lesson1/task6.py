# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Ссылка на диаграммы: https://drive.google.com/file/d/1Kan7g8csDHBAmjAHwLhqaUU-Xc_Z3rWJ/view?usp=sharing

place = int(input('Введите номер любой из букв английского алфавита: '))

if place <= 26:
    num = place + 96
    letter = chr(num)
    print(f'{place}-ая буква в английском алфавите это "{letter}"')
else:
    print('Ошибка: в английском алфавите 26 букв')

