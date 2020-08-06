"""
Problem Statement:
- In this problem, you have to implement the is_balanced() function
    which will take a string containing only curly {}, square [],
    and round () parentheses. The function will tell us whether all
    the parentheses in the string are balanced or not.

    For all the parentheses to be balanced, every opening parenthesis must
    have a closing one. The order in which they appear also matters.
    For example, {[]} is balanced, but {[}] is not.

Input:
- A string consisting solely of (, ), {, }, [, and ]
Output:
- Returns False if the expression doesn’t have balanced parentheses.
    If it does, the function returns True.

Sample Input:
- exp = "{[({})]}"
Sample Output:
- True
"""

from Stack import MyStack


def is_balanced(exp):
    stack = MyStack()
    parenthese = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for c in exp:
        if c in parenthese and not stack.is_empty() \
           and stack.top() == parenthese[c]:
            stack.pop()
        else:
            stack.push(c)

    return stack.is_empty()
