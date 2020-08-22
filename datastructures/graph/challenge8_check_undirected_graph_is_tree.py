"""
Problem Statement:
- The next section will tackle the tree data structure.
    For now, here’s the basic difference between a graph and a tree.
    A graph can only be a tree under two conditions:
        There are no cycles.
        The graph is connected.
    A graph is connected when there is a path between every pair of vertices.
    In a connected graph, there are no unreachable vertices. Each vertex must
    be connected to every other vertex through either a direct edge
    or a graph traversal.

    You have to implement is_tree() function which will take a graph as
    an input and find out if it is a tree.

Input:
- An undirected graph.
Output:
- Returns True if the given graph is a tree. Otherwise, it returns False.

Sample Input:
    graph = {
        0 - 1
        0 - 2
        0 - 3
        3 - 4  
    }
Sample Output:
- True
"""


from collections import deque
from Graph import Graph


def is_tree(g):
    visited = [False] * g.vertices

    q = deque()
    q.append((-1,0))

    while q:
        parent, v = q.popleft()
        visited[v] = True
        adjacent = g.array[v].get_head()
        while adjacent:
            if visited[adjacent.data] and adjacent.data != parent:
                return False
            if not visited[adjacent.data]:
                q.append((v, adjacent.data))
            adjacent = adjacent.next_element

    return all(visited)


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print(is_tree(g))
