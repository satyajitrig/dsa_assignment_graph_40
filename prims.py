def kruskal(graph):
    edges = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors.items()]
    edges.sort()

    parent = {node: node for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u, root_v = find(u), find(v)
        parent[root_u] = root_v

    mst = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((weight, u, v))

    return mst

# Sample Case:
graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 4},
    'D': {'A': 1, 'B': 2, 'C': 4}
}

result = kruskal(graph)
print("Minimum Spanning Tree (Kruskal's Algorithm):", result)

# Test case 1:
graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 4},
    'D': {'A': 1, 'B': 2, 'C': 4}
}

# Test case 2:
graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 4, 'D': 2},
    'C': {'A': 1, 'B': 4, 'D': 5},
    'D': {'B': 2, 'C': 5}
}
