import sys


def number_of_components(vertices, adj):
	result = 0

	while vertices:
		start = vertices[0]
		visited = explore(adj, start)
		vertices = [v for v in vertices if v not in visited]
		result += 1

	return result

def explore(adj, start):
	queue = [start]
	visited = set()

	while queue:
		new_node = queue.pop(0)
		visited.add(new_node)
		neighbors = [n for n in adj[new_node] if n not in visited and n not in queue]
		queue.extend(neighbors)

	return visited

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
	vertices = [_ for _ in range(n)]

	print(number_of_components(vertices, adj))
