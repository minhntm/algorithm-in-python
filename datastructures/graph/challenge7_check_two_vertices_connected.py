"""
Problem Statement:
- You have to implement the check_path() function. It takes a source vertex
    and a destination vertex and tells us whether or not a path
    exists between the two.

Input:
- A directed graph, a source value, and a destination value.
Output:
- Returns True if a path exists from the source to the destination.

Sample Input:
    graph = {
            0 -> 2
        0 -> 5
        2 -> 3
        2 -> 4
        5 -> 3
        5 -> 6
        3 -> 6
        6 -> 7
        6 -> 8
        6 -> 4
        7 -> 8
    }
    source = 0
    destination = 7
Sample Output:
- True
"""


from collections import deque
from Graph import Graph


def check_path(g, source, destination):
    visited = [False] * g.vertices
    stack = deque()
    stack.append(source)
    visited[source] = True
    while stack:
        v = stack.pop()
        if v == destination:
            return True
        adjacent = g.array[v].get_head()
        while adjacent:
            if not visited[adjacent.data]:
                stack.append(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next_element

    return False


if __name__ == '__main__':
    g1 = Graph(9)
    g1.add_edge(0, 2)
    g1.add_edge(0, 5)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(5, 3)
    g1.add_edge(5, 6)
    g1.add_edge(3, 6)
    g1.add_edge(6, 7)
    g1.add_edge(6, 8)
    g1.add_edge(6, 4)
    g1.add_edge(7, 8)
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)

    print(check_path(g1, 0, 7))
    print(check_path(g2, 3, 0))
