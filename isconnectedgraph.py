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
def is_connected(graph,u,v):
    if u not in graph:
        return False
    return v in graph[u]
print(is_connected(graph,0,1))

def add_edge(graph,u,v):
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
    graph[u].append(v)
graph={}
add_edge(graph,0,1)