# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
# Ссылка на диаграммы: https://drive.google.com/file/d/1Kan7g8csDHBAmjAHwLhqaUU-Xc_Z3rWJ/view?usp=sharing

letter1 = str(input('Введите любую букву английского алфавита: '))
letter2 = str(input('Введите любую другую букву английского алфавита: '))

num1 = ord(letter1)
num2 = ord(letter2)

place1 = num1 - 96
place2 = num2 - 96

if num1 > num2:
    q = num1 - num2 - 1
else:
    q = num2 - num1 - 1

print(f'Буква "{letter1}" в алфавите {place1}-ая, а "{letter2}" - {place2}-ая, между ними {q} букв(ы)')