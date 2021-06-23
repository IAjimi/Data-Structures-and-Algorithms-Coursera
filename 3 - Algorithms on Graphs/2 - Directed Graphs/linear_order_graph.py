import sys


class Graph():
	def __init__(self, n, adj):
		self.n_vertices = n
		self.adj = adj

		self.visited = set()
		self.order = []

	def explore(self, node):
		self.visited.add(node)
		for new_node in self.adj[node]:
			if new_node not in self.visited:
				self.explore(new_node)

		self.order.append(node + 1)

	def topoSort(self):
		for node in range(self.n_vertices):
			if node not in self.visited:
				self.explore(node)

		return self.order[::-1]

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
	postorder = Graph(n, adj).topoSort()
	postorder = [str(c) for c in postorder]
	print(' '.join(postorder), end=' ')
