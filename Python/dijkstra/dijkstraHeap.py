# Implementacao do algortimo de Dijkstra em conjunto de um Heap (priority Queue)
# Utilizamos o Heap para sempre adicionar automaticamente a Fila (queue) o menor Caminho
# Facilitando a comparacao ao inserir o menor sempre no inicio


import heapq

def dijkstra(graph, start):
    min_heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))
                0

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
}

shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)