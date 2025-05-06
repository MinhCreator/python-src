class node:

    def __init__(self, key) -> None:
        self.key = key
        self.next = None

class ll:

    def __init__(self) -> None:
        self.head = None


    def count_with_condition(self,condition):
        counts = 0

        curr = self.head

        while curr: 

            if condition(curr.key):
                counts += 1

            curr = curr.next

        return counts
def insert(lst: ll, key: int) -> None:
    nodes = node(key)
    nodes.next = lst.head
    lst.head = nodes  


# init list
lst = ll()

# add new node 
nodes = node(3)
lst.head = nodes 
n1 = node(10)
n2 = node(4)
lst.head.next = n1
n1.next = n2
insert(lst,6)

print(lst.count_with_condition(lambda x : x > 1))