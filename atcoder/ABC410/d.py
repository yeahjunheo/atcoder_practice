from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = defaultdict(list)
for a, b, w in edges:
    graph[a].append((b, w))

def dijkstra(start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d ^ w:
                dist[v] = d ^ w
                heappush(pq, (dist[v], v))
    
    return dist
distances = dijkstra(1, n)
if distances[n] == float('inf'):
    print(-1)
else:
    print(distances[n])