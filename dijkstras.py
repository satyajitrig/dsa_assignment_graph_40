# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 14:09:24 2023

@author: satya
"""

intmax=9999999999 #assuming inf class Graph():

def  init (self, vertices): self.V = vertices
self.graph = [[0 for column in range(vertices)] for row in range(vertices)]





def printSolution(self, dist):
    print ("Vertex \tDistance from Source") for node in range(self.V):
        print (node, "\t\t ", dist[node], "\n")



def minDistance(self, dist, sptSet):



min = intmax



for u in range(self.V):
if dist[u] < min and sptSet[u] == False: 


min = dist[u] min_index = u

return min_index



def dijkstra(self, src):


dist = [intmax] * self.V dist[src] = 0
count = [False] * self.V


for i in range(self.V):



x = self.minDistance(dist, count)



count[x] = True



for y in range(self.V):
if self.graph[x][y] > 0 and count[y] == False and \ dist[y] > dist[x] + self.graph[x][y]:
dist[y] = dist[x] + self.graph[x][y]


self.printSolution(dist)
 
# Driver program g = Graph(6)
g.graph = [[0, 5, 2, 0, 4, 0],
[5, 0, 5, 0, 0, 0],
[2, 5, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 2],
[4, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 0, 0]]


g.dijkstra(5)


# for second test case """g.graph = [[0, 5, 2, 0, 4, 0],
[5, 0, 5, 0, 0, 0],
[2, 5, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 2],
[4, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 0, 0]]"""