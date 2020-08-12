"""
Problem Statement:
- You have to implement the MinStack class which will have a min() function.
    Whenever min() is called, the minimum value of the stack is returned
    in O(1) time. The element is not popped from the stack.
    Its value is simply returned.

Output:
- Returns minimum number in O(1) time
Sample Output:
# min_stack = [9, 3, 1, 4, 2, 5]
# min_stack.min()
1
"""


from .Stack import MyStack


class MinStack:
    # Constructor
    def __init__(self):
        self.main_stack = MyStack()
        self.min_stack = MyStack()

    def pop(self):
        if self.main_stack.is_empty():
            return -1
        self.min_stack.pop()
        return self.main_stack.pop()

    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.top() > value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.top())
        print(self.min_stack.top())

    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.top()
