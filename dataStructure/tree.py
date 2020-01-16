class TreeNode():
    def __init__(self, value=None):
        self.value = value
        self.child = []
        self.parent = None
        self.childLen = 0

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
