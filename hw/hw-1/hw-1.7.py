# Определить високосный год или нет
# Определить, является ли год, который ввел пользователем, високосным или невисокосным.
#
# Високосные года делятся нацело на 4. Однако из этого правила есть исключение:
# столетия, которые не делятся нацело на 400, високосными не являются.
#
# В високосном годе 366 дней, в обычном 365.
#
# Если год не делится на 4, значит он обычный.
# Иначе надо проверить не делится ли год на 100.
# Если не делится, значит это не столетие и можно сделать вывод, что год високосный.
# Если делится на 100, значит это столетие и его следует проверить его делимость на 400.
# Если год делится на 400, то он високосный.
# Иначе год обычный.
# Проверки можно проводить последовательно, а можно группировать через логические
# операторы "И" и "ИЛИ". Поэтому способов решения задачи может быть несколько.

# 1-й вариант:

y = int(input())
if y % 4 != 0:
    print("Обычный")
elif y % 100 == 0:
    if y % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

# 2-й вариант:

if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print("Обычный")
else:
    print("Високосный")