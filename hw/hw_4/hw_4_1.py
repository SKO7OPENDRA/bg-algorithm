# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#######################################################################################################################
# hw_4_1_v1

from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, mn, imx + 1, mx))
arr[imn], arr[imx] = arr[imx], arr[imn]

for i in range(15):
    print(arr[i], end=' ')
print()

print('===' * N)

# python -m timeit -n 1000 -s "import hw_4_1_v1"
# 1000 loops, best of 5: 10.3 nsec per loop


#######################################################################################################################
# hw_4_1_v2

N = 15
arr = [0] * N

for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')

print()
mn = 0
mx = 0

for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i

print('arr[%d]=%d arr[%d]=%d' % (mn+1, arr[mn], mx+1, arr[mx]))
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b

for i in range(15):
    print(arr[i], end=' ')
print()

print('===' * N)

# python -m timeit -n 1000 -s "import hw_4_1_v2"
# 1000 loops, best of 5: 12.4 nsec per loop


#######################################################################################################################
# hw_4_1_v3

def m_array():
    N = 15
    arr = [] * N
    for i in range(N):
        arr.append(int(random() * 100))
        print(arr[i], end=' ')
    print()

    imx = arr.index(max(arr))
    imn = arr.index(min(arr))
    min_m_array = min(arr)
    max_m_array = max(arr)

    arr[imn] = max_m_array
    arr[imx] = min_m_array
    print('arr[%d]=%d arr[%d]=%d' % (imn + 1, arr[imn], imx + 1, arr[imx]))
    return arr


print(*m_array())

print('===' * N)

# python -m timeit -n 1000 -s "import hw_4_1_v3"
# 1000 loops, best of 5: 9.3 nsec per loop


#######################################################################################################################

# По итогу проверки задача, написанная через функцию, оказалась быстрее всего.
# Вариант 1 - 10.3 nsec per loop
# Вариант 2 - 12.4 nsec per loop
# Вариант 3 - 9.3 nsec per loop