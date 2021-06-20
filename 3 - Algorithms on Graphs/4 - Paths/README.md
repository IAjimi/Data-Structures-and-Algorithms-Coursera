## Algorithms on Graphs Week 4
### Paths 2 (Weighted Graphs)

* [Computing the Minimum Cost of a Flight]() (Finding shortest path in weighted graph)
* [Detecting Anomalies in Currency Exchange Rates]() (Detecting negative weight cycles)

---

### Lecture Notes
#### Fastest Route
Observation: any subpath of an optimal path must be optimal.

Edge relaxation: we don't start out with optimal distances stored
in `dist[v]` so `dist[v]` will be an *upper bound* on the actual distance
from S to v.

The edge relaxation procedure for an edge (u,v) just checks whether going
from S to v through u improves the current value of `dist[v]`.

```
def Relax(u, v):
	if dist[v] > dist[u] + w(u, v):
		dist[v] = dist[u] + w(u, v)
		prev[v] = u

def Naive(G, S):
	for all u in vertex:
		dist[u] = inf
		prev[u] = nil

	dist[S] = 0
	do:
		relax all edges
	while at least one dist change

def dijkstra(graph, start):
	for all u in vertices:
		dist[u] = inf
		prev[u] = nil

	dist[start] = 0
	H = make_queue(v) # dist values as keys

	while H is not empty:
		u = extract_min(H)

		for all u,v in edges:
			if dist[v] > dist[u] + w(u, v):
				dist[v] = dist[u] + w(u, v)
				prev[v] = u
				change_priority(H, v, dist[v])
```
Running time:
* array: `O(len(v) + len(v)**2 + len(edges)) = O(len(vertices)**2)`
* binary heap: `O((len(v) + len(edges)) * log(vertices))`

#### Paths in Graphs
* **Input**: currency exchange graph with weighted edges ei
* **Output**: maximize `r_ei*r_ej` from USD to RUR in the path

We cn take the logs of the numbers to turn the product into a sum. Then
we make all numbers negative - maximizing the sum of logarithms is the same as minimizing
the substraction of logarithms.

Dijkstra's algorithm struggles with negative numbers.

The issue comes from **negative weight cycles**: cycles with negative total
weight which tends to -inf.

The algorithm below (the naive algorithm from earlier) actually **does** work for negative edge weights:

```
def BellmanFord(G, S):
	# no negative weight cycles in G
	for all u in vertices:
		dist[u] = inf
		prev[u] = nil

	dist[S] = 0

	for _ in range(len(vertices) - 1):
		for all (u,v) in edges:
			relax(u, v)
```

The running time of Bellman-Ford is `O(len(v) * len(edges))`.

**Lemma**: a graph G contains a negative weight cycle if and only if
the len(v)-ith iteration of BellmanFord updates some dist value.

**Lemma**: it is possible to get any amount of currency u from currency S
if and only if u is reachable from some node w for which `dist[w]` 
decreases on iteration V of Bellman-Ford.

Detect infinite arbitrage:
* do length(v) iterations of Bellman-Ford, save all nodes relaxed
on v-th iteration - we'll call this set A
* put all nodes from A in queue Q
* do BFS with queue Q to find all nodes reachable from A
* all these nodes have infinite arbitrage

Reconstruct Infinite Arbitrage:
* during BFS, remember the parent of each visited node
* reconstruct the path to u from some node w relaxed on iteration v
* go back from w to find negative cycle from which w is reachable
* use this negative cycle to achieve infinite arbitrage from S to u

