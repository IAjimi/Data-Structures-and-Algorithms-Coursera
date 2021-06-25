import sys
import queue

def distance(adj, start, end):
    _queue = queue.PriorityQueue()
    _queue.put((0, start))
    visited = set()

    while not _queue.empty():
        steps, node = _queue.get()

        if node == end:
            return steps

        visited.add(node)
        adj_nodes = [new_node for new_node in adj[node] if new_node not in visited]

        for new_node in adj_nodes:
            _queue.put((steps + 1, new_node))

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
