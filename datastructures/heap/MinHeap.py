class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMin(self):
        return self.heap[0] if self.heap else None

    def removeMin(self):
        if len(self.heap) == 1:
            return self.heap.pop()

        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap.pop()
            self.__minHeapify(0)
            return max

        return None

    def __percolateUp(self, index):
        parent = (index-1)//2
        if parent < 0:
            return

        if self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = \
                self.heap[index], self.heap[parent]
            self.__percolateUp(parent)

    def __minHeapify(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        smallest = index

        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = \
                self.heap[index], self.heap[smallest]
            self.__minHeapify(smallest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in reversed(range(len(arr)//2)):
            self.__minHeapify(i)


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(12)
    heap.insert(10)
    heap.insert(-10)
    heap.insert(100)

    print(heap.getMin())
    print(heap.removeMin())
    print(heap.getMin())
    heap.insert(-100)
    print(heap.getMin())
