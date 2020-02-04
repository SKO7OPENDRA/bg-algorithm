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

# python -m timeit -n 1000 -s "import hw_4_1_v1"
# 1000 loops, best of 5: 10.3 nsec per loop


