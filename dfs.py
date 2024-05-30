def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

graph = {
    0: [1, 2],
    1: [3, 5],
    2: [4, 6],
    3: [],
    4: [],
    5: [],
    6: [],
}
visited = set()
dfs(graph, 0, visited)  