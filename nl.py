import sys

def number_lines(input_file, output_file=sys.stdout):
    """
    Функция для нумерации строк из входного файла.
    
    Args:
        input_file: файловый объект для чтения (например, sys.stdin или открытый файл)
        output_file: файловый объект для записи (по умолчанию sys.stdout)
    """
    line_number = 1
    for line in input_file:
        # Форматируем строку с номером (6 символов с выравниванием по правому краю)
        numbered_line = f"{line_number:6d}\t{line}"
        output_file.write(numbered_line)
        line_number += 1

def main():
    # Проверяем, передан ли аргумент командной строки (имя файла)
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as file:
                number_lines(file)
        except FileNotFoundError:
            print(f"Ошибка: файл '{sys.argv[1]}' не найден", file=sys.stderr)
            sys.exit(1)
        except IOError:
            print(f"Ошибка ввода/вывода при работе с файлом '{sys.argv[1]}'", file=sys.stderr)
            sys.exit(1)
    else:
        # Если файл не передан, читаем из stdin
        number_lines(sys.stdin)

if __name__ == "__main__":
    main()