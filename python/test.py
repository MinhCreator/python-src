
class Node:
    
    def __init__(self, key = None):
        self.key = key
        self.next = None

class linked_list:

    def __init__(self):
        self.head = None

    def calc(self, condition):
        s = 0
        cur = self.head
        while cur:
    
            if condition(cur.key):
                s += 1
            cur = cur.next

        return s


def insert(lst: linked_list, key: int) -> None:
    n_node = Node(key)
    n_node.next = lst.head
    lst.head = n_node

def print_list(lst: linked_list) -> None:
    while lst.head is not None:
        print(lst.head.key, end=' ')
        lst.head = lst.head.next
    print()


lst = linked_list()
lst.head = Node(1)
next1 = Node(2)
next2 = Node(3)

lst.head.next = next1
next1.next = next2
def condition(key):

    return key > 1

# print_list(lst)
print(lst.calc(condition))