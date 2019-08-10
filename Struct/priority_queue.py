class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.length = 0
        self.heap_size = 0
# function queue

    def heapMaximum(self):
        return self.queue[0]

    def heapExtractMax(self):
        if self.heap_size < 1:
            print('Очередь пуста')
        else:
            max = self.queue[0]
            self.queue[0] = self.queue[self.heap_size - 1]
            self.heap_size = self.heap_size - 1
            self.maxHapify(0)
            return max

    def heapIncreaseKey(self, i, key):
        if key < self.queue[i - 1]:
            print("Новый ключ меньше текущего")
            return
        self.queue[i - 1] = key
        while i > 1 and self.getParent(i) < self.queue[i - 1]:
            t = self.queue[i - 1]
            self.queue[i - 1] = self.queue[self.getParentIndex(i) - 1]
            self.queue[self.getParentIndex(i) - 1] = t
            i = self.getParentIndex(i)

    def maxHeapInsert(self, key):
        self.heap_size = self.heap_size + 1
        self.queue.append(float('-inf'))
        self.heapIncreaseKey(self.heap_size, key)

    def buildMaxHeap_(self, array):
        self.heap_size = 1
        self.length = len(array)
        self.queue.append(array[0])
        for i in range(2, len(array)+1):
            self.maxHeapInsert(array[i - 1])
    # function heap

    def maxHapify(self, i):
        l = self.getLeft(i)
        r = self.getRigth(i)
        largest = -1
        if l <= self.heap_size and self.queue[l - 1] > self.queue[i - 1]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.queue[r - 1] > self.queue[largest - 1]:
            largest = r
        if largest != i:
            t = self.queue[i - 1]
            self.queue[i - 1] = self.queue[largest - 1]
            self.queue[largest - 1] = t
            self.maxHapify(largest)

    def buildMaxHeap(self, queue):
        self.queue = queue
        self.length = len(queue)
        self.heap_size = self.length
        for i in range(self.length // 2, 0, -1):
            self.maxHapify(i)

    def getLeftChild(self, i):
        return self.queue[2 * i - 1]

    def getRigthChild(self, i):
        return self.queue[2 * i]

    def getRigth(self, i):
        return 2 * i + 1

    def getLeft(self, i):
        return 2 * i

    def getParentIndex(self, i):
        return i // 2

    def getParent(self, i):
        return self.queue[i // 2 - 1]

    def printHeap(self):
        print(self.queue)


if __name__ == '__main__':
    array = [1, 3, 3, 2, 12, 3, 2]
    print(array)
    queue = PriorityQueue()
    queue.buildMaxHeap_(array)
    queue.printHeap()
