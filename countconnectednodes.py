def count_connected_nodes(graph, start):
    visited = set()
    count = 0

    def dfs(node):
        nonlocal count
        visited.add(node)
        count += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return count
graph = {0: [1, 3], 1: [0, 2], 2: [1], 3: [0]}
print("Number of connected nodes from 0:", count_connected_nodes(graph, 0))  # possible output: 4