from os import link
class Node:
    def __init__(
        self, value
    ):  # instance var   these class is resoncible for crating linked list
        self.data = value  # [10|None] [30|None]data
        self.next = None  # 101 102 103 addreshh


class Linkedlist:
    def __init__(self):
        self.head = None  # none


Linkedobj = Linkedlist()
# creating independant nodes
Linkedobj.head = Node(10)
second = Node(20)
third = Node(30)
fourth=Node(40)
# connecting a node
Linkedobj.head.next=second   #adding second node addressof next node
second.next =third
third.next=fourth

#display

while Linkedobj.head != None:
    print("[",Linkedobj.head.data,"]",Linkedobj.head.next,"->",end="")
    Linkedobj.head = Linkedobj.head.next  

