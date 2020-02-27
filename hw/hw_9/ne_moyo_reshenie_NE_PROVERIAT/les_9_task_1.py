# 1. Определение количества различных подстрок с использованием
# хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(),
# sha1() или любой другой из модуля hashlib задача считается не решённой.


def substr_count(a: str):

    a = a.lower()
    subs_set = set()

    for i in range(len(a)):
        for j in range(len(a) - 1 if i == 0 else len(a), i, -1):
            subs_set.add(hash(a[i:j]))

    lenght = len(subs_set)
    return lenght


some_string = input('Введите строку латинскими буквами: ')

lenght_subs = substr_count(some_string)
print(f'Количество различных подстрок в строке {some_string}: {lenght_subs}')
