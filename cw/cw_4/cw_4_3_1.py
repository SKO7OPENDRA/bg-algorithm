# Поиск чисел Фибаначи с сохранением в list и в dict

# Для оптимизации будет использоваться технология мемоизации (memoization) - сохранение результатов выполнения функции
# для предотвращения повторных вычислений

import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'test{i} OK')


def fib_dic(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):