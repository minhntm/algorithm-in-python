"""
Problem Statement:
Implement a function rearrange(lst) which rearranges the elements such that
    all the negative elements appear on the left and positive elements
    appear at the right of the list.
    Note that it is not necessary to maintain the order of the input list.
Generally zero is NOT positive or negative,
    we will treat zero as a positive integer for this challenge!
    So, zero will be placed at the right.

Output:
- A list with negative elements at the left and positive elements at the right

Sample Input:
- [10,-1,20,4,5,-9,-6]
Sample Output:
- [-1,-9,-6,10,20,4,5]
"""


def rearrange(lst):
    # most_left_pos = 0
    # for i in range(len(lst)):
    #     if lst[i] < 0:
    #         if i != most_left_pos:
    #             lst[i] = lst[most_left_pos]
    #         most_left_pos += 1
    # return lst

    return [x for x in lst if x < 0] + [x for x in lst if x >= 0]
