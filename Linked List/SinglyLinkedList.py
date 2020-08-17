
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linkedlist class
class Linkedlist:
    def __init__(self):
        self.head = None

    # insert new head node
    def insertHead(self, newNode):

        temporary = self.head
        self.head = newNode
        self.head.next = temporary
        del temporary

    # insert item at the end of the list
    def insertEnd(self, newtNode):
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
linkedlist.insertEnd(firstnode)
secondnode = Node('Chetan')
linkedlist.insertEnd(secondnode)
thirdnode = Node('Bhanuop')
linkedlist.insertHead(thirdnode)
linkedlist.printList()