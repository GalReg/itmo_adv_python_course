import numpy as np
from typing import Tuple

class MatrixHashMixin:
    def __hash__(self) -> int:
        # Хэш-функция для матрицы с учётом формы и суммы элементов
        return hash((self.data.shape, np.sum(self.data)))

class Matrix(MatrixHashMixin):
    def __init__(self, data: np.ndarray):
        self.data = np.array(data)
        self._hash_cache = None
        self._product_cache = None

    def __str__(self) -> str:
        return f"Matrix({self.data.shape[0]}x{self.data.shape[1]})\n{self.data}"

    def save_to_file(self, filename: str) -> None:
        np.savetxt(filename, self.data, fmt="%d")

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if self._product_cache is None:
            self._product_cache = self.data @ other.data
        return Matrix(self._product_cache)

def generate_random_matrix(size: Tuple[int, int] = (5, 5), low: int = 0, high: int = 5) -> Matrix:
    # Генерация случайной матрицы заданного размера и диапазона значений
    return Matrix(np.random.randint(low, high, size))

def find_hash_collision(max_attempts: int = 100000) -> Tuple[Matrix, Matrix, Matrix, Matrix, Matrix, Matrix]:
    """
    Поиск коллизий хэш-функции для матриц с выполнением условий:
    1. hash(A) == hash(C)
    2. A != C
    3. A @ B != C @ D (при B == D)
    """
    # Инициализация одинаковых матриц B и D
    b = d = generate_random_matrix()
    
    for _ in range(max_attempts):
        a, c = generate_random_matrix(), generate_random_matrix()
        
        if hash(a) == hash(c) and not np.array_equal(a.data, c.data):
            ab, cd = a @ b, c @ d
            
            if not np.array_equal(ab.data, cd.data):
                return a, b, c, d, ab, cd
    
    raise RuntimeError(f"Не удалось найти коллизию после {max_attempts} попыток")

def save_results(matrices: Tuple[Matrix, ...], filenames: Tuple[str, ...]) -> None:
    # Сохранение матриц и их хэшей в файлы
    for matrix, filename in zip(matrices, filenames):
        matrix.save_to_file(filename)
    
    ab, cd = matrices[4], matrices[5]

    with open("hash.txt", "w") as f:
        f.write(f"hash(A) == hash(C): {hash(matrices[0]) == hash(matrices[2])}\n")
        f.write(f"hash(AB): {hash(ab)}\n")
        f.write(f"hash(CD): {hash(cd)}\n")

if __name__ == "__main__":
    np.random.seed(0)
    try:
        result = find_hash_collision()
        save_results(result, ("A.txt", "B.txt", "C.txt", "D.txt", "AB.txt", "CD.txt"))
    except RuntimeError as e:
        print(e)
