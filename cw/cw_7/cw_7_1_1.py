# Сортировка пузырьком

# сложность: O(n**2) - медленная
# Устойчивсть: Устойчивая. Если есть 2 одинаковх элемента, то сохраняется их порядок.
# Тип(категория): Обменная
# Потребление памяти: Не требует доп. памяти

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)  # shuffle создает перемешанный список
print(array)

n = 1
while n < len(array):  # пока занчение N меньше длины масива, сортировка продолжится
    for i in range(len(array) - n):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i] # меняем местами
    n += 1
    print(array)
print(array)
