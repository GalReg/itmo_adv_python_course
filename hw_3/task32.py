import numpy as np

class Matrix:
    def __init__(self, data):
        # Инициализация объекта с использованием массива numpy
        self.data = np.array(data)
    
    # Getter для поля data
    @property
    def matrix(self):
        return self.data

    # Setter для поля data
    @matrix.setter
    def matrix(self, value):
        self.data = np.array(value)
    
    def __str__(self):
        return f"Matrix({self.data.shape[0]}x{self.data.shape[1]})\n{self.data}"

    # Сохранение матрицы в файл
    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt="%d")
    
    # Перегрузка арифметических операций
    def __add__(self, other):
        return Matrix(self.data + other.data)

    def __sub__(self, other):
        return Matrix(self.data - other.data)

    def __mul__(self, other):
        return Matrix(self.data * other.data)

    def __truediv__(self, other):
        return Matrix(self.data / other.data)

    def __matmul__(self, other):
        return Matrix(np.matmul(self.data, other.data))

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)

# Сгенерируем две случайные матрицы размером 10x10 с помощью np.random.randint
np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

# Выполним три операции
matrix_sum = matrix1 + matrix2
matrix_mult = matrix1 * matrix2
matrix_matmul = matrix1 @ matrix2

# Сохраним результаты в текстовые файлы
matrix_sum.save_to_file("matrix+.txt")
matrix_mult.save_to_file("matrix_mult.txt")
matrix_matmul.save_to_file("matrix@.txt")
