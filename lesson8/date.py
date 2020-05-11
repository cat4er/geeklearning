# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    @classmethod
    def str2num(cls, date):
        try:
            num_date = [int(i) for i in date.split('-')]
        except ValueError:
            print('Формат должен был быть цифровым >>день-месяц-год<< и используйте "-"')
            quit()
        else:
            return num_date

    @staticmethod
    def validation(num_date):
        if not 1 <= num_date[0] <= 31:
            print(f'Error: В каком месяце у тебя {num_date[0]} дней?')
        elif not 1 <= num_date[1] <= 12:
            print(f'Error: По какому календарю живешь, что у тебя есть {num_date[1]} месяц?')
        elif not 1 <= num_date[1] <= 2020:
            print(f'Error: {num_date[2]} год?')
        else:
            return f'День:{num_date[0]} Месяц: {num_date[1]} Год: {num_date[2]}'


d = Date()
print(d.validation(d.str2num(input('Введите дату в формате день-месяц-год: '))))
