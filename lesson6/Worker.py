# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self):
        self.name = 'Виктор'
        self.surname = 'Павлюк'
        self.position = 'бизнес-аналитик'
        self._income = {"wage": 100000, "bonus": 30000}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход: {sum(self._income.values())}')

    def get_all_info(self):
        print(f'Сотрудник: {self.name} {self.surname}, должность {self.position}, доход: {sum(self._income.values())}')


p = Position()
print(p.name)
p.name = 'Виталий'
p.get_full_name()
p.get_total_income()
p.get_all_info()