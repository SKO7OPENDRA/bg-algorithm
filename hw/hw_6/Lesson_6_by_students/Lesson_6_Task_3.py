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

list1 = []
for i in range(2, 10):
    count = 0
    for number in range(2, 100):
        if number % i == 0:
            count += 1
    list1.insert(0, i)
    list1.insert(1, count)
    print(f'Числу {list1.pop(0)} кратны {list1.pop(0)} чисел')

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


show_size_orig(list1)
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


print(f'Объект list1 занимает {show_size(list1)} байт')

# 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] win32

#  type = <class 'list'>, size = 64, object = []
# Объект list1 занимает 64 байт

# ОБЩИЙ ВЫВОД
# В 1-м варианте используется список списков размерностью 2х8. Соответсвенно
# для хранения результатов выделяется 1216 байт.
# 2-й вариант использует словарь под который выделяется 816 байт.
# 3-й вариант кода является наилучшим, т.к. для хранения результатов
# используется список из двух элементов. При каждой итерации элементы
# перезатираются. 3-й вариант использует 64 байта памяти.
