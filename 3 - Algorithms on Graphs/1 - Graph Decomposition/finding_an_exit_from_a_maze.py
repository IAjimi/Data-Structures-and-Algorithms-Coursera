import sys


def reach(adj, x, y):
    queue = [x]
    visited = set()

    while queue:
        new_node = queue.pop(0)

        if new_node == y:
            return 1

        visited.add(new_node)

        neighbors = [n for n in adj[new_node] if n not in visited and n not in queue]
        queue.extend(neighbors)

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]

    adj = [[] for _ in range(n)]  # adj[0] are nodes 0 are next to
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
