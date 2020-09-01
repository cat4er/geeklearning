# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = complex(a, b)

    def __str__(self):
        return f'Комплексное число: {self.z}'

    def __add__(self, other):
        return f'Сумма комплекс. чисел: {self.z + other.z}'

    def __mul__(self, other):
        return f'Частное комплекс. чисел: {self.z * other.z}'


z_1 = ComplexNumber(4, -2)
z_2 = ComplexNumber(7, 3)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)