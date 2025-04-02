import sys

def wc_file(filename):
    """Функция для подсчёта строк, слов и байтов в файле."""
    lines_count = 0
    words_count = 0
    bytes_count = 0

    # Открываем файл для чтения
    with open(filename, 'r') as file:
        for line in file:
            lines_count += 1
            words_count += len(line.split())  # Разделение строки по пробелам для подсчёта слов
            bytes_count += len(line.encode('utf-8'))  # Подсчёт байтов в строке

    return lines_count, words_count, bytes_count

def wc_stdin():
    """Функция для подсчёта строк, слов и байтов из stdin."""
    lines_count = 0
    words_count = 0
    bytes_count = 0
    content = ""

    try:
        while True:
            for line in sys.stdin:
                content += line
                lines_count += 1
                words_count += len(line.split())  # Разделение строки по пробелам
                bytes_count += len(line.encode('utf-8'))  # Подсчёт байтов
    except KeyboardInterrupt:
        pass

    print("Результат:")
    return lines_count, words_count, bytes_count

def main():
    files = sys.argv[1:]

    total_lines = total_words = total_bytes = 0

    if files:
        # Если переданы файлы, обрабатываем их
        for filename in files:
            lines, words, bytes = wc_file(filename)
            total_lines += lines
            total_words += words
            total_bytes += bytes
            print(f"{lines:8} {words:8} {bytes:8} {filename}")
        
        # Выводим суммарную статистику
        print(f"{total_lines:8} {total_words:8} {total_bytes:8} total")

    else:
        # Если нет файлов, читаем из stdin
        lines, words, bytes = wc_stdin()
        print(f"{lines:8} {words:8} {bytes:8}")

if __name__ == '__main__':
    main()