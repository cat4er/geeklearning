# Пользователь вводит время в секундах.  Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input('Это программа преводчик из секунд в часы и минуты в формате чч:мм:сс.\n Введите число: '))

hour = time // 3600  # делим общее время на количество секунд в часе и выводим целое
minute = (time - hour * 3600) // 60  # отнимаем целые часы в секундах от общего времени и делим на минуту в секундах
second = time - hour * 3600 - minute * 60  # вычисляем остаток секунд

print(f'Мы тут посчитали и решили: {hour:02}.{minute:02}.{second:02}')