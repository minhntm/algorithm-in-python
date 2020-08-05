"""
Problem Statement:
    By definition, a loop is formed when a node in your linked list points to
    a previously traversed node.
    You must implement the `detect_loop()` function which will take a
    linked list as input and deduce whether or not a loop is present.

Input:
- A singly linked list.
Output:
- Returns `True` if the given linked list contains a loop.
    Otherwise, it returns `False`

Sample Input:
- LinkedList = 7->14->21->7 # Both '7's are the same node. Not duplicates.
Sample Output:
- True
"""


def detect_loop(lst):
    onestep = lst.get_head()
    twostep = lst.get_head()

    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element
        twostep = twostep.next_element.next_element
        if onestep == twostep:
            return True
    return False
