"""
Problem Statement:
- Implement a function findKSmallest(lst,k) that takes an unsorted integer list
    as input and returns the “k” smallest elements in the list using a Heap.

Output:
- Returns integer list that contains the first k smallest elements
    from the given list.

Sample Input:
- lst = [9,4,7,1,-2,6,5]
- k = 3
Sample Output:
- [-2,1,4]
"""


from MinHeap import MinHeap


def findKSmallest(lst, k):
    min_heap = MinHeap()
    min_heap.buildHeap(lst)
    k_smallest_elem = [min_heap.removeMin() for i in range(k)]
    return k_smallest_elem


if __name__ == '__main__':
    lst = [9, 4, 7, 1, -2, 6, 5]
    k = 3
    print(findKSmallest(lst, k))
