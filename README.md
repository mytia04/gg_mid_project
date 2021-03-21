# gg_mid_project

Medet Myrzash- Coder
Aruzhan Zhanatkyzy - Quality Assurance 
Tomiris Yerkinbek - Coder
Kami Burkitbay - Coder
#Explanation of Undirected Graphs 

An undirected graph is graph, i.e., a set of objects (called vertices or nodes) that are connected together, where all the edges are bidirectional. An undirected graph is sometimes called an undirected network. 
In contrast, a graph where the edges point in a direction is called a directed graph.

#When we use Undirected Graphs

Undirected graphs apply well to relationships for which it matters whether they exist or not, but aren’t intrinsically transitive. 
If, for example, we can go both ways in pedestrian paths, then we can model the pathways as an undirected graph
Undirected graphs are more restrictive kinds of graphs. They represent only whether or not a relationship exists between two vertices. 
They don’t however represent a distinction between subject and object in that relationship.
One type of graph can sometimes be used to approximate the other. When we do, though, there’s often a cost to pay in terms of information content.

#Explanation of python code.

Graphs as a Python Class
Before we go on with writing functions for graphs, we have a first go at a Python graph class implementation. 
If you look at the following listing of our class, you can see in the __init__-method that we use a dictionary "self.__graph_dict" for storing the vertices and their corresponding adjacent vertices.
We want to find now the shortest path from one node to another node. Before we come to the Python code for this problem, we will have to present some formal definitions.
Adjacent vertices:
Two vertices are adjacent when they are both incident to a common edge.
Path in an undirected Graph:
A path in an undirected graph is a sequence of vertices P = ( v1, v2, ..., vn ) ∈ V x V x ... x V such that vi is adjacent to v{i+1} for 1 ≤ i < n. Such a path P is called a path of length n from v1 to vn.
Simple Path:
A path with no repeated vertices is called a simple path.
Example:
(a, c, e) is a simple path in our graph, as well as (a,c,e,b). (a,c,e,b,c,d) is a path but not a simple path, because the node c appears twice.



