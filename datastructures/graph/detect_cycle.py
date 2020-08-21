from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}

def detect_cycle(g): 
  visited = [False] * g.vertices
  q = MyQueue()
  q.enqueue(0)
  while not q.is_empty():
    v = q.dequeue()
    if visited[v]:
      return True
    visited[v] = True
    adjacent = g.array[v].get_head()
    while adjacent:
      q.enqueue(adjacent.data)
      adjacent = adjacent.next_element

  return False
  

