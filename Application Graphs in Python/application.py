"""We want to find now the shortest path from one node to another node. Before we come to the Python code for this problem, we will have to present some formal definitions.

Adjacent vertices:
Two vertices are adjacent when they are both incident to a common edge.

Path in an undirected Graph:
A path in an undirected graph is a sequence of vertices P = ( v1, v2, ..., vn ) ∈ V x V x ... x V such that vi is adjacent to v{i+1} for 1 ≤ i < n. Such a path P is called a path of length n from v1 to vn.
Simple Path:
A path with no repeated vertices is called a simple path."""
        
""" find a path from start_vertex to end_vertex 
            in graph """

        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None

"""If we save our graph class including the find_path method as "graphs.py", we can check the way of working of our find_path function:
from graphs import Graph
"""
g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())


print('The path from vertex "a" to vertex "b":')
path = graph.find_path("a", "b")
print(path)

print('The path from vertex "a" to vertex "f":')
path = graph.find_path("a", "f")
print(path)

print('The path from vertex "c" to vertex "c":')
path = graph.find_path("c", "c")
print(path)
"""
The method find_all_paths finds all the paths between a start vertex to an end vertex:
    def find_all_paths(self, start_vertex, end_vertex, path=[]):"""
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths
"""We slightly changed our example graph by adding edges from "a" to "f" and from "f" to "d" to test the previously defined method:"""

from graphs import Graph

g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())


print('All paths from vertex "a" to vertex "b":')
path = graph.find_all_paths("a", "b")
print(path)

print('All paths from vertex "a" to vertex "f":')
path = graph.find_all_paths("a", "f")
print(path)

print('All paths from vertex "c" to vertex "c":')
path = graph.find_all_paths("c", "c")
print(path)

