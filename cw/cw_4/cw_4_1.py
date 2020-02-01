import timeit

x = 2 + 2
print(timeit.timeit('x = 2 + 2'))
print(timeit.timeit('x=sum(range(10))'))

# cd cw/cw_4
# python -m timeit -n 100 -s "import cw_4"