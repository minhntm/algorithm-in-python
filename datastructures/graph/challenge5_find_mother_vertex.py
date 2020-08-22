"""
Problem Statement:
- You have to implement the find_mother_vertex() function which will take
    a directed graph as an input and find out which vertex is the mother vertex
    in the graph.
    By definition, the mother vertex is one from which all other vertices
    are reachable. A graph can have multiple mother vertices,
    but you only need to find one.

Input:
- A directed graph
Output:
- Returns the value of the mother vertex if it exists. Otherwise, it returns -1

Sample Input:
    graph = {
            3 -> 0 
        3 -> 1
        0 -> 1
        1 -> 2
    }
Sample Output:
- 3
"""


from Graph import Graph


def find_mother_vertex(g):
    visited = [False] * g.vertices
    mother_vertex = 0
    for i in range(g.vertices):
        if not visited[i]:
            DFS(g, i, visited)
            mother_vertex = i

    visited = [False] * g.vertices
    DFS(g, mother_vertex, visited)
    return mother_vertex if all(visited) else -1


def DFS(g, v, visited):
    if not visited[v]:
        visited[v] = True
    adjacent = g.array[v].get_head()
    while adjacent:
        if not visited[adjacent.data]:
            DFS(g, adjacent.data, visited)
        adjacent = adjacent.next_element


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    print(find_mother_vertex(g))
