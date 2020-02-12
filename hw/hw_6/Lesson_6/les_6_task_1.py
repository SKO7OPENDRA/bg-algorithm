#!/usr/bin/env python
# coding: utf-8

# ### Homework к уроку 6

# #### 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# #### Выбрана задача 3 из ДЗ урока 3: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

# In[1]:


import sys
print(sys.version, sys.platform)


# In[ ]:


#print(sys.getsizeof())
vars = '', '', ''
for i in vars print(sys.getsizeof(i))


# Вариант решения №1 (без индексов):

# In[14]:


from random import random

def array(n):
    arr = [0]*n
    for i in range(n):
        arr[i] = int(random()*n)
    mn = 0
    mx = 0
    for i in range(n):
        if arr[i] < arr[mn]:
            mn = i
        elif arr[i] > arr[mx]:
            mx = i
    b = arr[mn]
    arr[mn] = arr[mx]
    arr[mx] = b

    vars = 'arr', 'n', 'mn', 'mx', 'b'
    for i in vars: print(i, sys.getsizeof(i)) 
    
    return arr

array(10000)
print('Total', sys.getsizeof(array))


# arr 52
# n 50
# mn 51
# mx 51
# b 50
# Total 136

# Вариант решения №2 (с индексами):

# In[21]:


import random

def change_min_and_max(array):
    max_element = 0
    max_element_index = 0
    min_element = 0
    min_element_index = 0
    i = 0
    for num in array:
        if i == 0:
            max_element = num
            min_element = num
        else:
            if num > max_element:
                max_element = num
                max_element_index = i
            if num < min_element:
                min_element = num
                min_element_index = i
        i += 1
    array[max_element_index], array[min_element_index] = array[min_element_index], array[max_element_index]
    
    vars = 'max_element', 'max_element_index', 'min_element', 'mx', 'min_element_index', 'i', 'array'
    for i in vars: print(i, sys.getsizeof(i))
    
    return array

array = [random.randint(-1000, 1000) for j in range(100)]

change_min_and_max(array)
print('Total', sys.getsizeof(change_min_and_max))


# max_element 60
# max_element_index 66
# min_element 60
# mx 51
# min_element_index 66
# i 50
# array 54
# Total 136

# Вывод: По итогу оба варианта занимают равное количество памяти. Но вариант без индексов в ходе выполнения памяти требует меньше, потому он предпочтительней

# Из любопытства посмотрим как решается та же задача, но уже в двумерном массиве

# In[28]:


import random

matrix = [[random.randint(0, 100) for i in range(100)] for j in range(100)]
max = 0
min = 101

# Находим и сохраняем min, max элементы и их индексы

for i, line in enumerate(matrix):
    for j, item in enumerate(line):
        if item > max:
            max = item
            max_i = (i)
            max_j = (j)
        if item < min:
            min = item
            min_i = (i)
            min_j = (j)

# Смотрим найденное        
print('max= ', max)
print(max_i, max_j)
print('min= ', min)
print(min_i, min_j)
type(min_i)

# Выводим матрицу
for i in matrix:
    for j in i:
        print(f'{j:>5}', end='')
    print()

# Меняем эл-ты местами
spam = matrix[min_i][min_j]
matrix[min_i][min_j] = matrix[max_i][max_j]
matrix[max_i][max_j] = spam

# Проверяем
for i in matrix:
    for j in i:
        print(f'{j:>5}', end='')
    print()


# In[29]:


vars = 'matrix', 'max', 'min', 'max_i', 'max_j', 'min_i', 'min_j', 'spam'
for i in vars: print(i, sys.getsizeof(i))


# Результаты для массива 5х5:
# matrix 55
# max 52
# min 52
# max_i 54
# max_j 54
# min_i 54
# min_j 54
# spam 53

# In[ ]:


Результаты для массива 100х100 идентичны. Неясно почему:
matrix 55
max 52
min 52
max_i 54
max_j 54
min_i 54
min_j 54
spam 53

