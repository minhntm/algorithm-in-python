from collections import deque
from Graph import Graph


def bfs_traversal(g, source):
    num_of_vertices = g.vertices
    visited = [False] * num_of_vertices
    q = deque()
    q.append(source)
    result = ""

    while q:
        v = q.popleft()
        node = g.array[v].get_head()
        if not visited[v]:
            result += str(v)
            visited[v] = True
        while node:
            if not visited[node.data]:
                q.append(node.data)

            node = node.next_element

    return result


if __name__ == '__main__':
    g = Graph(4)
    num_of_vertices = g.vertices

    if num_of_vertices == 0:
        print("Graph is empty")
    elif(num_of_vertices < 0):
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)

        print(bfs_traversal(g, 0))
