# from os import link
# class Node:
#     def __init__(
#         self, value
#     ):  # instance var   these class is resoncible for crating linked list
#         self.data = value  # [10|None] [30|None]data
#         self.next = None  # 101 102 103 addreshh


# class Linkedlist:
#     def __init__(self):
#         self.head = None  # none


# Linkedobj = Linkedlist()
# # creating independant nodes
# Linkedobj.head = Node(10)
# second = Node(20)
# third = Node(30)
# fourth=Node(40)
# # connecting a node
# Linkedobj.head.next=second   #adding second node addressof next node
# second.next =third
# third.next=fourth

# #display

#     print("[",Linkedobj.head.data,"]",Linkedobj.head.next,"->",end="")
#     Linkedobj.head = Linkedobj.head.next  
# while Linkedobj.head != None:

# ############################################


class Node:
    def __init__(self,value):
        self.data=value 
        self.next= None
class LinkedList:
    def __init__(self):
            
            self.head= None
            self.tail= None
            
    def addNodeBegginning(self,value):
        nodeValue = Node(value)
        if self.head is None:
            self.head= nodeValue
            self.tail= nodeValue
        else:
         nodeValue=self.head
         self.head=nodeValue
    def display(self):
        while self.head != None:
            print("[",self.head.data,"]","->>",end=" ")                                    
          
          
Linkedobj = LinkedList()
Linkedobj.addNodeBegginning(10)
Linkedobj.addNodeBegginning(5)

    
        