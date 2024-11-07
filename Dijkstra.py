import heapq
from collections import defaultdict

#Dijkstra: Shortest Reach 2.

#a kommenteket a futtatás előtt kiszedni (HACKERRANK oldalon)
def shortestReach(n, edges, s):
    graph = defaultdict(list)
    for x, y, r in edges:
        graph[x].append((y, r))
        graph[y].append((x, r)) #mivel nem  irányított gráf
    
    distances = {}
    for i in range(1, n+1):
        distances[i] = float('inf')
    distances[s] = 0

    pQueue = [(0, s)] # távolság, node

    while pQueue:
        c_distance, c_node = heapq.heappop(pQueue)
        if c_distance > distances[c_node]:
            continue

        for neighbor, weight in graph[c_node]:
            distance = c_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pQueue, (distance, neighbor))
    
    result = []
    for node in range(1, n+1):
        if node == s:
            continue
        if distances[node] == float('inf'):
            result.append(-1)
        else:
            result.append(distances[node])
    
    return result