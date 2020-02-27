# Что такое дерево
# Классификация дерева
# Создание деревьев в Python

# Самый простой способ создать дерево - создать свой собственный класс


from binarytree import tree, bst, Node, build

class MyNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

a = tree(height=4, is_perfect=False)
print(a)

b = bst(height=4, is_perfect=True)
print(b)

c = Node(7)
c.left = Node(3)
c.right = Node (1)
c.left = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
print(c)