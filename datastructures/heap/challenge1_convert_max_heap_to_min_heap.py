"""
Problem Statement:
- Implement a function convertMax(maxHeap) which will convert a binary Max-Heap
    into a binary Min-Heap. Where maxHeap is a list which is given in
    the maxHeap format, i.e, the parent is greater than its children.

Output:
- Returns converted list in string format

Sample Input:
- maxHeap = [9,4,7,1,-2,6,5]
Sample Output:
- result = [-2,1,5,9,4,6,7]
"""


def convertMax(maxHeap):
    for i in reversed(range(len(maxHeap)//2)):
        minHeapify(maxHeap, i)
    return maxHeap


def minHeapify(arr, index):
    left = index * 2 + 1
    right = index * 2 + 2
    smallest = index
    if len(arr) > left and arr[smallest] > arr[left]:
        smallest = left
    if len(arr) > right and arr[smallest] > arr[right]:
        smallest = right
    if smallest != index:
        arr[smallest], arr[index] = arr[index], arr[smallest]
        minHeapify(arr, smallest)


if __name__ == '__main__':
    maxHeap = [9, 4, 7, 1, -2, 6, 5]
    print(convertMax(maxHeap))
