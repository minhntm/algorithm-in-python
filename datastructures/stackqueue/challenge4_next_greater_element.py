"""
Problem Statement:
- You must implement the next_greater_element() function.
    For each element i in a list, it finds the first element to its right
    which is greater than ii. For any element that such a value does not exist,
    the answer is -1.
    Note: The next greater element is the first element towards the right
    which is greater than the given element.
    For example, in the list [1, 3, 8, 4, 10, 5],
    the next greater element of 3 is 8 and the next greater element for 8 is 10

Input:
- An integer list.
Output:
- A list containing the next greater element of each element from the list

Sample Input:
- list = [4, 6, 3, 2, 8, 1]
Sample Output:
- result = [6, 8, 8, 8, -1, -1]
"""
from Stack import MyStack


def next_greater_element(lst):
    res = [-1 for x in lst]
    stack = MyStack()

    for i in range(len(lst) - 1, -1, -1):
        while not stack.is_empty() and stack.top() <= lst[i]:
            stack.pop()

        if not stack.is_empty():
            res[i] = stack.top()

        stack.push(lst[i])

    return res


if __name__ == '__main__':
    print(next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9]))
