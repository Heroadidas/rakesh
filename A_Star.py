import heapq
def h(n):
        if (n == -1):
            return 0
        H_dist = {
            'S': 7,
            'A': 6,
            'B': 2,
            'C': 1,
            'D': 0,            
        }
        return H_dist[n]
        
def aStarAlgo(start: str, goal: str, graph: dict[str, list[tuple[str, int]]]):
    if graph is None:
        return "Graph is empty"
    if start not in graph.keys():
        return "Start node is not in the graph"
    
    visited = {i: False for i in graph.keys()}
    queue = []
    heapq.heappush(queue, (0 + h(start), start, -1))  # Initial cost, start node, parent node
    cost = 0
    path = []
    
    while queue:
        wt, nd, parent = heapq.heappop(queue)
        
        if visited[nd]:
            continue
        
        visited[nd] = True
        path.append(nd)
        cost += wt 
        
        if nd == goal:
            print("Path:", path)
            print("Total cost:", cost)
            return
        
        for neighbor, edge_cost in graph[nd]:
            if not visited[neighbor]:
                heapq.heappush(queue, (edge_cost + h(neighbor), neighbor, nd))

tree = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 3)],
    'D': [],
}
aStarAlgo('S', 'D', tree)

heuristics = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 0,
}