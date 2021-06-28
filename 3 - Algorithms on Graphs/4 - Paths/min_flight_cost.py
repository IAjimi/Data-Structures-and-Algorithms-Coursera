import sys
import queue

def distance(adj, cost, start, end):
    _queue = queue.PriorityQueue()
    _queue.put((0, start))
    visited = set()

    while not _queue.empty():
        steps, node = _queue.get()

        if node == end:
            return steps

        visited.add(node)

        for ix in range(len(adj[node])):
            new_node = adj[node][ix]
            if new_node not in visited:
                _queue.put((steps + cost[node][ix], new_node))

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
