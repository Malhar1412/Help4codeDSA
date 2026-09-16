class Tree:

    def __init__(self, data):
        self.data = data
        self.Tree_list = []

    def __str__(self, level=0):
        ret = " " * level + self.data + "\n"

        for child in self.Tree_list:
            ret += child.__str__(level + 1)

        return ret

    def addChild(self, child):
        self.Tree_list.append(child)


rootOBJ = Tree('Drinks')

hot = Tree('Hot')
cold = Tree('Cold')

rootOBJ.addChild(hot)
rootOBJ.addChild(cold)

tea = Tree('Tea')
coffee = Tree('Coffee')

hot.addChild(tea)
hot.addChild(coffee)

alco = Tree('Alco')
nonalco = Tree('Non-Alco')

cold.addChild(nonalco)
cold.addChild(alco)

print(rootOBJ)