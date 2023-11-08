import os


def empty_file(filename):  # проверка пуст ли файл.txt
    file_info = os.stat(filename)
    return file_info.st_size == 0
