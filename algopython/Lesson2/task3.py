# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# https://drive.google.com/file/d/1OUxSmp4pRZcezHkVGFQxMaz6fyRfmgPF/view?usp=sharing


num = int(input('Введите натуральное число: '))
mun = 0
while num > 0:
    mun = mun * 10 + num % 10
    num = num // 10
print(mun)