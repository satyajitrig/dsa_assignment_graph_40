# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 14:56:24 2023

@author: satya
"""


def bfs(graph, start):
    visited = [False] * len(graph)
    queue = []
    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for neigh in graph[v]:
            if not visited[neigh]:
                visited[neigh] = True
                queue.append(neigh)

# Example usage:

graph = {
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
}

bfs(graph, 'A')

graph1 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'E': ['B'],
    'F': ['C'],
    'G': ['D'],
}

bfs(graph1, 'A')

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'D': ['B'],
    'E': ['C'],
}

bfs(graph2, 'A')
