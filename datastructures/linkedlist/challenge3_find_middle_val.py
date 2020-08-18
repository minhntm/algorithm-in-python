"""
Problem Statement:
- You have to implement the `find_mid()` function which will take a linked list
    as an input and return the value of the middle node.
    If the length of the list is even, the middle value will occur at length/2.
    For a list of odd length, the middle value will be **length/2+1**.

Input:
- A singly linked list.
Output:
- The integer value of the middle node.

Sample Input:
- LinkedList = 7->14->10->21
Sample Output:
- 14
"""
from LinkedList import LinkedList


def find_mid(lst):
    if lst.is_empty():
        return None

    onestep = lst.get_head()
    twostep = lst.get_head()

    while twostep.next_element and twostep.next_element.next_element:
        onestep = onestep.next_element
        twostep = twostep.next_element.next_element
    return onestep.data


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_head(22)
    lst.insert_at_head(21)
    lst.insert_at_head(10)
    lst.insert_at_head(14)
    lst.insert_at_head(7)

    lst.print_list()
    print(find_mid(lst))
