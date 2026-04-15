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

def count_edges(graph):
    total_degrees = 0
    for neighbors in graph.values():
        total_degrees += len(neighbors)
    return total_degrees // 2   # each edge counted twice

print("Edge count:", count_edges(graph))  # 3