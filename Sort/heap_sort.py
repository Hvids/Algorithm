class Heap:
    def __init__(self):
        self.array = []
        self.heap_size = 0
        self.length = 0

    def maxHapify(self, i):
        l = self.getLeft(i)
        r = self.getRigth(i)
        largest = -1
        if l <= self.heap_size and self.array[l-1] > self.array[i-1]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.array[r-1] > self.array[largest-1]:
            largest = r
        if largest != i:
            t = self.array[i-1]
            self.array[i-1] = self.array[largest-1]
            self.array[largest-1] = t
            self.maxHapify(largest)


    def heapSort(self):
        for i in range(self.length, 1, -1):
            t = self.array[i-1]
            self.array[i-1] = self.array[0]
            self.array[0] = t
            self.heap_size = self.heap_size - 1
            self.maxHapify(1)

    def buildMaxHeap(self, array):
        self.array = array
        self.length = len(array)
        self.heap_size = self.length
        for i in range(self.length // 2, 0, -1):
            self.maxHapify(i)

    def getLeftChild(self, i):
        return self.array[2 * i - 1 ]

    def getRigthChild(self, i):
        return self.array[2 * i]

    def getRigth(self,i):
        return 2*i +1
    def getLeft(self,i):
        return 2*i
    def getParent(self,i):
        return i//2

    def getParent(self, i):
        return self.array[i // 2]

    def printHeap(self):
        print(self.array)


if __name__ == '__main__':
    heap = Heap()
    array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(array)
    heap.buildMaxHeap(array)
    heap.heapSort()
    heap.printHeap()
