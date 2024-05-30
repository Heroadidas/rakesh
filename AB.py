def alphabeta(node, depth, alpha, beta, maximizing_player, terminal_nodes, tree, path=[]):
    path = path + [node]

    if node in terminal_nodes:
        return terminal_nodes[node], path

    if maximizing_player:
        max_value = float('-inf')
        max_path = []
        for child in tree.get(node, []):
            value, child_path = alphabeta(child, depth - 1, alpha, beta, False, terminal_nodes, tree, path)
            if value > max_value:
                max_value = value
                max_path = child_path
            alpha = max(alpha, value)
            print(f"Alpha: {alpha}, Beta: {beta}")
            if beta <= alpha:
                break
        return max_value, max_path
    else:
        min_value = float('inf')
        min_path = []
        for child in tree.get(node, []):
            value, child_path = alphabeta(child, depth - 1, alpha, beta, True, terminal_nodes, tree, path)
            if value < min_value:
                min_value = value
                min_path = child_path
            beta = min(beta, value)
            print(f"Alpha: {alpha}, Beta: {beta}")
            if beta <= alpha:
                break
        return min_value, min_path

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

value, path = alphabeta('A', 4, float('-inf'), float('inf'), True, terminal_nodes, tree)
print(f"Value: {value}")
print(f"Path: {' -> '.join(path)}")