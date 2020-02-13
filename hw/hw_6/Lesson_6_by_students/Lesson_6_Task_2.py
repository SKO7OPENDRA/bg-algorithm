# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков. Проанализировать
# результат и определить программы с наиболее эффективным использованием
# памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным
# решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки)
# вставить в виде комментариев в файл с кодом. Не забудьте указать версию и
# разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество
# sys.getsizeof после каждой переменной, а проявили творчество, фантазию и
# создали универсальный код для замера памяти.

# Задача № 1 из Урока 3.
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

import sys

print(sys.version, sys.platform)

dict1 = {}
for i in range(2, 10):
    count = 0
    for number in range(2, 100):
        if number % i == 0:
            count += 1
    dict1.update({i: count})
for key, value in dict1.items():
    print(f'Числу {key} кратны {value} чисел')

print('=' * 20, '\n')


def show_size_orig(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size_orig(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size_orig(xx, level + 1)


show_size_orig(dict1)
print('=' * 20, '\n')


def show_size(x, level=0):   # level - для красивого вывода значений на экран
    result_size = sys.getsizeof(x)
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):  # if object => iterable
        if hasattr(x, 'items'):  # if object => dictionary
            for key, value in x.items(): # if dict => get evey key & value and send it to func
                result_size += show_size(key, level + 1)  # function - recursive !!!
                result_size += show_size(value, level + 1)
        elif not isinstance(x, str):  # if object also iterable but is not a string (string is also iterable)
            for item in x:
                result_size += show_size(item, level + 1)
    return result_size


print(f'Объект dict1 занимает {show_size(dict1)} байт')


# 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] win32

#  type = <class 'dict'>, size = 368, object = {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'int'>, size = 28, object = 49
# 	 type = <class 'int'>, size = 28, object = 3
# 	 type = <class 'int'>, size = 28, object = 33
# 	 type = <class 'int'>, size = 28, object = 4
# 	 type = <class 'int'>, size = 28, object = 24
# 	 type = <class 'int'>, size = 28, object = 5
# 	 type = <class 'int'>, size = 28, object = 19
# 	 type = <class 'int'>, size = 28, object = 6
# 	 type = <class 'int'>, size = 28, object = 16
# 	 type = <class 'int'>, size = 28, object = 7
# 	 type = <class 'int'>, size = 28, object = 14
# 	 type = <class 'int'>, size = 28, object = 8
# 	 type = <class 'int'>, size = 28, object = 12
# 	 type = <class 'int'>, size = 28, object = 9
# 	 type = <class 'int'>, size = 28, object = 11
# Объект dict1 занимает 816 байт
