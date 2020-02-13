# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# while True:
#     try:
#         a = input("Введите ваш возраст: ")
#         if int(a) < 18:
#             print("Доступ запрещен.")
#             break
#         elif int(a) >= 18:
#             print("Доступ разрешен.")
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         continue

while True:
    a = input("Введите возраст: ")
    if not a.isnumeric():
        continue
    else:
        a = int(a)
        break
if a < 18:
    print("Доступ запрещен.")
elif a >= 18:
    print("Доступ разрешен.")
