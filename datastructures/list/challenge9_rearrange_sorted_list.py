"""
Problem Statement:
- Implement a function called maxMin(lst) which will re-arrange the elements of
    a sorted list such that the first position will have the largest number,
    the second will have the smallest, and the third will have second largest,
    and so on. In other words, all the odd-numbered indices will have
    the largest numbers in the list in descending order and
    the even numbered indices will have the smallest numbers in ascending order

Input:
- A sorted list

Output:
- A list with elements stored in max/min form

Sample Input:
- lst = [1,2,3,4,5]
Sample Output:
- lst = [5,1,4,2,3]
"""


def max_min(lst):
    left = 0
    right = len(lst) - 1
    result = []

    while left < right:
        result.append(lst[right])
        right -= 1
        result.append(lst[left])
        left += 1

    if left == right:
        result.append(lst[right])

    return result


if __name__ == '__main__':
    print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
