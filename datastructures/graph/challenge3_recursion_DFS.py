from Graph import Graph


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
