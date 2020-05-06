# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        a = ''
        for i in self.matrix:
            a = a + str(i) + '\n'
        return a

    def __add__(self, other):
        for el in range(0, len(self.matrix)):
            for elem in range(0, len(self.matrix[el])):
                try:
                    self.matrix[el][elem] += other.matrix[el][elem]
                except IndexError:
                    self.matrix[el][elem] += 0
        return self


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix1_2 = Matrix([[1, 2], [7, 4], [5, 8]])
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(matrix1)
print(matrix2)
print(matrix3)

print(matrix1 + matrix1_2)
print(matrix3 + matrix1)
print(matrix1 + matrix3)
