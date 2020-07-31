"""
Problem Statement #
Implement a function right_rotate(lst, n) which will rotate
    the given list by k. This means that the right-most elements will
    appear at the left-most position in the list and so on.
    You only have to rotate the list by one element at a time.

Input:
- A list and a number by which to rotate that list

Output:
- The given list rotated by k elements

Sample Input:
lst = [10,20,30,40,50]
n = 3
Sample Output:
lst = [30,40,50,10,20]
"""


def right_rotate(lst, n):
    n = n % len(lst)

    # rotated_lst = []
    # for i in range(len(lst) - n, len(lst)):
    #     rotated_lst.append(lst[i])
    # for i in range(0, len(lst) - n):
    #     rotated_lst.append(lst[i])
    # return rotated_lst

    return lst[-n:] + lst[:-n]
