class Node:
    def __init__(self, value):
        self.linked = []
        self.linkLength = []
        self.value = value

    def setLink(self, node, length, rec=True):
        self.linked.append(node)
        self.linkLength.append(length)

        ## link other side node.
        if rec:
            node.setLink(self, length, rec=False)
    
    def printSelf(self):
        for i in range(0, len(self.linked)):
            print("Value : " + str(self.value) + " is linked with " + str(self.linked[i].value) + " with length " + str(self.linkLength[i]))
    
class Graph:
    nodeList = []
    def __init__(self, valueList, linkA, linkB, lengthList):
        for v in valueList:
            self.nodeList.append(Node(v))
        
        for i in range(0, len(linkA)):
            # Set linkA[i] to linkB[i] with length lengthList[i]
            self.nodeList[linkA[i] - 1].setLink(self.nodeList[linkB[i] - 1], lengthList[i])
    
    def showGraph(self):
        for i in range(0, len(self.nodeList)):
            self.nodeList[i].printSelf()

def inputGraph():
    inp = input().split(" ")
    nodeNum = int(inp[0])
    rodeNum = int(inp[1])

    linkA = []
    linkB = []
    length = []

    for i in range(0, rodeNum):
        inp = input().split(" ")
        linkA.append(int(inp[0]))
        linkB.append(int(inp[1]))
        length.append(int(inp[2]))

    univ = Graph(range(1, nodeNum + 1), linkA, linkB, length)
    return univ