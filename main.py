import itertools
import numpy as np

def matrix(a, b, match_score=3, gap_cost=2):
    H = np.zeros((len(a) + 1, len(b) + 1), np.int)

    for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
        match = H[i - 1, j - 1] + (match_score if a[i - 1] == b[j - 1] else - match_score)
        delete = H[i - 1, j] - gap_cost
        insert = H[i, j - 1] - gap_cost
        H[i, j] = max(match, delete, insert, 0)
    return H

def traceback(H, b, b_='', old_i=0):
    # flip H to get index of *last* occurrence of H.max() with np.argmax()
    H_flip = np.flip(np.flip(H, 0), 1)
    i_, j_ = np.unravel_index(H_flip.argmax(), H_flip.shape)
    i, j = np.subtract(H.shape, (i_ + 1, j_ + 1))  # (i, j) are *last* indexes of H.max()
    if H[i, j] == 0:
        return b_, j
    b_ = b[j - 1] + '-' + b_ if old_i - i > 1 else b[j - 1] + b_
    return traceback(H[0:i, 0:j], b, b_, i)

def smith_waterman(s1, s2, match_score=3, gap_cost=2):
    s1, s2 = s1.upper(), s2.upper()
    H = matrix(a, b, match_score, gap_cost)
    b_, pos = traceback(H, b)
    return pos, pos + len(b_)

 # prints correct scoring matrix from Wikipedia example
print(matrix('GGTTGACTA', 'TGTTACGG'))
print("\n")
a, b = 'ggttggaccttaccaa', 'ttggttaaccggcaca'
H = matrix(a, b)
print(traceback(H, b)) # ('gtt-ac', 1)
print("\n")
a, b = 'GGTTGGACCTTACCAA', 'TTGGTTAACCGGCACA'
start, end = smith_waterman(a, b)
print(a[start:end])   

#Prims 
Prims(a,start):
    n = number of vertices in a
    mst = empty set of size n
    key = array of size n with all values set to infinity
    prev = array of size n with all values set to null
    key[start] = 0
    heap = new priority queue with all vertices and key values
    while heap is not empty:
        u = heap.extractMin()
        mst.add(u)
        for each vertex v in a.adjacentVertices(u):
            if v is not in mst and key[v] > a.weight(u,v):
                key[v] = a.weight(u,v)
                prev[v] = u
                heap.decreaseKey(v, key[v])
    return mst, prev

traceback(prev, start, end):
    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    return path[::-1]# GTTGAC
#Kruskals
Kruskal(G):
    n = number of vertices in G
    mst = empty set of edges
    edges = list of edges in G sorted by ascending weight
    ds = new disjoint set data structure with n elements
    for each edge (u, v, w) in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.add((u, v, w))
    return mst

traceback(mst, start, end):
    path = []
    ds = new disjoint set data structure with n elements
    for each edge (u, v, w) in mst:
        ds.makeSet(u)
        ds.makeSet(v)
        ds.union(u, v)
    current = start
    while current != end:
        for each edge (u, v, w) in mst:
            if ds.find(u) == current and ds.find(v) == current:
                path.append((u, v))
                current = v
                break
    return path
#Djikshtra
Dijkstra(G, start):
    n = number of vertices in G
    dist = array of size n with all values set to infinity
    prev = array of size n with all values set to null
    dist[start] = 0
    heap = new priority queue with all vertices and key values
    while heap is not empty:
        u = heap.extractMin()
        for each vertex v in G.adjacentVertices(u):
            if dist[v] > dist[u] + G.weight(u, v):
                dist[v] = dist[u] + G.weight(u, v)
                prev[v] = u
                heap.decreaseKey(v, dist[v])
    return dist, prev

traceback(prev, start, end):
    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    return path[::-1]
        