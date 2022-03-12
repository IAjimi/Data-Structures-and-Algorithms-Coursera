## Algorithms on Graphs Week 3
### Paths 1

* [Computing the Minimum Number of Flight Segments](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/3%20-%20Algorithms%20on%20Graphs/3%20-%20Paths/minimum_distance.py) (Shortest Path)
* [Bipartite graphs](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/3%20-%20Algorithms%20on%20Graphs/3%20-%20Paths/bipartite_graph.py) (didn't pass Coursera but passed Leetcode)

---

### Paths
### Breadth-First Search
Visit nodes from closest to furthest away from a given point. The queue
structure is used to keep layers in order.

```
def bfs(G, S):
	for all u in V:
		dist[u] = inf, prev[u] = None
	dist[S] = 0
	Q = {S} # queue with just S
	while Q is not empty:
		u = dequeue(Q)
		for all u,v in edges:
			if dist[v] == inf:
				enqueue(Q, v)
				dist[v] = dist[u] + 1
				prev[v] = u

```


The running time of breadth-first search is `O(len(edges) + len(vertices))`.
* Each vertex is enqueued at most once
* Each edge is examined either once (for directed graphs) or twice (for undirected graphs)

### Reconstructing Shortest Path
```
def reconstructPath(S, u, prev):
	result = empty

	while u != S:
		result.append(u)
		u = prev[u]

	return reversed(result)
```

The runtime of the above is `O(len(edges) + len(vertices))`.