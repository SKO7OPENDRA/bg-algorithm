# Закодируйте любую строку из трех слов по алгоритму Хаффмана.


from collections import Counter, deque


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffman_tree(s):
    assert len(s) > 0, "String must not be empty"
    counter = Counter(s)
    deq = deque(sorted(counter.items(), key=lambda x: x[1]))

    while len(deq) > 1:
        weight = deq[0][1] + deq[1][1]
        node = MyNode(left=deq.popleft()[0], right=deq.popleft()[0])

        for idx, itm in enumerate(deq):
            if weight > itm[1]:
                continue
            else:
                deq.insert(idx, (node, weight))
                break
        else:
            deq.append((node, weight))
    return deq[0][0]


def encode_tree(tree, encode_table, path=''):
    if not isinstance(tree, MyNode):
        encode_table[tree] = path
    else:
        encode_tree(tree=tree.left,  encode_table=encode_table, path=f'{path}0')
        encode_tree(tree=tree.right, encode_table=encode_table, path=f'{path}1')


my_string = input("Enter a string of 3 words: ")
my_tree = huffman_tree(my_string)
encode_dict = dict()

encode_tree(my_tree, encode_dict)

encoded_list = []

for ch in my_string:
    encoded_list.append(encode_dict[ch])

encoded_string = ''.join(encoded_list)

print(f'Encoded string: {encoded_string}')