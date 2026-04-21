def dfs_print(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    visited.add(start_node)
    print(start_node, end=" ")

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            dfs_print(graph, neighbor, visited)

print("DFS from 0:")
dfs_print(graph, 0)   # possible output: 0 1 2 3