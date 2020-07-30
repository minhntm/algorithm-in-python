"""
Implement a function that removes all the even elements from a given list.
Name it remove_even(list).

Input:
- A list with random integers.
Output:
- A list with only odd integers

Sample Input:
- my_list = [1,2,4,5,10,6,3]
Sample Output:
- my_list = [1,5,3]
"""


def remove_even(list):
    return [x for x in list if x % 2 != 0]
