## Algorithms on Graphs Week 6
### Advanced Shortest Path

* [Friend Suggestion](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/3%20-%20Algorithms%20on%20Graphs/6%20-%20Advanced%20Shortest%20Path/friend_suggestion.py) (Bidirectional Dijkstra)
* [Distance with Coordinates]() (A* Dijkstra)
* [Compute Distance with Processing](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/3%20-%20Algorithms%20on%20Graphs/6%20-%20Advanced%20Shortest%20Path/dist_preprocess_small.py) (Bidirectional Dijkstra with preprocessing)

> Note: although the Bidirectional Dijkstra with preprocessing script returns the right results, its 
> preprocessing is too slow for the last test of the Compute Distance with Preprocessing (small) problem. The Bidirectional
> Dijkstra script from Friend Suggestion is fast enough for that problem, however.

---
### Lecture Notes
#### Brief Note
Some of these notes borrow from [Contraction Hierarchies: An Illustrative Guide](https://jlazarsfeld.github.io/ch.150.project/).
I would recommend reaching the guide - it is a very clear and approachable explanation of Contraction
Hierarchies.

#### Refresher: Shortest path
* **Input:** a graph G with non-negative edge weights, a source vertex
s and a target vertex t
* **Output:** the shortest path between s and t in G

Idea: growing circle
* do one turn of Djikstra from start
* do one turn of Djikstra from end
* repeat until both searches find the same node!
* reconstruct search from start to end

Original Djikstra covers an area of size `4*pi*r**2`, where
`r = 0.5 * d(start, end)`.

Bidirectional Djikstra covers two circles of size `pi*r**2`,
with start and end as origins - i.e., a total area of `2*pi*r**2`, half the
size of the search from 'regular' Djisktra.

#### Dijkstra Reminder
* Initialize dist[s] to 0, all other distances to inf
* ExtractMin - choose unprocessed u with smallest dist[u]
* Process u - relax edges outgoing from u
* Repeat until t is processed

The **reversed graph** `G^R` of a graph G is the graph with the
same set of vertices V and the set of reversed edges `E^R`, s.t.
for any edge (u, v) belonging to E there is an edge (v, u)
belonging to `E^R` and vice-versa.

#### Bidirectional Dijsktra: Implementation
* Build `G^R`
* start Dijkstra from s in G and from t in G^R
* Alernate between steps in G and G^R
* Stop when some vertex v is processed in both G and G^R
* Compute shortest path between s and t

#### Computing distance
Let v be the first vertex processed both in G and G^R. Does it follow
that there is a shortest path from s to t going through v? No!

Lemma: let dist[u] be the distance estimate in the forward estimate
in the forward Dijkstra from s in G and dist^r[u] - the same as the
distance in the backward Dijkstra from t in G^R.

After some node v is processed both in G and G^R, some shortest path
from s to t passes through some node u which is processed either in G,
in G^R, or both, and `d(s, t) = dist[u] + dist^R[u]`.

The worst-case running time of Bidirectional Dijkstra is the same as
for Dijkstra. The speedup time depends on the graph.

The memory consumption is 2x to store both G and G^R.

```
def BidirectionalDijkstra(G, start, end):
	G^R = ReverseGraph(G)

	dist = [inf for _ in vertices]
	dist_R = [inf for _ in vertices]
	prev = [None for _ in vertices]
	prev_R = [None for _ in vertices]

	dist[start] = 0
	dist_R[end] = 0

	proc = []
	proc_R = []

	while True:
		v = extractmin(dist)
		process(v, G, dist, prev, proc)
		if v in proc_R:
			return ShortestPath(start, dist, prev, proc, end)

		v_R = extractmin(dist_R)
		if v_R in proc:
			return ShortestPath(end, dist_R, prev_R, proc_R, start)

def Relax(u, v, dist, prev):
	if dist[v] > dist[u] + w(u, v):
		dist[v] = dist[u] + w(u, v)
		prev[v] = u

def Process(u, v, dist, prev, proc):
	for u,v in edges:
		Relax(u, v, dist, prev)
	proc.append(u)

def ShortestPath(start, dist, prev, proc, end):
	distance = inf
	u_best = None

	for u in proc + proc_R:
		if dist[u] + dist_R[u] < distance:
			u_best = u
			distance = dist[u] + dist_R[u]

	path = []
	last = u_best

	while last != start:
		path.append(last)
		last = prev[last]

	path = Reverse(path)
	last = u_best

	while last != end:
		last = prev_R[last]
		path.append(last)

	return (distance, path)
```

#### A-Start Algorithm
Take any **potential function** `p(v)` mapping vertices to real numbers.
It defines new edge weights `l_p(u, v) = l(u, v) - p(u) + p(v)`.
Replacing l by l_p does not change the shortest paths.

For any potential function p: V -> R, for any two vertices s and t 
in the graph and any path P between them,`l_p(P) = l(P) - p(s) + p(t)`.

Dijkstra with potentials:
* Take some potential function p
* Launch Dijkstra with edge weights l_p
* The resulting shortest path is also a shortest path initially

We need a `p` s.t. for any edge (u, v) the new length l_p(u, v) is non-negative - i.e., p must be *feasible*.

p(v) is an estimation of d(v, t). Typically, p(v) is a *lower
bound* on d(v, t) - i.e., on a real map a path from v to t
cannot be shorter than the straight line segment from v to t.

Dijkstra with potentials (again):
* On each step, pick the vertex v minimizing dist[v] - p(s) + p(v)
* p(s) is the same for all v, so v minimizes dist[v] + p(v)
* Pick the vertex v with the minimum current estimate of d(s, v) + d(v, t)

Performance of A*
* Worst case: `p(v) = 0` for all v - the same as Dijkstra
* Best case: `p(v) = d(v, t)` for all v - then, `l_p(u, v) = 0` iff (u, v) is on the shortest path
to t, so search visits only search the edges of shortest s - t paths

The tighter the lower bounds, the better the performance.

#### Bidirectional A*
We need two potential functions, `p_f(v)`, estimating `d(v, t)`, and `p_r(v)`, estimating
`d(s, v)`.

Problem: different edge weights
Solution? We need l_pf(u, v) = l_pr(u, v).
use pf(u) = (pf(u) - pr(u)) / 2 and pr(u) = -pf(u)
then pf(u) + pr(u) = 0 for any u

Lemma: if p is feasible and p(t) <= 0 then p(v) <= d(v, t) for any v.

Lemma: Consider a road network on a plane map with each vertex v
having coordinates (x1, y1).

The potential given by Eudlidean distance between v and t 
`p(v) = d_e(v, t) = ((x1 - x2)**2 + (y1 - y1)**2)**0.5` is feasible
and `p(t) = 0`.

For any edge (u, v) in edges, `l(u, v) >= d_e(u, v)` because line segments
are the shortest path between two points on a plane.

To find the shortest path from s to t:
* For each v, compute `p(v) = d_e(v, t)`
* Launch Dijkstra with potentials `p(v)`

#### Contraction Hierarchies
The **Contraction Hierarchies** algorithm uses a process of *node contraction* to create a hierarchy in which every node 
belongs to a unique level (in other words, an ordering of nodes based on importance).

During the contraction process, a set of shortcut edges is added to the graph that preserves shortest paths. 
The bidirectional search then only considers the **subset** of edges that lead from less important to more important nodes. 
The result is faster querying with only a modest increasing in preprocessing.

#### Node Contraction
When we contract a node, we first remove it from the graph. If the contracted node existed on the shortest path between 
two of its neighbors before contraction, we add a shortcut edge between the two neighbors such that all shortest path 
lengths are still preserved.

The output of node contraction is an augmented graph + ordering of nodes.

#### Finding Shortcuts (Witness Search)
When contracting a node v, we consider the set of all vertices with edges incoming to v as U, and the set of all vertices with incoming edges from v as W.

So we can do the following for every u in U:
* For every node w in W, compute Pw as the cost from u to w through v, `w(u, v) + w(v, w)`.
* Call the maximum Pw over all w in W Pmax.
* Perform a standard Dijkstra’s shortest-path search from u on the subgraph *excluding v*.
* Stop the search once we reach a node with a shortest-path distance greater than Pmax.

We can also speed up the search by only considering shortest paths from w with at most k edges. If a witness path isn't found
in this search, we can add a shortcut.

#### Optimal Node Ordering
Our algorithm works for any node ordering but the speed of both the preprocessing and querying steps are heavily
dependent on our contraction order.

We want to:
* minimize the number of added shortcuts
* spread the important nodes across the graph

Algorithm:
* keep all nodes in a priority queue by decreasing importance
* on each iteration, extract the least important node
* recompute its importance
* if it's still minimal (compared w/ the top of priority queue), contract the node
* else put back into priority queue with new priority

Eventual stopping
* if we don't contract a node, we update its importance
* after at most len(vertices) attempts all nodes have update importance
* the node with the minimum updated importance will be contracted after that

Importance criteria
* edge difference
	* `ed(v)` = number of added shortcuts - number of incoming edges - number of outgoing edges
	* number of edges increases by `ed(v)` after contracting v
	* contract node with small `ed(v)`
* number of contracted neighbors
	* want to spread the contracted vertices across the graph -> contract the node with small number of contracted neighbors
* shortcut cover
	* want to contract important nodes late
	* sc(v) = the number of neighbors w of v s.t. we have to shortcut to or from w after 
	contracting v
	* contract nodes with small sc(v) - few nodes depend on v
* node level
	* initially L(v) = 0
	* after contracting node v, for neighbors u of v do L(u) = max(L(u), L(v) + 1)
	* contract node with small L(v) - upper bound on the number of edges in the shortest
	path from s to v in the augmented graph

We will use importance `I(v) = ed(v) + cn(v) + sc(v) + L(v)`. The weights of the different components of 
importance can be changed.

#### Overlay Graph
After contracting the last node we consider the overlay graph G* that contains all original nodes and edges and all 
shortcut edges added during the contraction process. This is the graph used for our bidirectional Dijkstra searches.

#### Bidirectional Dijkstra w/ upwards edges
This Dijkstra search only considers edges with higher importance.

We run a **complete** Dijkstra search on both of these upward graphs, meaning that **all** nodes in both subgraphs must be settled. 
In both searches, the number of settled nodes and relaxed edges is significantly reduced than if we were searching on the entire G* graph.

After running two complete Dijkstra searches on G*U from both the source and target, we have a set of nodes that are 
settled in both searches. We denote this set as L.

For every node v in L, we sum the shortest path scores of v (one score from s, one from t). The shortest path distance 
then is the minimum sum over all v in L.
