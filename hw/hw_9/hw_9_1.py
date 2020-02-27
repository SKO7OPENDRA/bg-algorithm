# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
# задача считается не решённой.


import hashlib


def substring(input_string):
    input_string = str(input_string).lower()
    length = len(input_string)
    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)
    return len(hash_set)


# any_string = 'hello'
# any_string = 'world'
any_string = 'hello world'

print(f'Количество различных подстрок в строке {any_string}: {substring(any_string)}')