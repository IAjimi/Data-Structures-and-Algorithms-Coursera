"""Bidirectional Dijkstra.

Using heapq instead of queue pushes this from 1.4s to 1s for n = 100, m = 1000, q = 1000."""

import sys
import heapq


class BidirectionalDijkstra:
    def __init__(self, n, adj, cost):
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n * 10 ** 6
        self.distance = [
            [self.inf] * n,
            [self.inf] * n,
        ]  # initialize distances for forward and backward searches
        self.visited = [
            [False] * n,
            [False] * n,
        ]  # visited[v] == True iff v was visited by forward or backward search
        self.workset = set()  # all the nodes visited by forward or backward search
        self.q = [
            [],
            [],
        ]  # forward and backward priority queues

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        self.distance = [[self.inf] * n, [self.inf] * n]
        self.visited = [[False] * n, [False] * n]
        self.workset = set()
        self.q = [[], []]

    def process(self, side, node):
        """Add valid nodes to the queue."""
        self.visited[side][node] = True
        self.workset.add(node)
        other_nodes = self.adj[side][node]

        for ix in range(len(other_nodes)):
            new_node = other_nodes[ix]
            dist = cost[side][node][ix]

            if self.distance[side][new_node] > self.distance[side][node] + dist:
                self.distance[side][new_node] = self.distance[side][node] + dist
                heapq.heappush(self.q[side], (self.distance[side][new_node], new_node))

    def ShortestPath(self):
        """Find shortest path."""
        distance = self.inf

        for node in self.workset:
            node_dist = self.distance[0][node] + self.distance[1][node]
            if node_dist < distance:
                distance = node_dist

        return distance

    def query(self, start, end):
        self.clear()
        heapq.heappush(self.q[0], (0, start))
        heapq.heappush(self.q[1], (0, end))
        self.distance[0][start] = 0
        self.distance[1][end] = 0

        while self.q[0] and self.q[1]:
            _, forward_node = heapq.heappop(self.q[0])
            self.process(0, forward_node)
            if self.visited[1][forward_node]:
                return self.ShortestPath()

            _, backward_node = heapq.heappop(self.q[1])
            self.process(1, backward_node)
            if self.visited[0][backward_node]:
                return self.ShortestPath()

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == "__main__":
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)

    bd = BidirectionalDijkstra(n, adj, cost)

    print("Ready")
    sys.stdout.flush()
    (t,) = readl()
    for i in range(t):
        s, t = readl()
        print(bd.query(s - 1, t - 1))

