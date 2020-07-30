"""
Implement a function that merges two sorted lists of m and n elements,
into another sorted list. Name it merge_lists(lst1, lst2).

Input:
- Two sorted lists.
Output:
- A merged and sorted list consisting of all elements of both input lists.

Sample Input:
list1 = [1,3,4,5]  
list2 = [2,6,7,8]

Sample Output:
arr = [1,2,3,4,5,6,7,8]
"""


def merge_lists(lst1, lst2):
    result = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    result.extend(lst1[i:])
    result.extend(lst2[j:])

    return result
