class Node:
    def __init__(self, data):
        self.data = data      # value
        self.next = None      # next node pointer


class LinkedList:
    def __init__(self):
        self.head = None      # starting node

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head   # new node → old head
        self.head = new_node        # head update

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete(self, key):
        temp = self.head

        # if head itself is to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")