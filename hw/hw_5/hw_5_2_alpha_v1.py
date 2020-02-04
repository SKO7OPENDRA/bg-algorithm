# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из
# примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.


import platform
import sys
import memory_profiler


def profile(func):
    """Decorator for run function profile"""

    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result

    return wrapper


def abs123(q):
    for i in range(len(q)):
        if q[i] == 'a':
            q[i] = 10
        elif q[i] == 'b':
            q[i] = 11
        elif q[i] == 'c':
            q[i] = 12
        elif q[i] == 'd':
            q[i] = 13
        elif q[i] == 'e':
            q[i] = 14
        elif q[i] == 'f':
            q[i] = 15
    return q


def to16(s):
    for i in range(len(s)):
        if s[i] == 10:
            s[i] = 'a'
        elif s[i] == 11:
            s[i] = 'b'
        elif s[i] == 12:
            s[i] = 'c'
        elif s[i] == 13:
            s[i] = 'd'
        elif s[i] == 14:
            s[i] = 'e'
        elif s[i] == 15:
            s[i] = 'f'
    return s


def sum16(x, y):
    z = []
    xx = abs123(x[::-1])
    yy = abs123(y[::-1])
    if len(xx) >= len(yy):
        for i in range(len(xx) - len(yy)):
            yy.append(0)
    else:
        for i in range(len(yy) - len(xx)):
            xx.append(0)
    p, zz, zzz = 0, 0, 0
    for i in range(len(xx)):
        zz = int(xx[i]) + int(yy[i]) + p
        if zz >= 16:
            p = zz // 16
            zzz = zz % 16
        else:
            zzz = zz
            p = 0
        z.append(zzz)
    if p > 0:
        z.append(p)
    # print(z, to16(z[::-1]))
    return to16(z[::-1])


def to10(x):
    xx = abs123(x)
    tenn = 0
    for i in range(len(xx)):
        ll = len(xx) - i - 1
        s = 16 ** ll
        ten = int(xx[i]) * s
        tenn += ten
    return tenn


def mul(x, y):
    dd = x
    for i in range(to10(y) - 1):
        dd = sum16(x, dd)
    return dd


@profile
def main():
    # a = input("\nВведите первое число в 16 формате: ")
    # b = input("Введите второе число в 16 формате: ")
    a = 'fff'
    b = 'fff'
    aa = list(a)
    bb = list(a)
    sum = sum16(aa, bb)
    print(f"\nСумма чисел {a} и {b}:")
    for i in sum:
        print(i, end="")
    dd = mul(aa, bb)
    print(f"\nПроизведение чисел {a} и {b}:")
    for i in dd:
        print(i, end="")
    print(f"\n\nцифры в десятичном формате:\na = {to10(aa)}\nb = {to10(bb)}\nsum = {to10(sum)}\nmul = {to10(dd)}\n\n")


if __name__ == '__main__':
    main()

print("\n\nДомашнее задание 6")

# cProfile.run('main()')

print("Версия Python - ", sys.version)
print("Разрядность ОС - ", platform.architecture())
# print("\n\nref number of a", sys.getrefcount(a))  # сколько ссылок у данной переменной
# print("a", asizeof.asizeof(a), type(a))  # сколько памяти потребляется переменной а
# # print(sys.getsizeof(a))
# print("aa", asizeof.asizeof(aa), type(aa), id(aa))  # сколько памяти потребляется переменной, тип, адреса памяти
# print("dd", asizeof.asizeof(dd), type(dd))  # сколько памяти потребляется переменной а
print("\nСтатистика по переменным\n")
totalsize = 0
for i in dir():
    w = str(type(eval(i)))
    if not i.startswith("_") and w != "<class 'module'>":
        print(
            f"адрес {id(i)}, {i}, размер {sys.getsizeof(eval(i))}, {type(eval(i))}, кол-во ссылок {sys.getrefcount(i)}")
        totalsize += sys.getsizeof(i)
print(f"Общий объем памяти для всех переменных {totalsize}")

# Чтобы получить имена:
#
# for name in vars().keys():
#   print(name)
# Чтобы получить значения:

# for value in vars().values():
#   print(value)

# @profile - сделать для всех примеров (см. в доп материалах к уроку) https://python-scripts.com/cprofile-code-profiling
# узнать как узнать весь объем занимаемый программой и сколько занимает