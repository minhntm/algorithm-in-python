"""
Problem Statement:
- Implement a function called sort_stack() which takes a stack and
    sorts all of its elements in ascending order such that when they are
    popped and printed, they come out in ascending order. So the element that
    was pushed last to the stack has to be the smallest.

Input:
- A stack of integers.
Output:
- The stack with all its elements sorted in descending order.

Sample Input:
- stack = [23, 60, 12, 42, 4, 97, 2]
Sample Output:
- result = [97, 60, 42, 23, 12, 4, 2]
# 2 was the value last pushed
"""
from Stack import MyStack


def sort_stack(stack):
    sub_stack = MyStack()

    if stack.is_empty():
        return stack

    while not stack.is_empty():
        if sub_stack.is_empty() or stack.top() >= sub_stack.top():
            sub_stack.push(stack.pop())
            continue

        val = stack.pop()
        while not sub_stack.is_empty():
            stack.push(sub_stack.pop())
        sub_stack.push(val)

    while not sub_stack.is_empty():
        stack.push(sub_stack.pop())
    return stack


if __name__ == '__main__':
    stack = MyStack()
    stack.push(2)
    stack.push(97)
    stack.push(4)
    stack.push(42)
    stack.push(12)
    stack.push(60)
    stack.push(23)

    sort_stack(stack)

    # Printing by popping
    print([stack.pop() for i in range(stack.size())])
