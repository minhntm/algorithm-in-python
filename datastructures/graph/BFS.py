from Graph import Graph
from Queue import MyQueue
# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex


def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    visited = [False] * num_of_vertices
    q = MyQueue()
    q.enqueue(source)

    while not q.is_empty():
        v = q.dequeue()
        if not visited[v]:
            result = result + str(v)
        node = g.array[v].get_head()
        while node is not None:
            q.enqueue(node.data)
            node = node.next_element

    return result
