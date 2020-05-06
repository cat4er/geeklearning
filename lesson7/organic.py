# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки
# (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
# исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __str__(self):
        return f'Сообщество клеток: {self.qty * "*"}'

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        if (self.qty - other.qty) > 0:
            return Cell(self.qty - other.qty)
        else:
            return 'Это сделать нельзя!'

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(self.qty // other.qty)

    def make_order(self, cells):
        line = ''
        for i in range(0, self.qty // cells):
            line += f'{"*" * cells}\\n'
        line += f'{"*" * (self.qty % cells)}'
        return line


cells1 = Cell(25)
cells2 = Cell(6)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells2 - cells1)
print(cells1 * cells2)
print(cells1 / cells2)
print(cells1.make_order(10))
print(cells2.make_order(4))