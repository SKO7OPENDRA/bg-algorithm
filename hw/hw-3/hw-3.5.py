# Максимальный отрицательный элемент массива
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#
# Задача поиска максимального отрицательного элемента массива не такая простая, как может показаться на первый взгляд.
#
# Введем переменную (условно назовем ее A) для хранения индекса максимального отрицательного элемента и присвоим ей
# значение, выходящее за пределы возможных индексов. Например, если индексация элементов начинается с нуля,
# то данной переменной можно присвоить значение -1 (можно присвоить 0, если индексация начинается с 1).
# Если в массиве вообще не будет найдено отрицательных элементов, то ее такое значение будет "сигнализировать" об этом.
#
# Перебираем массив в цикле. Если очередной элемент меньше нуля и значение переменной A равно -1, то значит,
# это первый встретившийся отрицательный элемент. Запоминаем его индекс в переменной A.
# Если же очередной элемент отрицательный, но A уже не содержит -1, то сравниваем значение текущего элемента с тем,
# которое содержится по индексу, хранимому в A. Если текущий элемент больше, то записываем его индекс в A.
#
# После завершения цикла проверяем, не равно ли значение A -1. Если не равно,
# то выводим индекс максимального отрицательного элемента массива и его значение.

from random import random

N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])