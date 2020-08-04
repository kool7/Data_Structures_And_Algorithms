class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def print(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

first = Node("Kuldeep")
linkedlist = LinkedList()
linkedlist.insert(first)

second = Node("Chetan")
linkedlist.insert(second)

third = Node("Python")
linkedlist.insert(third)

linkedlist.print()