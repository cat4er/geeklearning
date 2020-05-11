# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.


class Store:
    my_store = []

    @staticmethod
    def show_depot():
        print('Наличие товара на складе: ')
        for el in Store.my_store:
            print(el)

    @staticmethod
    def move_dep(name, qty, name_dep):
        if Store.valid(name, qty, name_dep):
            for el in Store.my_store:
                for key, val in el.items():
                    if name == val:
                        if qty <= el['кол-во']:
                            el['кол-во'] -= qty
                            if el['кол-во'] == 0:
                                Store.my_store.remove(el)
                            return print(f'Позиция: {name}, кол-во: {qty} перемещена в подзразделение: {name_dep}')
                        else:
                            return print('На складе нет столько товара')
            return print('Такого товара нет на складе')

    @staticmethod
    def valid(name, qty, name_dep):
        if not(isinstance(name, str)):
            print('ERROR: Наименование должно быть строчным')
            return False
        elif not(isinstance(qty, int)):
            print('ERROR: Количество должно быть числом')
            return False
        elif not(isinstance(name_dep, str)):
            print('ERROR: Название подразделения должно быть строчным')
            return False
        return True


class OfficeDevices:
    _office_eq = []

    @staticmethod
    def show_office_eq():
        for el in OfficeDevices._office_eq:
            print(el)

    @staticmethod
    def move_depot():
        Store.my_store.extend(OfficeDevices._office_eq)
        print('Оргтехника перемещена на склад')

    def __init__(self, name, model, price, qty):
        self.name = name
        self.model = model
        self.price = price
        self.qty = qty


class Printer(OfficeDevices):
    def __init__(self, name, model, price, qty, tech_print):
        super().__init__(name, model, price, qty)
        self.tech_print = tech_print
        OfficeDevices._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.qty,
            'тип': self.tech_print
        })


class Scanner(OfficeDevices):
    def __init__(self, name, model, price, qty, sc_type):
        super().__init__(name, model, price, qty)
        self.sc_type = sc_type
        OfficeDevices._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.qty,
            'тип': self.sc_type
        })


class Xerox(OfficeDevices):
    def __init__(self, name, model, price, qty, x_type):
        super().__init__(name, model, price, qty)
        self.x_type = x_type
        OfficeDevices._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.qty,
            'тип': self.x_type
        })


x1 = Xerox('Fujitsa XX1', 'CC23456', 45000, 2, 'планшетный')
x2 = Xerox('Fujitsa XX2', 'CC23446', 45000, 1, 'портативный')
s1 = Scanner('Kodak Z1', 'XC6565', 13000, 3, 'цветной')
p1 = Printer('Kodak LJ125', 'MFP123', 45000, 4, 'лазерный')
OfficeDevices.show_office_eq()
OfficeDevices.move_depot()
Store.show_depot()
Store.move_dep('Kodak LJ125', 4, 'Юридический департамент')
Store.show_depot()
Store.move_dep('Fujitsa XX1', 3, 'Бухгалтерия')
Store.show_depot()
Store.move_dep('Kodak LJ125i', 5, 'Офис продаж')
Store.show_depot()
Store.move_dep('Kodak LJ125i', '5', 'Офис продаж')
Store.move_dep(123, 5, 'Офис продаж')
Store.move_dep('Kodak LJ125i', 5, 123)