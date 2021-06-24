import sys

class Solution:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def subgraph_isBipartite(self, start):
        queue = [start]
        color = [None for _ in range(self.n)]
        color[start] = 1
        visited = set()

        while queue:
            node = queue.pop(0)
            visited.add(node)

            if color[node] is not None:
                new_color = 1 if color[node] == 0 else 0

                for neighbor in self.graph[node]:
                    if color[neighbor] is None:
                        color[neighbor] = new_color
                        queue.append(neighbor)

                    elif color[neighbor] != new_color:
                        return False, set()

        return True, visited


    def isBipartite(self):
        queue = [n for n in range(self.n)]

        while queue:
            start = queue.pop(0)
            isb, visited = self.subgraph_isBipartite(start)
            if not isb:
                return False
            queue = [q for q in queue if q not in visited]

        return True


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

    result = Solution(adj).isBipartite()
    print(1 if result else 0)




