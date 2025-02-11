import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = []
        if to_vertex not in self.vertices:
            self.vertices[to_vertex] = []
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))

def dijkstra(graph, start_vertex):
    shortest_paths = {vertex: float('inf') for vertex in graph.vertices}
    shortest_paths[start_vertex] = 0
    priority_queue = [(0, start_vertex)] # (distance, vertex)
    heapq.heapify(priority_queue)
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight

            # Update if the new way if shorter
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 1)
    g.add_edge("D", "E", 3)

    start_vertex = "A"
    shortest_paths = dijkstra(g, start_vertex)

    print(f"Fastes way from '{start_vertex}':")
    for vertex, distance in shortest_paths.items():
        print(f"To '{vertex}': {distance}")
