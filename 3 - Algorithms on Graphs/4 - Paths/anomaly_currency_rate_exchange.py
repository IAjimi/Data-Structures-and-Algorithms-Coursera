import sys

class Solution():
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.dist = []
        #self.prev = []

    def initialize_dist(self):
        self.dist = [999999999 for node in range(self.n)]
        #self.prev = [0 for node in range(self.n)]


    def relax(self, node, other_node, weight):
        if self.dist[other_node] > self.dist[node] + weight:
            self.dist[other_node] = self.dist[node] + weight
            #self.prev[other_node] = node
            return True
        return False


    def BellmanFord(self, start=0):
        self.initialize_dist()
        self.dist[start] = 0

        # 1st iteration
        for _ in range(self.n - 1):
            for nodes, weight in self.edges:
                node, other_node = nodes
                self.relax(node - 1, other_node - 1, weight)

        # 2nd iteration - if any edges are relaxed, there is a cycle
        for nodes, weight in self.edges:
            node, other_node = nodes
            relaxed = self.relax(node - 1, other_node - 1, weight)
            if relaxed:
                return 1
        return 0

def main(_input):
    data = list(map(int, _input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))

    is_cycle = Solution(n, edges).BellmanFord()
    return is_cycle

if __name__ == '__main__':
    _input = sys.stdin.read()
    is_cycle = main(_input)
    print(is_cycle)


