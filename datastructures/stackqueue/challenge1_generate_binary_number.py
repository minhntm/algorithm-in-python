"""
Problem Statement:
- Implement a function find_bin(n) which will generate binary numbers
    from 1 till n in the form of a string using a queue. The MyQueue()
    and MyStack() classes are provided in all of these challenges.
    An illustration is also provided for your understanding.

Input:
- A positive integer n
Output:
- Returns binary numbers in the form of strings from 1 up to n

Sample Input:
- n = 3
Sample Output:
- result = ["1","10","11"]
"""
from Queue import MyQueue


def find_bin(number):
    result = []
    queue = MyQueue()
    queue.enqueue('1')
    for i in range(number):
        result.append(queue.dequeue())
        queue.enqueue(result[i] + '0')
        queue.enqueue(result[i] + '1')

    return result


if __name__ == '__main__':
    print(find_bin(2))
