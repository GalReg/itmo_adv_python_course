import sys
from collections import deque

def print_last_lines(filename, lines_to_print=10):
    """Функция для вывода последних lines_to_print строк из файла."""
    with open(filename, 'r') as file:
        # Используем deque для чтения последних строк
        lines = deque(file, maxlen=lines_to_print)
        print(f'\n==> {filename} <==')
        for line in lines:
            print(line, end='')

def print_last_stdin(lines_to_print=17):
    """Функция для вывода последних lines_to_print строк из stdin."""
    lines = [] 

    try:
        while True:
            for line in sys.stdin:
                lines.append(line)  
    except KeyboardInterrupt:
        pass

    print("Результат:")
    # Выводим последние 17 строк
    for line in lines[-lines_to_print:]:
        print(line, end='')

def main():
    # Получаем аргументы командной строки
    files = sys.argv[1:]
    
    if files:
        # Если переданы файлы, обрабатываем их
        for filename in files:
            print_last_lines(filename, lines_to_print=10)
    else:
        # Если нет файлов, читаем из stdin
        print_last_stdin(lines_to_print=17)

if __name__ == '__main__':
    main()
