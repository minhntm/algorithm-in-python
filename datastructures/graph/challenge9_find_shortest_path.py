"""
Problem Statement:
- Implement the find_min() function which will take a directed graph and
    two vertices, A and B. The result will be the shortest path from A to B.
    Remember, the shortest path will contain the minimum number of edges.

Input:
- A directed graph, a vertex A and a vertex B.
Output:
- Returns number of edges in the shortest path between A and B.

Sample Input:
    graph = {
        0 -> 1
        0 -> 2
        0 -> 3
        3 -> 5
        5 -> 4
        2 -> 4
    }
    
    Vertex A = 0 
    Vertex B = 4
 
Sample Output:
- 2
"""


from collections import deque
from Graph import Graph


def find_min(g, source, destination):
    distance = [0] * g.vertices
    visited = [False] * g.vertices
    q = deque()
    q.append(source)

    while q:
        v = q.popleft()
        adjacency = g.array[v].get_head()
        visited[v] = True
        while adjacency:
            if not visited[adjacency.data]:
                distance[adjacency.data] = distance[v] + 1
                if adjacency.data == destination:
                    return distance[destination]
                q.append(adjacency.data)
            adjacency = adjacency.next_element
    return -1


if __name__ == '__main__':
    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    print(find_min(g, 1, 5))
