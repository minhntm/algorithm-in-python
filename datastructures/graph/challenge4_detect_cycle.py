"""
Problem Statement:
- The concept of loops or cycles is very common in graph theory.
    A cycle exists when you traverse the directed graph and come upon a vertex
    that has already been visited.
    You have to implement the detect_cycle function which tells you
    whether or not a graph contains a cycle.

Input:
- A directed graph.
Output:
- True if a cycle exists. False if it doesn’t.

Sample Input:
    graph = {
        0 -> 1 
        1 -> 2
        2 -> 0
    }
Sample Output:
- True
"""


from collections import deque
from Graph import Graph


def detect_cycle(g): 
    visited = [False] * g.vertices
    q = deque()
    q.append(0)
    while q:
        v = q.pop()
        if visited[v]:
            return True
        visited[v] = True
        adjacent = g.array[v].get_head()
        while adjacent:
            q.append(adjacent.data)
            adjacent = adjacent.next_element

    return False


if __name__ == '__main__':
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)
    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    print(detect_cycle(g2))
