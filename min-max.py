tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
}

terminal_nodes = {
    'H': -1,
    'I': 4,
    'J': 2,
    'K': 6,
    'L': -3,
    'M': -5,
    'N': 0,
    'O': 7,
}


def minimax(tree, terminal_nodes, node, isMax=True):
    if node in terminal_nodes.keys():
        return terminal_nodes[node], [node]

    if isMax:
        val = float('-inf')
    else:
        val = float('inf')

    path = [] 

    for i in tree[node]:
        temp_val, temp_path = minimax(tree, terminal_nodes, i, not isMax)
        if isMax:
            val = max(val, temp_val)
        else:
            val = min(val, temp_val)
        if val == temp_val:
            path = temp_path

    path.insert(0, node)
    return val, path

val, path = minimax(tree, terminal_nodes, 'A')
print(val)
print(path)
