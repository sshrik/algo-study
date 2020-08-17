import math
import heapq

class FibonacciHeap:
    def __init__(self):
        self.smallest_index = -1
        self.root_list = []
        self.node_num = 0
    
    def insert(self, value):
        self.root_list.insert(0, Tree(value))
        self.smallest_index += 1
        self.node_num += 1
        
        if self.root_list[self.smallest_index].root.value > value:
            self.smallest_index = 0
    
    def min(self):
        return self.root_list[self.smallest_index].root.value

    def union(self, index1, index2):
        tree1 = self.root_list[index1]
        tree2 = self.root_list[index2]
        merged_tree = merge_tree(tree1, tree2)
        if index1 > index2:
            del self.root_list[index1]
            del self.root_list[index2]
            self.root_list.insert(index2, merged_tree)
        else:
            del self.root_list[index2]
            del self.root_list[index1]
            self.root_list.insert(index1, merged_tree)
        
    def pop(self):
        ret = self.min()
        
        # 최솟값을 가지는 tree의 root를 삭제하고, 자식들을 root_list에 넣는다.
        child = self.root_list[self.smallest_index].child
        del self.root_list[self.smallest_index]

        for i in range(0, len(child)):
            child[i].parent = None
            self.root_list.insert(self.smallest_index + i, child[i])

        # 같은 degree를 가지는 tree 끼리는 합산한다.
        # 각각의 degree는 degree_list의 index로, 각 degree의 root_list의 index 는 degree_list의 값으로 표현.
        degree_max = math.ceil(math.log(self.node_num)/math.log(2))
        degree_list = [-1 for _ in range(0, degree_max)]
        marked_list = [False for _ in range(0, len(self.root_list))]

        while not check_all_true(marked_list):
            for i in range(0, len(self.root_list)):
                degree_i = len(self.root_list[i].child)
                if degree_list[degree_i] == -1:
                    degree_list[degree_i] = i
                    marked_list[i] = True
                else:
                    self.union(degree_list[degree_i], i)
                    # Init lists.
                    degree_list = [-1 for _ in range(0, degree_max)]
                    marked_list = [False for _ in range(0, len(self.root_list))]
                    break
        
        root_heap = []

        for i in range(0, len(self.root_list)):
            heapq.heappush(root_heap, (self.root_list[i].root.value, i))
        
        self.smallest_index = root_heap[0][1]

        return ret
    
    def printHeap(self):
        print(self.root_list)

def check_all_true(arr):
    for l in arr:
        if not l:
            return False
    return True

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
    
fh = FibonacciHeap()
fh.insert(20)
fh.insert(24)
fh.insert(1)
fh.insert(21)
fh.insert(12)
print(fh.min())
print(fh.pop())
fh.insert(1)
fh.insert(21)
fh.insert(1)
fh.insert(21)
print(fh.pop())
fh.printHeap()