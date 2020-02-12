import random
import sys

N = 13
M = 13
mn_i = 0
mx_i = 9

MATRIX = [[random.randint(mn_i, mx_i) for _ in range(N)] for _ in range(M)]

PRINT_MATRIX = False
SHOW_VARS = True
DETAIL = False

if PRINT_MATRIX:
    for row in MATRIX:
        for element in row:
            print(f'{element:>4}', end='')
        print('')


def trace_func(frame, event, arg):
    if event == "return":
        global ram

        for key in frame.f_locals.keys():

            size = var_size(frame.f_locals[key])
            ram += size

            if SHOW_VARS:
                print(f'{key} {type(frame.f_locals[key])}: {size}')

            if DETAIL:
                print('')

    return trace_func

#################################################################

def var_size(a, level=0):
    info = sys.getsizeof(a)

    if DETAIL:
        print('\t' * level, f'type={type(a)}, size={sys.getsizeof(a)}')

    if hasattr(a, '__iter__'):

        if hasattr(a, 'items'):
            for key, value in a.items():
                info += var_size(key, level + 1)
                info += var_size(value, level + 1)

        elif not isinstance(a, str):
            for item in a:
                info += var_size(item, level + 1)

    return info

#################################################################

def cache_optimized(matrix=MATRIX):
    min_array = [mx_i for _ in range(N)]

    for row in matrix:
        for i, el in enumerate(row):
            if min_array[i] > el:
                min_array[i] = el

    min_el = mn_i - 1

    for i in min_array:
        if i > min_el:
            min_el = i

    return min_el


# Для функции cache_optimized:
# .0 <class 'range_iterator'>: 24
# _ <class 'int'>: 14
# matrix <class 'list'>: 3732
# min_array <class 'list'>: 262
# row <class 'list'>: 278
# i <class 'int'>: 12
# el <class 'int'>: 14
# min_el <class 'int'>: 14
# Суммарный объем памяти 4350

funcs = [(cache_optimized, ())]

sys.settrace(trace_func)
for func, args in funcs:
    ram = 0
    print(f'Для функции {func.__name__}:')
    sys.call_tracing(func, args)
    print(f'Суммарный объем памяти {ram}\n')