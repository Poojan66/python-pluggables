class Graph:
    """
    A class that represents a directed graph using adjacency lists.

    Attributes:
        vertices (int): The number of vertices in the graph.
        adj_list (dict): A dictionary containing adjacency lists for each vertex.

    Methods:
        add_edge(u, v): Adds a directed edge from vertex u to vertex v.
        dfs_util(v, visited): A utility function for DFS traversal starting from vertex v.
        dfs(v): Performs DFS traversal starting from vertex v.
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

    def dfs_util(self, v, visited):
        """
        A utility function for DFS traversal starting from vertex v.

        Args:
            v (int): The starting vertex for DFS traversal.
            visited (set): A set of visited vertices.

        Returns:
            A list of vertices visited in DFS order.
        """
        visited.add(v)
        dfs_order = [v]
        for neighbor in self.adj_list[v]:
            if neighbor not in visited:
                dfs_order += self.dfs_util(neighbor, visited)
        return dfs_order

    def dfs(self, v):
        """
        Performs DFS traversal starting from vertex v.

        Args:
            v (int): The starting vertex for DFS traversal.

        Returns:
            A list of vertices visited in DFS order.
        """
        visited = set()
        return self.dfs_util(v, visited)


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
dfs_order = g.dfs(2)
print(dfs_order)
