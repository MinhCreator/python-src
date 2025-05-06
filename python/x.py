class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def count_nodes_with_condition(self, condition):
        count = 0
        current = self.head
        while current:
            if condition(current.data):
                count += 1
            current = current.next
        return count


# Usage
# Create a linked list
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third


# Define your condition
def condition(data):
    return data > 1

print(
    "Number of nodes in the linked list that satisfy the condition:",
    llist.count_nodes_with_condition(condition),
)

