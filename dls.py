def dls(start, visited, graph, depth):
    visited[start] = True
    print(start, end=" ")

    if depth == 0:
        return

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dls(neighbor, visited, graph, depth - 1)

graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['G'], 'F': [], 'G': []}
start_node = 'A'
max_depth = 1

visited = {node: False for node in graph}
dls(start_node, visited, graph, max_depth)