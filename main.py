import os
import argparse
import multiprocessing

# Функция для поиска ключевого слова в файле
def search_keyword_in_file(file_path, keyword):
    print(file_path, keyword)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if keyword in content:
            print(f"Ключевое слово найдено в файле: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Поиск ключевого слова в файлах")
    parser.add_argument("keyword", help="Ключевое слово для поиска")
    parser.add_argument("path", help="Путь к каталогу с файлами")

    args = parser.parse_args()

    # Получите список файлов в каталоге
    file_list = [os.path.join(args.path, filename) for filename in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, filename))]

    # Создайте пул процессов
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # Используйте метод map для запуска функции поиска в нескольких процессах
    pool.starmap(search_keyword_in_file, [(file, args.keyword) for file in file_list])

    # Завершите пул процессов
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()

