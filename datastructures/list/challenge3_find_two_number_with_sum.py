"""
Problem Statement:
- In this problem, you have to implement the find_sum(lst,k) function
    which will take a number k as input and return two numbers that add up to k

Input:
- A list and a number k
Output:
- A list with two integers a and b that add up to k

Sample Input:
- lst = [1,21,3,14,5,60,7,6]
- k = 81
Sample Output:
- lst = [21,60]
"""


def find_sum(lst, k):
    d = {}
    for x in lst:
        if x in d:
            return [x, d[x]]
        else:
            d[x] = k - x
            d[k-x] = x

    return []


if __name__ == '__main__':
    print(find_sum([1, 2, 3, 4], 5))
    print(find_sum([1, 2, 3, 4], 2))
