from collections import deque
from Graph import Graph


def dfs_traversal(g, source):
    result = ''
    visited = [False] * g.vertices
    stack = deque()
    stack.append(source)
    while stack:
        v = stack.pop()
        if not visited[v]:
            result += str(v)
            visited[v] = True
        adjacent = g.array[v].get_head()
        while adjacent:
            stack.append(adjacent.data)
            adjacent = adjacent.next_element

    for i, is_visited in enumerate(visited):
        if not is_visited:
            result += str(i)

    return result


if __name__ == '__main__':
    g = Graph(7)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("graph is empty")
    elif(num_of_vertices < 0):
        print("graph cannot have negative vertices")
    else:
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        print(dfs_traversal(g, 1))
