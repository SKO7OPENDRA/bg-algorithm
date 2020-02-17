# Сортировка выбором

# сложность: O(n**2)
# Устойчивсть: Устойчивая/неустойчивая
# Тип(категория): Выбором
# Потребление памяти: Не требует доп. памяти

# Найти наименьший элемент в неотсортированной части масиива
# Поменять его местами с первым элементом в неотсортированной части масиива
# Продолжать эти действия, пока весь массив не будет отсортирован.

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def selection_sort(array):

    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]
        print(array)

selection_sort(array)
print(array)