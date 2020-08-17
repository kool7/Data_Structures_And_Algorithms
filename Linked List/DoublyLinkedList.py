
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
    def __init__(self, head):
        self.head = None
      
    # Insertion: At fronnt  
    def insertHead(self, newNode):

        newNode = Node(newNode)
        newNode.next = self.head
        newNode.prev = None

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode

    # Insertion: After a node
    def insertAfter(self, prevNode, newNode):
        
        if prevNode is None:
            print('This node doesn\'t exist')
            return 

        newNode = Node(newNode)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode

        if newNode.next is not None:
            newNode.next.prev = newNode

#########
# SCRIPT#
#########

