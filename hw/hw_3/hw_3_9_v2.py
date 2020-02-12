import random
import sys

M = 10
N = 5
min_item = 0
max_item = 10

PRINT_MATRIX = False
SHOW_VARS = True
DETAIL = False


MATRIX = [[random.randint(min_item, max_item) for _ in range(N)] for _ in range(M)]
print(MATRIX)


if PRINT_MATRIX:
    for row in MATRIX:
        for element in row:
            print(f'{element:>4}', end='')
        print('')


def trace_func(frame, event, arg):

    if event == "return":
        global us_memory

        for key in frame.f_locals.keys():

            size = var_size(frame.f_locals[key])
            us_memory += size

            if SHOW_VARS:
                print(f'{key} {type(frame.f_locals[key])}: {size}')

            if DETAIL:
                print('')

    return trace_func


def var_size(x, level=0):
    res = sys.getsizeof(x)

    if DETAIL:
        print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}')

    if hasattr(x, '__iter__'):

        if hasattr(x, 'items'):
            for key, value in x.items():
                res += var_size(key, level + 1)
                res += var_size(value, level + 1)

        elif not isinstance(x, str):
            for item in x:
                res += var_size(item, level + 1)

    return res