'''Valid answers but too slow for final case. Being optimized.'''

import sys
import queue
from copy import deepcopy

# Maximum allowed edge length
maxlen = 2 * 10 ** 6


class DistPreprocessSmall:
    def __init__(self, n, adj, cost):
        self.n = n
        self.adj = deepcopy(adj)
        self.cost = deepcopy(cost)
        self.inf = n * 10 ** 6
        self.distance = [
            [self.inf] * n,
            [self.inf] * n,
        ]  # initialize distances for forward and backward searches
        self.visited = [[False] * n]
        self.workset = set()  # all the nodes visited by forward or backward search
        self.q = [
            queue.PriorityQueue(),
            queue.PriorityQueue(),
        ]  # forward and backward priority queues
        self.level = [0] * n  # Levels of nodes for node ordering heuristics
        self.contraction_order = {
            v: 0 for v in range(self.n)
        }  # so self.visit will work in preprocessing

        # Preprocess graph
        contracted_nodes, all_shortcuts = self.preprocess()
        self.adj = adj  # reset adj
        self.cost = cost  # reset cost
        self.contraction_order = {v: ix for ix, v in enumerate(contracted_nodes)}
        self.add_shortcuts(all_shortcuts)

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        self.distance = [[self.inf] * n, [self.inf] * n]
        self.visited = [[False] * n, [False] * n]
        self.workset = set()
        self.q = [queue.PriorityQueue(), queue.PriorityQueue()]

    def find_shortcuts(self, v):
        """
        Find all the shortcuts going through v.

        :input v: int, node name
        :return: list[tuple], shortest paths going through v
        """
        shortcuts = []
        incoming_nodes = self.adj[1][v]
        outgoing_nodes = self.adj[0][v]

        # Node leads nowhere or comes from nowhere
        if not incoming_nodes or not outgoing_nodes:
            return shortcuts

        for ix in range(len(incoming_nodes)):
            incoming_node = incoming_nodes[ix]

            all_v_dist = [self.cost[0][v][jx] + self.cost[1][v][ix] for jx in range(len(outgoing_nodes))]
            max_dist = max(all_v_dist)  # max v dist - Dijkstra will terminate after reaching max_dist

            self.Dijkstra(incoming_node, set(outgoing_nodes), max_dist, v)

            for jx in range(len(outgoing_nodes)):
                outgoing_node = outgoing_nodes[jx]
                this_v_dist = all_v_dist[jx]

                if this_v_dist <= self.distance[0][outgoing_node]:
                    shortcuts.append((incoming_node, outgoing_node, this_v_dist))

        return shortcuts

    def add_shortcuts(self, shortcuts):
        """
        Add shorcuts to adjacency list.

        :input shortcuts: list[tuple], shortest paths going through some node
        """
        for node1, node2, dist in shortcuts:
            self.adj[0][node1].append(node2)
            self.cost[0][node1].append(dist)

            self.adj[1][node2].append(node1)
            self.cost[1][node2].append(dist)

    def update_levels(self, node):
        """
        Update node levels after contraction. Part of importance calculation.

        :input node: int, node name/number
        """
        node_level = self.level[node]
        neighbors = self.adj[0][node] + self.adj[1][node]
        self.level = [
            max(level, node_level + 1) if ix in neighbors else 0
            for ix, level in enumerate(self.level)
        ]

    def contract_node(self, node, shortcuts):
        """
        Contract node: remove all references to edge in self.adj and self.cost,
        add shortcuts.

        :input node: int, node name / number
        :input shortcuts: list[tuples], (from_node, to_node, dist_node), shortcuts replacing node
        """
        # Remove edges from node
        self.adj[0][node] = []
        self.adj[1][node] = []
        self.cost[0][node] = []
        self.cost[1][node] = []

        # Remove all references to node
        for ix in range(self.n):  # get sublist in self.adj[0] etc
            self.cost[0][ix] = [
                self.cost[0][ix][jx]
                for jx in range(len(self.adj[0][ix]))
                if self.adj[0][ix][jx] != node
            ]
            self.adj[0][ix] = [
                self.adj[0][ix][jx]
                for jx in range(len(self.adj[0][ix]))
                if self.adj[0][ix][jx] != node
            ]
            self.cost[1][ix] = [
                self.cost[1][ix][jx]
                for jx in range(len(self.adj[1][ix]))
                if self.adj[1][ix][jx] != node
            ]
            self.adj[1][ix] = [
                self.adj[1][ix][jx]
                for jx in range(len(self.adj[1][ix]))
                if self.adj[1][ix][jx] != node
            ]

        # Add edges (shortcuts)
        self.add_shortcuts(shortcuts)

    def preprocess(self):
        """
        1. Get an estimate of importance for every node, based on edge difference.
        Place nodes in queue with importance = edge_difference.
        2. Extract the least important node.
        3. Recompute its importance.
        4. Compare with top of priority queue: if lower, contract the node.
        Else return to priority queue with updated priority.

        Return contracted nodes, in order, and shortcuts.
        """
        # Start by getting edge difference of every node
        preprocessing_queue = queue.PriorityQueue()

        for node in range(self.n):
            shortcuts = self.find_shortcuts(node)
            estimated_importance = (
                len(shortcuts) - len(self.adj[0][node]) - len(self.adj[1][node])
            )
            preprocessing_queue.put((estimated_importance, node))

        # Go through queue
        all_shortcuts = []
        contracted_nodes = []  # appends in order so also stores contraction order for now

        while preprocessing_queue.qsize() > 0:
            # Retrieve node with min imp
            _, node = preprocessing_queue.get()

            # If there still is a node in the queue, recalculate the importance of the node
            # and compare to top of queue
            if preprocessing_queue.qsize() >= 1:
                shortcuts = self.find_shortcuts(node)
                recalculated_imps = self.calculate_importance(
                    node, contracted_nodes, shortcuts
                )
                second_imp, second_node = preprocessing_queue.get()
                preprocessing_queue.put((second_imp, second_node))
            else:
                second_imp = self.inf

            # Either contract node or put it back in queue
            if recalculated_imps <= second_imp:
                contracted_nodes.append(node)
                self.update_levels(node)
                self.contract_node(node, shortcuts)
                all_shortcuts.extend(shortcuts)
            else:
                preprocessing_queue.put((recalculated_imps, node))

        return contracted_nodes, all_shortcuts

    def calculate_importance(self, node, contracted_nodes, shortcuts):
        """
        Compute the importance of a node.

        :input node: int
        :input contracted_nodes: list[int], contracted nodes
        :input shortcuts: list[tuple], shortest paths going through node

        :return importance: int
        """
        neighbors = self.adj[0][node] + self.adj[1][node]

        # Compute components of importance
        edge_difference = (
            len(shortcuts) - len(self.adj[0][node]) - len(self.adj[1][node])
        )
        contracted_neighbors = sum([1 for n in neighbors if n in contracted_nodes])
        shortcut_cover = 0
        node_level = self.level[node]

        # Compute importance
        importance = (
            edge_difference + contracted_neighbors + shortcut_cover + node_level
        )
        return importance

    def visit(self, side, _queue, node):
        """Add valid nodes to the queue.

        :param side: int, 0 for forward search, 1 for backward search
        :param _queue: priority queue
        :param node: int, starting node
        """
        self.visited[side][node] = True
        self.workset.add(node)
        other_nodes = self.adj[side][node]

        for ix in range(len(other_nodes)):
            new_node = other_nodes[ix]
            new_dist = self.distance[side][node] + self.cost[side][node][ix]

            if (
                new_dist < self.distance[side][new_node]
                and not self.visited[side][new_node]
                and self.contraction_order[new_node] >= self.contraction_order[node]  # in preprocessing, all nodes have order 0
            ):
                self.distance[side][new_node] = new_dist
                _queue.put((new_dist, new_node))

        return _queue

    def Dijkstra(self, start, end, max_dist, blacklisted_node=None):
        """Single Dijkstra.

        :param start: int, starting node
        :param end: set(int), ending nodes
        :param max_dist: int, maximum distance
        :param blacklisted_node: int, blacklisted node
        """
        self.clear()
        dist = 0
        _queue = queue.PriorityQueue()
        self.distance[0][start] = dist
        _queue.put((dist, start))

        # Heuristic: max number of moves thru Dijkstra before ending search
        turns = 0
        k = len(end) * 3

        # Optional: removing node from search
        if blacklisted_node:
            self.visited[0][
                blacklisted_node
            ] = True  # this will stop self.visit from considering this node

        while (
            _queue.qsize() > 0
            and end.difference(self.workset) != set()
            and dist < max_dist
            and turns < k
        ):
            dist, node = _queue.get()
            _queue = self.visit(0, _queue, node)
            turns += 1

    def query(self, start, end):
        """
        Run query. Returns shortest path between the two nodes.
        Complete Bidirection Dijkstra search.
        """
        self.clear()
        self.q[0].put((0, start))
        self.q[1].put((0, end))
        self.distance[0][start] = 0
        self.distance[1][end] = 0

        while self.q[0].qsize() > 0 or self.q[1].qsize() > 0:
            if self.q[0].qsize() > 0:
                _, forward_node = self.q[0].get()
                if not self.visited[0][forward_node]:
                    self.visit(0, self.q[0], forward_node)

            if self.q[1].qsize() > 0:
                _, backward_node = self.q[1].get()
                if not self.visited[1][backward_node]:
                    self.visit(1, self.q[1], backward_node)

        return self.ShortestPath()

    def ShortestPath(self):
        """Find shortest path."""
        distance = self.inf

        for node in self.workset:
            node_dist = self.distance[0][node] + self.distance[1][node]
            if node_dist < distance:
                distance = node_dist

        if distance < self.inf:
            return distance
        else:
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

    ch = DistPreprocessSmall(n, adj, cost)

    print("Ready")
    sys.stdout.flush()
    (t,) = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s - 1, t - 1))
