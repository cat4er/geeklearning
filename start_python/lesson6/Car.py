# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed=None, color=None, name=None, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'{self.name}  поехала, скорость {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'{self.name}  остановилась')

    def turn(self, direction):
        print(f'{self.name}  повернула {direction}')

    def show_speed(self):
        print(f'{self.name} Ваша скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, trunk):
        super().__init__(speed, color, name)
        self.trunk = trunk

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} помедленней бричку, твой предел 60 км/ч')
        elif self.speed == 0:
            print('Машина припаркована')
        else:
            print('Скорость в норме')


class WorkCar(Car):
    def __init__(self, speed, color, name, cargo):
        super().__init__(speed, color, name)
        self.cargo = cargo

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} помедленней бричку, твой предел 40 км/ч')
        elif self.speed == 0:
            print('Машина припаркована')
        else:
            print('Скорость в норме')


class SportCar(Car):
    def __init__(self, speed, color, name, boosted):
        super().__init__(speed, color, name)
        self.boosted = boosted


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, siren):
        super().__init__(speed, color, name, is_police)
        self.siren = siren


s = SportCar(200, 'Red', 'Ferrari', True)
print(s.name)
s.go(150)
t = TownCar(61, 'Grey', 'Toyota Thundra', True)
t.show_speed()
t.turn('налево')
t.stop()
t.show_speed()
p = PoliceCar(0, 'Black&White', 'Ford', True, 'Off')
print(p.siren)
p.show_speed()
print(s.is_police)
w = WorkCar(39, 'Yellow', 'Ford', False)
print(w.cargo)
w.show_speed()
w.go(45)
w.show_speed()