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


def dfs_traversal(g, source):
    result = ''
    visited = [False] * g.vertices
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        v = stack.pop()
        if not visited[v]:
            result += str(v)
            visited[v] = True
        adjacent = g.array[v].get_head()
        while adjacent:
            stack.push(adjacent.data)
            adjacent = adjacent.next_element

    for i in range(len(visited)):
        if not visited[i]:
            result += str(i)

    return result
