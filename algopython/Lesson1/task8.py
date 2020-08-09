# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# Ссылка на диаграммы: https://drive.google.com/file/d/1Kan7g8csDHBAmjAHwLhqaUU-Xc_Z3rWJ/view?usp=sharing

year = int(input('Введите год: '))

if year % 100 == 0 and year % 400 == 0:
    print(f'{year} - високосный год')
elif year % 4 == 0 and year % 100 != 0:
    print(f'{year} - високосный год')
else:
    print(f'{year} - невисокосный год')
