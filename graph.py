def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)   # undirected

graph = {}
add_edge(graph, 0, 1)
add_edge(graph, 1, 2)
add_edge(graph, 0, 3)
def print_neighbors(graph, node):
    if node in graph:
        print(f"Neighbors of {node}:", graph[node])
    else:
        print(f"Node {node} not found")

print_neighbors(graph, 1)  # Neighbors of 1: [0, 2]

