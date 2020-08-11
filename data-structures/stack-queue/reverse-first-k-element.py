"""
Problem Statement:
- Implement the function reverseK(queue, k) which takes a queue and
    a number “k” as input and reverses the first “k” elements of the queue.
    An illustration is also provided for your understanding.

Output:
- The queue with first “k” elements reversed.
    Remember to return the queue itself!
    In case the value of “k” is larger than the size of the queue,
    is smaller than 0, or if the queue is empty, simply return None instead.

Sample Input:
- Queue = [1,2,3,4,5,6,7,9,10], k = 5
Sample Output:
- Queue = [5,4,3,2,1,6,7,8,9,10]
"""


from .Stack import MyStack


def reverseK(queue, k):
    if k > queue.size() or k < 0 or queue.is_empty():
        return None

    stack = MyStack()

    for i in range(k):
        stack.push(queue.dequeue())

    for i in range(k):
        queue.enqueue(stack.pop())

    for i in range(queue.size() - k):
        queue.enqueue(queue.dequeue())

    return queue
