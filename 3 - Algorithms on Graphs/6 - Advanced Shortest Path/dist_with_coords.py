import sys
import queue


class AStar:
    def __init__(self, n, adj, cost, vertices):
        self.n = n
        self.adj = adj
        self.cost = cost
        self.vertices = vertices

        self.inf = n * 10 ** 6
        self.distance = [
            self.inf
        ] * n
        self.estimated_distance = [self.inf] * n
        self.visited = [
            False
        ] * n
        self.workset = set()
        self.q = queue.PriorityQueue()

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        self.distance = [self.inf] * n
        self.estimated_distance = [self.inf] * n
        self.visited = [False] * n
        self.workset = set()
        self.q = queue.PriorityQueue()

    def euclidean_dist(self, node1, node2):
        x1, y1 = node1
        x2, y2 = node2
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def process(self, node):
        """Add valid nodes to the queue."""
        self.visited[node] = True
        self.workset.add(node)
        other_nodes = self.adj[node]
        destination = self.objective  # location of either start or end

        for ix in range(len(other_nodes)):
            new_node = other_nodes[ix]
            new_dist = self.distance[node] + cost[node][ix]

            if self.distance[new_node] > new_dist:
                # Update actual distance
                self.distance[new_node] = new_dist

                # Update estimated distance (full path)
                euclidean_dist = self.euclidean_dist(
                    self.vertices[new_node], self.vertices[destination]
                )
                euclidean_dist = round(euclidean_dist)
                self.estimated_distance[new_node] = new_dist + euclidean_dist

                # Add to queue
                self.q.put((self.estimated_distance[new_node], new_node))

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
        self.q.put((0, start))
        self.distance[start] = 0
        self.objective = end

        while self.q.qsize() > 0:
            _, forward_node = self.q.get()
            if forward_node == end:
                return self.distance[end]
            self.process(forward_node)

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == "__main__":
    n, m = readl()
    vertices = []
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        vertices.append((a, b))
    for e in range(m):
        u, v, c = readl()
        adj[u - 1].append(v - 1)
        cost[u - 1].append(c)
    (t,) = readl()
    astar = AStar(n, adj, cost, vertices)

    for i in range(t):
        s, t = readl()
        print(astar.query(s - 1, t - 1))
