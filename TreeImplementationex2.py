class Tree:

    # Creation of tree
    def __init__(self, data):
        self.data = data
        self.Tree_list = []


    # Display the tree
    def __str__(self, level=0):
        ret = " " * level + self.data + "\n"

        for child in self.Tree_list:
            ret += child.__str__(level + 1)

        return ret


    # Insertion of a node
    def addChild(self, child):
        self.Tree_list.append(child)


    # Deletion of a node
    def deleteChild(self, child):
        self.Tree_list.remove(child)


    # Search for a value
    def search(self, value):

        if self.data == value:
            return True

        for child in self.Tree_list:
            if child.search(value):
                return True

        return False


    # Traverse all nodes
    def traverse(self):

        print(self.data)

        for child in self.Tree_list:
            child.traverse()


    # Deletion of tree
    def deleteTree(self):
        self.Tree_list = []


# --------------------------------
# Creation of tree
# --------------------------------

n1 = Tree("n1")

n2 = Tree("n2")
n3 = Tree("n3")

n1.addChild(n2)
n1.addChild(n3)


n4 = Tree("n4")
n5 = Tree("n5")

n2.addChild(n4)
n2.addChild(n5)


n6 = Tree("n6")
n7 = Tree("n7")

n3.addChild(n6)
n3.addChild(n7)


n8 = Tree("n8")
n9 = Tree("n9")
n10 = Tree("n10")

n4.addChild(n8)
n4.addChild(n9)
n4.addChild(n10)


# --------------------------------
# Print tree
# --------------------------------

print("Tree:")
print(n1)


# --------------------------------
# Search
# --------------------------------

print("Search:")

print(n1.search("n5"))

print(n1.search("n11"))


# --------------------------------
# Traverse
# --------------------------------

print("Traverse:")

n1.traverse()


# --------------------------------
# Delete a node
# --------------------------------

n2.deleteChild(n5)

print("After deleting n5:")

print(n1)


# --------------------------------
# Delete tree
# --------------------------------

n1.deleteTree()

print("After deleting tree:")

print(n1)