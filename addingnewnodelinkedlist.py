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
         nodeValue.next=self.head
         self.head=nodeValue
    def addnodeatend(self,value):
        nodeValue = Node(value)
        if self.head is None:
            self.head= nodeValue
            self.tail= nodeValue
        else:
         nodeValue.next=self.head
         self.head=nodeValue    
    def display(self):
        while self.head != None:
            print("[",self.head.data,"]","->>",end=" ")                                    
        
          
Linkedobj = LinkedList()
Linkedobj.addNodeBegginning(10)
Linkedobj.addNodeBegginning(5)
Linkedobj.addnodeatend(200)
Linkedobj.display()
    
        