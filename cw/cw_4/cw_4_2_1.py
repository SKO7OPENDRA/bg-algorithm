# Рекурсивный поиск чисел Фибаначи
#
# Числа Фибаначи.
# Индекс:   [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] ...  [n]
# Значение: [0] [1] [1] [2] [3] [5] [8] [13][21][34]...[F(n)]
# F(0)=0, F(1)=1, F(n)=F(n-1) + F(n-2)
# n>2, n принадлежит Z(целым числам)

# Реализуем алгоритм для нахождения числа по индексу в виде рекурсивной функции

import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # делаем цикс проверки ответа.
    for i, item in enumerate(lst):
        assert item == func(i)
    # assert будет сравнивать значение item и значение, которое принимает функция, получив на вход переменную i
    # Если значения совпали (т.е. функция вернула нужное значение числа Фибаначи, то всё ок. Если нет, то будет ошибка.
        print(f'test{i} OK')


def fib(n):
    if n<2:
        return n
    return fib(n - 1) + fib(n - 2)

cProfile.run('fib(20)')

# cProfile.run('fib(15)')
# 1976 function calls (4 primitive calls) in 0.001 seconds
# 1973 / 1    0.001   0.000   0.001   0.001   cw_4_2_1.py: 21(fib)

# cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.006 seconds
# 21891 / 1   0.006   0.000   0.006   0.006   cw_4_2_1.py: 21(fib)


# test_fib(fib)

# python -m timeit -n 1000 -s "import cw_4_2_1" "cw_4_2_1.fib(10)
# 1000 loops, best of 5: 31.3 usec per loop

# python -m timeit -n 1000 -s "import cw_4_2_1" "cw_4_2_1.fib(15)
# 1000 loops, best of 5: 332 usec per loop

# python -m timeit -n 1000 -s "import cw_4_2_1" "cw_4_2_1.fib(20)
# 1000 loops, best of 5: 3.74 msec per loop

# python -m timeit -n 1000 -s "import cw_4_2_1" "cw_4_2_1.fib(25)
# 1000 loops, best of 5: 41.1 msec per loop



# По итогу проверки алгоритма, он получился экспоненциальным, так как время на его выполнение растет в геометрической прогрессии.