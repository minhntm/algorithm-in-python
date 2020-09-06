class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMax(self):
        return self.heap[0] if self.heap else None

    def removeMax(self):
        if len(self.heap) == 1:
            return self.heap.pop()

        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self.heap.pop()
            self.__maxHeapify(0)
            return max

        return None

    def __percolateUp(self, index):
        parent = (index-1)//2
        if parent < 0:
            return

        if self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = \
                self.heap[index], self.heap[parent]
            self.__percolateUp(parent)

    def __maxHeapify(self, index):
        left = 2*index + 1
        right = 2*index + 2
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = \
                self.heap[index], self.heap[largest]
            self.__maxHeapify(largest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in reversed(range(len(arr)//2)):
            self.__maxHeapify(i)


if __name__ == '__main__':
    heap = MaxHeap()
    print(heap.getMax())
    heap.insert(12)
    heap.insert(10)
    heap.insert(-10)
    heap.insert(100)
    print(heap.getMax())
    heap.removeMax()
    print(heap.getMax())

    heap.buildHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(heap.heap)
