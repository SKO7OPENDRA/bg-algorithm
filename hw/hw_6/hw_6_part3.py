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

def with_transpose(matrix=MATRIX):
    info = float('-inf')
    tr_matrix = zip(*matrix)

    for tr_row in tr_matrix:

        min_el = tr_row[0]
        for el in tr_row:

            if el < min_el:
                min_el = el

        if info < min_el:
            info = min_el

    return info


# Для функции with_transpose:
# matrix <class 'list'>: 3732
# info <class 'int'>: 14
# tr_matrix <class 'zip'>: 36
# tr_row <class 'tuple'>: 258
# min_el <class 'int'>: 12
# el <class 'int'>: 14
# Суммарный объем памяти 4066

#################################################################

funcs = [(with_transpose, ())]

sys.settrace(trace_func)
for func, args in funcs:
    ram = 0
    print(f'Для функции {func.__name__}:')
    sys.call_tracing(func, args)
    print(f'Суммарный объем памяти {ram}\n')