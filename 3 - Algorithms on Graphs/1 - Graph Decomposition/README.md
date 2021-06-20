## Algorithms on Graphs Week 1
### Graph Decomposition 1

* [Find an exit from a maze]() (Is node reachable?)
* [Find the number of exists needed for a maze]() (Find the number of graph components)

---

### Lecture Notes
#### Formal Definition
An (undirected) graph is a collection V of vertices and a collection E of edges
each of which connects a pair of vertices.

Loops connect a vertex to itself.
There can be multiple edges between the same vertices.

If a graph has neither, it is called a **simple graph**.

#### Representing Graphs
* list of edges: `edges = [(a,b), (a,c), (a,d), (c,d)]`
* matrix, with entries 1 if there is an edge, 0 if not: `adj_matrix = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0]]`
* adjacency list: for each vertex, keep a list of adjacent 
vertices: `adj_list = [[b,c,d], [a], [a,d], [a,c]]`

Which is best?
Different operations are faster in different representations.

* Is edge:
	* adj_matrix: `O(1)`, direct lookup
	* edge_list: `O(len(edges))`, need to scan whole list to find entry
	* adj_list: `O(deg)`, proportion to degree (number of neighbors) of vertex
* List edges:
	* adj_matrix: `O(len(vertex)**2)`, scan through every entry of the matrix
	* edge_list: `O(len(edges))`
	* adj_list: `O(len(edges))`
* List neighbors:
	* adj_matrix: O(len(vertex)), scan through row of matrix and find all 1s
	* edge_list: O(len(edges))
	* adj_list: O(deg),

For many problems, we want to use the **adjacency list**.

#### Algorithm Runtimes
Graph algorithm runtimes depend on len(vertex) and len(edges).

What is faster, O(len(vertex)**3/2) or O(len(edges))?
It depends on the graph's density!

In **dense** graphs (`len(edges) += len(vertex)**2`), a large fraction of pairs are connected
by edges.


In **sparse** graphs (`len(edges) += len(vertex)`), each vertex has only a few edges.

#### Exploring Graphs
We want to know what nodes are reachable from a given vertex.

A **path** in a graph G is a sequence of vertices s.t. for all i,
`v_i, v_i+1` is an edge of G.

* **Input**: graph G, vertex s
* **Output**: collection of vertices v of G s.t. there is a path to s

```
def component(s):
	discovered_nodes = set(s)

	# while there is an edge e leaving discovered_nodes not in discovered_nodes:
		# add vertex at the other end of e to discovered_nodes

	return discovered_nodes
```

To keep track of vertices found, give each vertex boolean visited(v). The list 
of vertices with edges left to check is hidden in program stack.

We will explore new edges in a **depth first** order: we will follow a long path
forward, only backtracking when we hit a dead end.

```
def explore(v):
	visited[v] = True
	cc_num[v] = cc

	for v,w in edges:
		if not visited(w):
			explore(w)
```

The vertices of a graph G can be partitioned into connected 
components so that v is reachable from w if and only if
they are in the same connected component.

`cc_num` doesn't change during the recursive calls to explore, so everything found during this will have same cc.

```
def explore(v):
	visited(v) = True
	previsit(v)

	for v,w in edges:
		if not visited(w):
			explore(w)

	postvisit(v)
```

previsit() and postvisit() can be used alongside a "clock" to keep track of when a node was 1st and last visited.

```
initialize clock = 1

def previsit(v):
	prev(v) = clock
	clock += 1

def postvisit(v):
	post(v) = clock
	clock += 1
```
