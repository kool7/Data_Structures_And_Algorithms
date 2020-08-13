
# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linkedlist class
class Linkedlist:
    def __init__(self):
        self.head = None

    # insert item at the end of the list
    def insert(self, newtNode):
        if self.head is None:
            self.head = newtNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newtNode
    # print contents of the linked list
    def printList(self):

        if self.head is None:
            print('List is empty')
            return

        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

firstnode = Node('Kuldeep')
linkedlist = Linkedlist()
linkedlist.insert(firstnode)
secondnode = Node('Chetan')
linkedlist.insert(secondnode)
thirdnode = Node('Bhanuop')
linkedlist.insert(thirdnode)
linkedlist.printList()