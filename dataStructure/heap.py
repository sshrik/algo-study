class MaxHeap():
    ROOT = 0

    def __init__(self, initValue=[]):
        self.value = []
        if len(initValue) != 0:
            for i in initValue:
                self.addValue(i)

    def addValue(self, v):
        '''
            v : value for add.
        '''
        self.value.append(v)
        index = len(self.value) - 1
        ret = self.calcParentValue(index)
        
        while ret:
            index = self.getParentIndex(index)
            ret = self.calcParentValue(index)
    
    def calcParentValue(self, index):
        pIndex = self.getParentIndex(index)
        # Compare with parents and if parents is not big as child, change it.
        if self.value[pIndex] < self.value[index]:
            temp = self.value[index]
            self.value[index] = self.value[pIndex]
            self.value[pIndex] = temp
            return True
        else:
            return False

    def removeValue(self):
        popValue = self.value[self.ROOT]
        self.value[self.ROOT] = self.value[-1]
        del self.value[-1]

        index = self.ROOT
        if self.getLargerChild(index):
            ret = self.calcLeftChildValue(index)
            index = self.getLeftChildIndex(index)
        else:
            ret = self.calcRightChildValue(index)
            index = self.getRightChildIndex(index)
        
        while ret:
            if self.getLargerChild(index):
                ret = self.calcLeftChildValue(index)
                index = self.getLeftChildIndex(index)
            else:
                ret = self.calcRightChildValue(index)
                index = self.getRightChildIndex(index)
        return popValue

    def calcLeftChildValue(self, index):
        # Compare with left child value and if parents is not big as child, change it.
        lcIndex = self.getLeftChildIndex(index)
        if lcIndex >= len(self.value):
            return False
        elif self.value[lcIndex] > self.value[index]:
            temp = self.value[index]
            self.value[index] = self.value[lcIndex]
            self.value[lcIndex] = temp
            return True
        else:
            return False

    def calcRightChildValue(self, index):
        # Compare with right child value and if parents is not big as child, change it.
        rcIndex = self.getRightChildIndex(index)
        if rcIndex >= len(self.value):
            return False
        elif self.value[rcIndex] > self.value[index]:
            temp = self.value[index]
            self.value[index] = self.value[rcIndex]
            self.value[rcIndex] = temp
            return True
        else:
            return False

    def getLargerChild(self, index):
        # If left is larger, return True, else False
        if self.getRightChildIndex(index) >= len(self.value):
            return True
        else:
            return self.value[self.getLeftChildIndex(index)] > self.value[self.getRightChildIndex(index)]

    def getParentIndex(self, index):
        if index == self.ROOT:
            return self.ROOT
        elif index % 2 == 0:
            return int(index / 2) - 1
        else:
            return int(index / 2)

    def getLeftChildIndex(self, index):
        return (index + 1) * 2 - 1
    
    def getRightChildIndex(self, index):
        return (index + 1) * 2
    
    def printHeap(self):
        '''
        for i in range(0, len(self.value)):
            print("Heap value [" + str(i) + "] is " + str(self.value[i]))
        '''
        print(self.value)

heap = MaxHeap([7, 5, 10, 20, 10, 23, 17, 20])
heap.printHeap()
print(heap.removeValue())
heap.printHeap()

import heapq

nums = [7, 5, 10, 20, 10, 23, 17, 20]
heap = []
for n in nums:
    heapq.heappush(heap, (-n, n))
for h in heap:
    print(h[1], end = ", ")