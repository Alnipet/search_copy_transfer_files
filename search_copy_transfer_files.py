#подключаем библиотеки для работы с файлами
import os, shutil
import time

"""генерация имён файлов в дереве каталогов.
Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов)"""
def CopyTransFile(pathFrom, pathIn, exp):
    n = 0
    for root, dirs, files in os.walk(pathFrom):
        for file in files:
            # проверяем расширение файла
            if file.endswith(exp):
                # путь к начальному файлу
                file_from = root + "\\" + file
                # путь в место назначения
                file_in = pathIn + "\\" + file
                print(file_from)
                # копируем файлы
                shutil.copy2(file_from, file_in)
                n += 1
    return print('Готово ! Найдено и скопировано: ', n, ' файлов')

print("Находим файлы с необходимым расширением в дереве папок и копируем их в другою папку")
time.sleep(3)
pathFrom = str(input("Введите путь к начальной папке: "))
pathIn = str(input("Введите путь к папке назначения: "))
exp = str(input("Введите расширение файлов (например .pdf): "))
CopyTransFile(pathFrom, pathIn, exp)
