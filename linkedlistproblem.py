class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
def length(ll):
    count=0
    current=ll.head
    while current is not None:
        count+=1
        current=current.next
    return count

ll=LinkedList()
ll.head=Node(10)
second=Node(20)
third=Node(30)

ll.head.next=second
second.next=third

print(length(ll))
