class Node():
    def __init__(self, num=None):
        self.childList = []
        self.number = num

    def addLink(self, v):
        self.childList.append(v)
        v.childList.append(self)
    
    def getChildNum(self):
        res = []
        for i in range(0, len(self.childList)):
            res.append(self.childList[i].number)
        return res

if __name__ == "__main__":
    N = int(input())
    
    nodeList = []

    for i in range(0, N):
        nodeList.append(Node(i))
    
    K = int(input())
    
    for i in range(0, K):
        inp = input().split(" ")
        nodeList[int(inp[0]) - 1].addLink(nodeList[int(inp[1]) - 1])
    
    inpected = [0]

    q = [0]
    while len(q) != 0:
        numList = nodeList[q[0]].getChildNum()
        for i in range(0, len(numList)):
            if numList[i] not in inpected:
                inpected.append(numList[i])
                q.append(numList[i])
        del q[0]
    
    print(len(inpected) - 1)
