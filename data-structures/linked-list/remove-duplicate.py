"""
Problem Statement:
- You will now be implementing the remove_duplicates() function.
    When a linked list is passed to this function, it removes any node
    which is a duplicate of another existing node.

Input:
- A linked list.
Output:
- A list with all the duplicates removed.

Sample Input:
- LinkedList = 1->2->2->2->3->4->4->5->6
Sample Output:
- LinkedList = 1->2->3->4->5->6
"""


def remove_duplicates(lst):
    dataset = set()
    cur_node = lst.get_head()
    prev_node = None

    while cur_node is not None:
        val = cur_node.data
        if val in dataset:
            prev_node.next_element = cur_node.next_element
        else:
            dataset.add(val)
            prev_node = cur_node
        cur_node = cur_node.next_element

    return lst
