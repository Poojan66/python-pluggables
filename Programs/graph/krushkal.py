class Kruskal:
    """
    A class that implements Kruskal's algorithm to find the minimum spanning tree of a weighted, undirected graph.

    Methods:
        find_min_spanning_tree(graph): Finds the minimum spanning tree of the given graph.
    """

    class DisjointSet:
        """
        A helper class for implementing disjoint sets.

        Methods:
            __init__(self, n): Initializes the disjoint set.
            find(self, x): Finds the root of the set containing x.
            union(self, x, y): Merges the sets containing x and y.
        """

        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.rank = [0 for _ in range(n)]

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            xroot = self.find(x)
            yroot = self.find(y)
            if xroot == yroot:
                return
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            elif self.rank[xroot] > self.rank[yroot]:
                self.parent[yroot] = xroot
            else:
                self.parent[yroot] = xroot
                self.rank[xroot] += 1

    @staticmethod
    def find_min_spanning_tree(graph):
        """
        Finds the minimum spanning tree of the given graph using Kruskal's algorithm.

        Args:
            graph (dict): A dictionary representing the graph, where each key is a vertex and the corresponding value is
                          a list of tuples, where each tuple represents an adjacent vertex and the weight of the edge.

        Returns:
            A list of tuples representing the edges of the minimum spanning tree and their weights.
        """
        edges = []
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                edges.append((weight, vertex, neighbor))
        edges.sort()

        mst = []
        disjoint_set = Kruskal.DisjointSet(len(graph))

        for weight, u, v in edges:
            if disjoint_set.find(u) != disjoint_set.find(v):
                disjoint_set.union(u, v)
                mst.append((u, v, weight))

        return mst
graph = {
    'A': [('B', 2), ('D', 4)],
    'B': [('A', 2), ('C', 3), ('D', 1)],
    'C': [('B', 3), ('D', 5)],
    'D': [('A', 4), ('B', 1), ('C', 5)]
}
kruskal = Kruskal()
mst = kruskal.find_min_spanning_tree(graph)
print(mst)
