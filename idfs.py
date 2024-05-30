graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F' : [],
    'G': ['J'],
    'H' : [],
    'I' : [],
    'J' : []
}


def idfs(start , goal , graph , max_depth) :


    for idx in range(max_depth + 1):
        visited = {node : False for node in graph}
        print(f"{idx} iteration : " , end = ' ')
        dls(start, visited , graph , idx)
        print()

        if visited[goal]:
            break

def dls (start, visited ,  graph , depth ):
    visited[start] = True
    print(start , end = " ")


    if depth == 0:
        return

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dls(neighbor , visited , graph , depth - 1)



idfs('A' , 'J' , graph , 5)