# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, item_name):
        self.item_name = item_name

    @property
    def ready(self):
        return f'{self.item_name} готов(о), приезжайте, забирайте!'

    @abstractmethod
    def cloth_intake(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        super().__init__(item_name='пальто')
        self.v = int(v)

    @property
    def cloth_intake(self):
        intake = self.v / 6.5 + 0.5
        return f'Затраты на {self.item_name} составили {intake:.2f}'


class Suit(Clothes):
    def __init__(self, h):
        super().__init__(item_name='костюм')
        self.h = int(h)

    @property
    def cloth_intake(self):
        intake = self.h * 2 + 0.3
        return f'Затраты на {self.item_name} составили {intake:.2f}'


p = Suit(2.4)
print(p.cloth_intake)
print(p.ready)

c = Coat(3)
print(c.cloth_intake)
print(c.ready)