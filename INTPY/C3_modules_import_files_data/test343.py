import os


# Задание 3.4.3
#
# Сделайте функцию, которая принимает от пользователя путь
# и выводит всю информацию о содержимом этой папки.
# Для реализации используйте функцию встроенного модуля os.walk().
# Если путь не указан, то сравнение начинается с текущей директории.

def show_dir(path=None):
    start_path = path if path is not None else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print("Текущая директория", root)
        print("---")

        if dirs:
            print("Список папок", dirs)
        else:
            print("Папок нет")
        print("---")

        if files:
            print("Список файлов", files)
        else:
            print("Файлов нет")
        print("---")

        if files and dirs:
            print("Все пути:")
        for f in files:
            print("Файл", os.path.join(root, f))
        for d in dirs:
            print("Папка", os.path.join(root, d))
        print("===")



if __name__ == '__main__':
    show_dir()
