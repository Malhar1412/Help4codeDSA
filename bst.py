class BSTree:
    def __init__(self,data):
        self.data-data
        self.leftChild=None
        self.rightChild=None

def insertNode(rootNode,nodeValue):
    if rootNode.data==None:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:  #left child
        if rootNode.leftChild is None:
            nodeValue=BSTree (nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightCild is None:   #rightchild
            rootNode.rightChild=BSTree(nodeValue)
        else:
             insertNode(rootNode.rightchild,nodeValue)


def preOrderTravrsal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)   
    preOrderTravrsal(rootNode.leftChild)
    preOrderTravrsal(rootNode.rightChild) 



newBST=BSTree(None)
insertNode(BSTree,70)
insertNode(BSTree,50)
insertNode(BSTree,90)
insertNode(BSTree,30)

preOrderTravrsal(newBST)