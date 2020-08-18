"""
Problem Statement:
- In the find_nth() function, a certain N is specified as an argument.
    You simply need to return the node which is N spaces away from
    the `None` end of the linked list.

Input:
- A linked list and a position *N*.
Output:
- The value of the node *n* positions from the end.
    Returns -1 if *n* is out of bounds.

Sample Input:
- LinkedList = 22->18->60->78->47->39->99 and n = 3
Sample Output:
- 47
"""
from LinkedList import LinkedList


def find_nth(lst, n):
    length = 1
    pointer1 = None
    pointer2 = lst.get_head()

    while pointer2:
        if length == n:
            pointer1 = lst.get_head()
        pointer2 = pointer2.next_element
        if length > n:
            pointer1 = pointer1.next_element
        length += 1

    return pointer1.data if pointer1 else -1


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_head(21)
    lst.insert_at_head(14)
    lst.insert_at_head(7)
    lst.insert_at_head(8)
    lst.insert_at_head(22)
    lst.insert_at_head(15)

    lst.print_list()
    print(find_nth(lst, 5))
    print(find_nth(lst, 1))
    print(find_nth(lst, 10))
