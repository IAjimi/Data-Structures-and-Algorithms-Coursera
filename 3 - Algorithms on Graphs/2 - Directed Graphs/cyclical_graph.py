import sys


class CyclicalGraph():
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        self.visited = set()

    def dfs(self, node, cyclic=False):
        self.visited.add(node)
        self.recently_visited.add(node)

        for adj_node in self.adj[node]:
            if adj_node not in self.visited:
                cyclic = self.dfs(adj_node, cyclic)
            elif adj_node in self.recently_visited:
                cyclic = True

        self.recently_visited.remove(node)
        return cyclic

    def acyclic(self):
        for node in range(self.n):
            if node not in self.visited:
                self.recently_visited = set()
                if self.dfs(node):
                    return 1

        return 0


def read_input():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    return n, adj


if __name__ == '__main__':
    n, adj = read_input()
    print(CyclicalGraph(n, adj).acyclic())
