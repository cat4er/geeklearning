# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
# не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число
# не отгадано, вывести правильный ответ.
# https://drive.google.com/file/d/1OUxSmp4pRZcezHkVGFQxMaz6fyRfmgPF/view?usp=sharing


import random

guess_num = 0   # счетчик числа попыток для разгадывания
guess_num_max = 10  # максимальное число попыток для разгадывания
min_num = 1
max_num = 100
number = random.randint(min_num, max_num)
print('Компьюетр загадал число между 1 и 100. Сможешь угадать?')


while guess_num < guess_num_max:

    guess = int(input('Введи число: '))
    guess_num += 1

    if guess < number:
        print(f'Отслось {guess_num_max - guess_num} попыток. Твое число меньше загаданного')
    elif guess > number:
        print(f'Отслось {guess_num_max - guess_num} попыток. Твое число больше загаданного.')
    else:
        print('Ты угадал!')
        exit()
print(f'Попытки закончились. Правильное число: {number}')