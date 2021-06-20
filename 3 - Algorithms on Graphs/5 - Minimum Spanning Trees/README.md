## Algorithms on Graphs Week 5
### Minimum Spanning Trees

* [Building roads]()
* [Clustering]()

---

### Lecture Notes
#### Minimum Spanning Tree (MST)
* **Input**: a connected, undirected graph G = (V, E) with positive edge
weights.
* **Output**: a subset of edges e' subset of E of minimum total weight 
s.t. the graph (V, e') is connected.
  
#### Kruskal's algorithm
* Every vertex starts in a separate set.
* Each set is the set of vertices of a connected component.
* Iteratively add the next lightest edge e that doesn't produce a cycle (i.e., aren't in the same set).

```
def kruskal(G):
	for all u in vertices:
		makeset(v)

	X = set()
	# sort edges e by weight
	for all u,v in e:
		if find(u) != find(v):
			add u,v to X
			union(u, v)

	return X
```

Sorting edges is `O(len(edges) * log(len(edges))) = O(len(edges) * log(len(vertices)))` and
processing edges is also `O(len(edges) * log(len(vertices)))`, so the total running time is `O(len(edges) * log(len(vertices)))`.

#### Prim's algorithm
* Use a priority queue data structure.
* Pick a random vertex as root of tree, change priority to 0.
* Process every edge going out from this root, pick one with smallest cost.

```
def prim(G):
	for all u in vertices:
		cost[u] = inf
		parent[u] = nil

	# pick any initial vertex u_0
	cost[u_0] = 0
	q = makeQueue(V)

	while q:
		v = extract_min(q)
		for all v,z in edges:
			if z in q and cost[z] > w(v, z):  # z not in tree and cheaper to attach to tree
				cost[z] = w(v, z)
				parent[z] = v
				change_priority(q, z, cost[z])
```

The running time depends on implementation. Array-based implementations will be `O(len(vertices)**2)` and binary heap-based implementations
will be `O(len(edges) * log(len(vertices)))`.

> Note: you can also start with a queue containing only the start node and adding nodes on the fly. You may need to check that the node hasn't already
been processed, but this saves you from "changing the priority of the node" which doesn't seem to be possible with
the `queue` and `heapq` modules.
