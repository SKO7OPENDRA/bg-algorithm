'''
Как работает list
'''

#list - Упорядоченная изменяемая коллекция объектов произвольных типов, к которым можно обратиться по индексу.

lst = []
lst.append(1)
lst.extend([2,3,4])

print(lst)

# list.insert(i,a) - добавляет в позицию i число a

lst.insert(1,5)
print(lst)

last = lst.pop()
print(lst, last)