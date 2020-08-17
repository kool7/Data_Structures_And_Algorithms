
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
    def __init__(self, head):
        self.head = None