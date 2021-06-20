## Algorithms on Graphs Week 2
### Graph Decomposition 2

* [Checking consistency of CS curriculum]() (Is graph cyclical?)
* [Determining an order of courses]() (Find an order in which the whole graph can be visited linearly)

---

### Lecture Notes
#### Directed Graphs
A **directed graph** is a graph where each edge has a start and end vertex.

We can still run DFS:
* we only follow directed edges
* explore(v) finds all vertices reachable from v

We could order everything linearly, as long as there isn't a *cycle* in the dependencies.

A **cycle** in a graph G is a sequence of vertices s.t.
`(v1, v2), (v2, v3), ..., (vn-1, vn), (vn, v1)` are all edges.

#### Linear Order
Any DAG can be linearly ordered.

Terminology:
* A **source** is a vertex with no incoming edges.
* A **sink** is a vertex with no outgoing edges.

Naive algorithm:
```
def linear_order(G):
	# follow a path until end
	# find sink v
	# put v at the end of order
	# remove v from G
	# repeat
```

Runtime is `O(len(v)**2)`... 
We retrace the same path every time! We could instead just back up one step - this is just DFS, sorting vertices by 
reverse post-order.

#### Strongly Connected Components
A directed graph can be partitioned into **strongly connected components**
where two vertices if and only if they are in the same component - i.e., once you leave you can't come back.

We can use SCCs to create a metagraph showing how strongly connected components connect to one another.