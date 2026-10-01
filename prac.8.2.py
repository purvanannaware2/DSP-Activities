# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Creating linked list
ll = DoublyLinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Doubly Linked List:")
ll.display()