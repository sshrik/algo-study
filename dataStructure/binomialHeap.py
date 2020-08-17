import heapq

class BinomialHeap():
    def __init__(self):
        self.order = []

    def insert(self, value):
        self.order.insert(0, Tree(value))
        
        self.addUp(1)

    def addUp(self, index):
        while index < len(self.order):
            if self.order[index - 1].nodeNum == self.order[index].nodeNum:
                # order에서 같은 index가 있으면 합친다.
                tree1 = self.order[index]
                tree2 = self.order[index - 1]
                del self.order[index - 1]
                del self.order[index - 1]

                merged_tree = merge_tree(tree1, tree2)
                self.order.insert(index - 1, merged_tree)
            else:
                break

    def insert_tree(self, tree):
        for i in range(0, len(self.order)):
            if self.order[i].nodeNum > tree.nodeNum:
                self.order.insert(i, tree)
                break
            elif self.order[i].nodeNum == tree.nodeNum:
                self.order.insert(i, tree)
                self.addUp(i + 1)
                break
            elif i == len(self.order) - 1:
                self.order.append(tree)
                

    def findLow(self):
        rootHeap = []

        # 각 Order의 최솟값을 Heap으로 정렬한 뒤 가장 작은 값을 return.
        for o in self.order:
            heapq.heappush(rootHeap, o.root.value)

        return rootHeap[0]
        
    def popLow(self):
        rootHeap = []
        
        # heap에 ( value, index )의 순서로 저장하여 가장 작은것을 찾는다.
        for i in range(0, len(self.order)):
            heapq.heappush(rootHeap, (self.order[i].root.value, i))
        
        # 가장 작은 값 return 값에 저장 및 가장 작은 값의 하위 Tree를 다시 합산.
        # 하위 tree들을 합산 할 때에는 nodeNum이 작은 것 부터 합산한다.
        smallest_index = rootHeap[0][1]
        child_node_num = []
        ret = self.order[smallest_index].root.value
        child = self.order[smallest_index].child
        # 가장 작은 값이 있는 order는 제거.

        del self.order[smallest_index]
        for i in range(0, len(child)):
            # 부모 node가 사라졌으므로 None 으로 초기화.
            child[i].parent = None
            heapq.heappush(child_node_num, (child[i].nodeNum, i))
        
        while child_node_num:
            self.insert_tree(child[heapq.heappop(child_node_num)[1]])
        
        return ret

    def printHeap(self):
        print(self.order)

def check_2_power(n):
    # n 이 2의 거듭제곱인지 확인. 
    return False if n == 0 else n & ( n - 1 ) == 0

def merge_tree(tree1, tree2):
    # 더 큰 root 값을 가진 tree를 다른 tree의 자식으로 추가.
    # 다만 나중의 연산을 편하게 하기 위해서 증가하는 순으로 자식을 추가하기로 한다.
    small = tree1 if tree1.root.value < tree2.root.value else tree2
    large = tree2 if tree1.root.value < tree2.root.value else tree1
    large.parent = small

    if not small.child:
        small.addChildWithTree(large)
    else:
        # 작은게 앞으로 오게 추가.
        for i in range(0, len(small.child)):
            if small.child[i].root.value >= large.root.value:
                small.addChildWithTree(large, i)
                break
    
    return small

class Node():
    def __init__(self, value):
        self.value = value

class Tree():
    def __init__(self, root, parent=None):
        self.child = []
        self.nodeNum = 1
        self.root = Node(root)
        self.parent = parent
    
    def addChildWithTree(self, tree, index=0):
        self.nodeNum += tree.nodeNum
        self.child.insert(index, tree)

    def addChild(self, value):
        self.nodeNum += 1
        self.child.append(Tree(v))

    def __repr__(self):
        ret = str(self.root.value) + " : " + str(self.child) if self.child else str(self.root.value)

        return ret
    
bh = BinomialHeap()
bh.insert(12)
bh.insert(31)
bh.insert(27)
bh.insert(34)
bh.insert(21)
bh.insert(10)
bh.insert(12)
bh.insert(31)
bh.insert(27)
bh.insert(34)
bh.insert(21)
bh.insert(10)
bh.printHeap()
bh.popLow()
bh.printHeap()
bh.printHeap()