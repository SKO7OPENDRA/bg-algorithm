import cProfile
import timeit
from random import random


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


# python -m timeit -n 1000 -s "import hw_4_1_v3"
# 1000 loops, best of 5: 9.3 nsec per loop

