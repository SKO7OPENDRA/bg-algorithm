from random import random


N = 15
arr = [0] * N

for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')

print()
mx = 0
mn = 0

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

# python -m timeit -n 1000 -s "import hw_4_1_v2"
# 1000 loops, best of 5: 12.4 nsec per loop