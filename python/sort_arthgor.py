def insertion_sort(lst):

    n = len(lst)

    for i in range(1, n):

        value = lst[i]

        j = i - 1

        while j >= 0 and lst[j] > value:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = value

    return lst

def selection_sort(lst):

    n = len(lst)

    for i in range(n - 1):
        imin = i
        for j in range(i + 1, n):
            if lst[j] < lst[imin]:
                imin = j

        lst[i], lst[imin] = lst[imin], lst[i]

    return lst

def bubble_sort(lst):

    n = len(lst)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if lst[j] > lst[j + 1]:

                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


class node:

    def __init__(self, key) -> None:
        self.key = key
        self.next = None

class linked_list:

    def __init__(self) -> None:
        self.head = None

    def count_condition(self, con):
        count = 0
        curr = self.head

        while curr :

            if con(curr.key):
                count += 1
               
            curr = curr.next

        return count
    
def insert(ll, key):
    nodes = node(key)
    nodes.next = ll.head
    ll.head = nodes

def displayed(ll):
    x = ll.head
    while x != None:
        print(x.key, end=' ')
        x = x.next

    print()

ll = linked_list()
nodes = node(4)
n2 = node(3)
n3 = node(5)

ll.head = nodes
nodes.next = n2
n2.next = n3

print(ll.count_condition(lambda x : x > 2))
print(displayed(ll))
