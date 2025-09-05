import heapq
import math
import copy
from copy import deepcopy
import numpy as np

#########################################################
############## QUESTION 1 HERE ##################
#########################################################
def myFloyd(M):
    n = len(M)
    dist = [row[:] for row in M]
    out = []
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        out.append([row[:] for row in dist])
    return out
    
#########################################################
############## QUESTION 2 HERE ##################
#########################################################
def dijkstra_matrix(vertices, edges):
    n = len(vertices)
    INF = math.inf
    A = [[INF] * n for _ in range(n)]
    for u, v, w in edges:
        A[u][v] = w
    dist = [INF] * n
    prev = [None] * n
    dist[0] = 0
    visited = [False] * n
    for _ in range(n):
        u = None
        best = INF
        for i in range(n):
            if not visited[i] and dist[i] < best:
                best = dist[i]
                u = i
        if u is None:
            break
        visited[u] = True
        for v in range(n):
            w = A[u][v]
            if w != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
    paths = {}
    for v in range(n):
        if dist[v] == INF:
            paths[v] = []
        else:
            path = []
            cur = v
            while cur is not None:
                path.append(cur)
                cur = prev[cur]
            paths[v] = path[::-1]
    return paths, dist