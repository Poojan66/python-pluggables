import heapq

class Dijkstra:
    """
    A class that implements Dijkstra's algorithm to find the shortest paths in a weighted, directed graph.

    Methods:
        find_shortest_paths(graph, start): Finds the shortest paths from the start vertex to all other vertices in the graph.
    """

    @staticmethod
    def find_shortest_paths(graph, start):
        """
        Finds the shortest paths from the start vertex to all other vertices in the graph using Dijkstra's algorithm.

        Args:
            graph (dict): A dictionary representing the graph, where each key is a vertex and the corresponding value is
                          a list of tuples, where each tuple represents an adjacent vertex and the weight of the edge.
            start (str): The starting vertex.

        Returns:
            A dictionary representing the shortest paths from the start vertex to all other vertices in the graph.
        """
        distances = {vertex: float('inf') for vertex in graph}
        distances[start] = 0

        heap = [(0, start)]
        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances
graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('A', 2), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}
dijkstra = Dijkstra()
shortest_paths = dijkstra.find_shortest_paths(graph, 'A')
print(shortest_paths)
