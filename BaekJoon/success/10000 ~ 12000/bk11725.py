import sys


class TreeNode():
    def __init__(self, value=None):
        self.value = value
        self.child = []
        self.parent = None
        self.childLen = 0
        self.link = []
        self.linkLen = 0

    def addLink(self, other):
        self.link.append(other)
        self.linkLen += 1

    def delLink(self, other):
        for i in range(0, self.linkLen):
            if other.value == self.link[i].value:
                del self.link[i]
                self.linkLen -= 1
                return True
        return False

    def makeSelfParent(self):
        for _ in range(0, self.linkLen):
            self.link[0].parent = self
            self.link[0].delLink(self)
            self.addChild(self.link[0])
            del self.link[0]
            self.linkLen -= 1

    def addChild(self, other):
        self.child.append(other)
        self.childLen += 1

    def addParent(self, other):
        self.parent = other

    def getParent(self):
        return self.parent

    def subChild(self, other):
        for i in range(0, self.childLen):
            if other.value == self.child[i].value:
                del self.child[i]
                self.childLen -= 1
                return True
        return False

    def isChild(self, other):
        for i in range(0, self.childLen):
            if other.value == self.child[i].value:
                return True
        return False

    def toString(self):
        retVal = "Parent : " + str(self.parent.value) + "\nChild : [" if self.parent != None else "Parent : None\nChild : ["
        for i in range(0, self.childLen):
            retVal += str(self.child[i].value) + " "
        retVal += "]\n"
        return retVal

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    treeNode = []
    for i in range(0, N):
        treeNode.append(TreeNode(value=(i + 1)))
    makeUpQueue = [treeNode[0]]

    for _ in range(0, N-1):
        inp = sys.stdin.readline().rstrip().split(" ")
        n1 = int(inp[0]) - 1
        n2 = int(inp[1]) - 1
        treeNode[n1].addLink(treeNode[n2])
        treeNode[n2].addLink(treeNode[n1])
    
    while len(makeUpQueue) != 0:
        makeUpQueue[0].makeSelfParent()
        makeUpQueue += makeUpQueue[0].child
        del makeUpQueue[0]
    
    for i in range(1, len(treeNode)):
        print(treeNode[i].parent.value)
