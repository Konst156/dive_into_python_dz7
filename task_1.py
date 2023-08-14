# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для
# var = диапазона[3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно
# var = передано.Далее
# счётчик файлов и расширение.


import os


def batch_rename_files(desired_name, num_digits, source_extension, target_extension, name_range=None):
    directory = os.getcwd()  # Текущая рабочая директория
    files = os.listdir(directory)  # Список файлов в директории

    # Фильтрация файлов по расширению исходного файла
    files = [file for file in files if file.endswith(source_extension)]

    # Проверка наличия диапазона сохраняемого оригинального имени
    if name_range is not None:
        start, end = name_range
        files = [file[start-1:end] for file in files]

    # Переименование файлов
    for i, file in enumerate(files):
        new_name = desired_name + str(i).zfill(num_digits) + target_extension
        os.rename(file, new_name)

# Пример использования функции
desired_name = "new_file"
num_digits = 3
source_extension = ".txt"
target_extension = ".docx"
name_range = (3, 6)

batch_rename_files(desired_name, num_digits, source_extension, target_extension, name_range)
