"""
Problem Statement:
Implement a function, `find_first_unique(lst)` that returns
    the first unique integer in the list.

Input:
- A list of integers
Output:
- The first unique element in the list

Sample Input:
[9,2,3,2,6,6]
Sample Output:
9
"""


def find_first_unique(lst):
    is_unique = {}
    for i, v in enumerate(lst):
        if v in is_unique:
            is_unique[v] = False
        else:
            is_unique[v] = True

    for i, v in enumerate(lst):
        if is_unique[v]:
            return v
