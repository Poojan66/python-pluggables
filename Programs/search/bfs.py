from collections import deque

class Graph:
    """
    A class that represents a directed graph using adjacency lists.

    Attributes:
        vertices (int): The number of vertices in the graph.
        adj_list (dict): A dictionary containing adjacency lists for each vertex.

    Methods:
        add_edge(u, v): Adds a directed edge from vertex u to vertex v.
        bfs(v): Performs BFS traversal starting from vertex v.
    """

    def __init__(self, vertices):
        """
        Initializes a new graph with the given number of vertices.

        Args:
            vertices (int): The number of vertices in the graph.
        """
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(self.vertices)}

    def add_edge(self, u, v):
        """
        Adds a directed edge from vertex u to vertex v.

        Args:
            u (int): The source vertex of the edge.
            v (int): The destination vertex of the edge.
        """
        self.adj_list[u].append(v)

    def bfs(self, v):
        """
        Performs BFS traversal starting from vertex v.

        Args:
            v (int): The starting vertex for BFS traversal.

        Returns:
            A list of vertices visited in BFS order.
        """
        visited = set()
        queue = deque([v])
        bfs_order = []
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return bfs_order
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
bfs_order = g.bfs(2)
print(bfs_order)
