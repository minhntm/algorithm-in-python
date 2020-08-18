"""
You have written the reverse function, which takes a singly linked list and
    produces the exactly opposite list.

Input:
- A singly linked list.
Output:
- The reversed linked list.

Sample Input:
- LinkedList = 0->1->2->3-4
Sample Output:
- LinkedList = 4->3->2->1->0
"""
from LinkedList import LinkedList


def reverse(ll):
    if ll.is_empty():
        return None

    current_node = ll.get_head()
    previous = None
    next = None

    while current_node is not None:
        next = current_node.next_element
        current_node.next_element = previous
        previous = current_node
        current_node = next

    ll.head_node = previous
    return ll


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_head(6)
    lst.insert_at_head(4)
    lst.insert_at_head(9)
    lst.insert_at_head(10)
    lst.print_list()

    reverse(lst)
    lst.print_list()
