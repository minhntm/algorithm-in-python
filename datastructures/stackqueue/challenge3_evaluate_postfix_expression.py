"""
Problem Statement:
- The usual convention followed in mathematics is the infix expression.
    Operators like + and * appear between the two numbers involved in
    the calculation:
    6 + 3 * 8 - 4
    Another convention is the postfix expression where the operators appear
    after the two numbers involved in the expression.
    In postfix, the expression written above will be presented as:

    6 3 8 * + 4 -
    The two digits preceding an operator will be used with that operator

    From the first block of digits 6 3 8,we pick the last two which are 3 and 8.
    Reading the operators from left to right, the first one is *. The expression now becomes 3 * 8
    The next number is 6 while the next operator is +, so we have 6 + 8 * 3.
    The value of this expression is followed by 4, which is right before -. Hence we have 6 + 8 * 3 - 4.
    Implement a function called evaluatePostFix() that will compute a postfix expression given to it as a string.

Input:
- A string containing a postfix mathematic expression.
    Each digit is considered to be a separate number, i.e.,
    there are no double digit numbers.
Output:
- A result of the given postfix expression.

Sample Input:
- exp = "921 * - 8 - 4 +" # 9 - 2 * 1 - 8 + 4
Sample Output:
- 3
"""
from Stack import MyStack


def evaluate_post_fix(exp):
    stack = MyStack()
    operators = ['+', '-', '*', '/']
    for i in exp:
        if i.isdigit():
            stack.push(int(i))
        elif i in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            res = operate(operand2, operand1, i)
            stack.push(res)

    return stack.pop()


def operate(operand1, operand2, operate):
    if operate == '+':
        return operand1 + operand2
    if operate == '-':
        return operand1 - operand2
    if operate == '*':
        return operand1 * operand2
    if operate == '/':
        return operand1 / operand2


if __name__ == '__main__':
    print("Result: " + str(evaluate_post_fix("921*-8-4+")))
