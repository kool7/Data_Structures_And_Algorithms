'''
Program to remove duplicate from python linked list.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insert(self, head, data):
        p = Node(data)
        
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end = ' ')
            current = current.next

    def removeDuplicate(self, head):
        if head is None:
            return

        start = head
        while(start.next != None):
            if start.data == start.next.data:
                start.next = start.next.next
            else:
                start = start.next
        return head

# assigning solution class to an object
mylinkedlist = Solution()

# number of times ask user to take input
T = int(input())

# head --> None
head = None

# looping for T num of times
for i in range(T):
    data = int(input())
    head = mylinkedlist.insert(head, data)

# removing duplicate elements from LL
head = mylinkedlist.removeDuplicate(head)


# display elemets in LL
mylinkedlist.display(head)
            