"""
Problem Statement:
- Implement a function `find_second_maximum(lst)` which returns
    the second largest element in the list.

Input:
- A List
Output:
- Second largest element in the list

Sample Input:
[9,2,3,6]
Sample Output:
6
"""


def find_second_maximum(lst):
    if lst[0] > lst[1]:
        maximum = lst[0]
        second_maximum = lst[1]
    else:
        maximum = lst[1]
        second_maximum = lst[0]

    for x in lst:
        if x > maximum:
            second_maximum = maximum
            maximum = x
        elif x > second_maximum and x < maximum:
            second_maximum = x

    return second_maximum
