def reverse_string(s):
    return s[::-1]
print(reverse_string("abcd"))


def reverstring(s):
    rev=""
    for ch in s:
        rev=ch+rev
    return rev
print(reverstring("sheela"))

def palindrome(s):
    cleaned=s.lower()
    return cleaned==cleaned[::-1]
print(palindrome("racecar"))
print(palindrome("sheela"))


# def count_char(s,ch):
#     count=0
#     for c in s:
#         if c==ch:
#             count+=1
#     return count
# print(count_char("programming","m"))


#linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node(10)
node2=node(20)
node3=node(30)

node1.next= node2
node2.next= node3
head=node1

def print_list(head):
    current=head
    while current is not None:
        print(current.data, end=" -> ")
        current=current.next
    print("none")

print(print_list(head))

def count_head(head):
    count=0
    current=head
    while current is not None:
        count+=1
        current=current.next
    return count
print("node count:",count_head(head))

def search_list(head,tar):
    current=head
    while current is not None:
        if current.data==tar:
            return True
        current=current.next
    return  False
print(search_list(head,0))

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(seld,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
