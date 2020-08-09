# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Ссылка на диаграммы: https://drive.google.com/file/d/1Kan7g8csDHBAmjAHwLhqaUU-Xc_Z3rWJ/view?usp=sharing

number = int(input('Введите целое трехзначное число: '))
a = number // 100
b = number // 10 % 10
c = number % 10
x = a + b + c
y = a * b * c
print(f'Сумма цифр трехзначного числа {number} = {x} \nПроизведение цифр трехзначного числа {number} = {y}')
