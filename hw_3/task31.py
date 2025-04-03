import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.rows, self.cols = self.data.shape

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы имеют разные размеры для сложения")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы имеют разные размеры для покомпонентного умножения")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй для матричного умножения")
        return Matrix(np.matmul(self.data, other.data))

    def __str__(self):
        return str(self.data)

    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt="%d")

# Сгенерируем две случайные матрицы размером 10x10 с помощью np.random.randint
np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

# Выполним все три операции
matrix_sum = matrix1 + matrix2
matrix_mult = matrix1 * matrix2
matrix_matmul = matrix1 @ matrix2

# Сохраним результаты в текстовые файлы
matrix_sum.save_to_file("matrix+.txt")
matrix_mult.save_to_file("matrix_mult.txt")
matrix_matmul.save_to_file("matrix@.txt")
