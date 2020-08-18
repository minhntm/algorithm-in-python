
from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input directed graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}
# Depth First Traversal of Graph "g" from source vertex

# recursion method
def dfs_traversal(g, source):
    visited = [False] * g.vertices
    result = traverse(g, source, visited)
    for i in range(len(visited)):
        if not visited[i]:
            result += str(i)
    return result

def traverse(g, source, visited):
    adjacent = g.array[source].get_head()
    result = ''
    if not visited[source]:
        result = str(source)
        visited[source] = True
    while adjacent:
        result += traverse(g, adjacent.data, visited)
        adjacent = adjacent.next_element
    return result
