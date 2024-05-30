def alphabeta(node , depth , alpha , beta , isMax , terminal_nodes , tree ):
    if depth == 0 or node in terminal_nodes:
        return terminal_nodes[node]
    
    if isMax:
        max_value = float('-inf')
        
        for child in tree[node]:
            value = alphabeta(child , depth - 1 , alpha , beta , False , terminal_nodes , tree)
            max_value = max(max_value , value)
            alpha = max(alpha , value)
            if beta <= alpha:
                break
        return max_value
    
    else:
        min_value = float('inf')
        
        for child in tree[node]:
            value = alphabeta(child , depth - 1 , alpha , beta , True , terminal_nodes , tree)
            min_value = min(min_value , value)
            beta = min(beta , value)
            if beta <= alpha:
                break
        return min_value

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

sol  = alphabeta('A' , 4 , float('-inf') , float('inf') , True , terminal_nodes , tree)
print(sol)