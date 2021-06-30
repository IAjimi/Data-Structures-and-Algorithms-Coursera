import sys
import queue

class JoinNodes():
	def __init__(self):
		input = sys.stdin.read()
		data = list(map(int, input.split()))
		x = data[1::2]
		y = data[2::2]

		self.n = data[0]
		self.vertices = list(zip(x, y))

	def dist(self, node1, node2):
		x1, y1 = node1
		x2, y2 = node2
		return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


	def prim(self):
		visited = set()
		visit_set = set(self.vertices)
		cost = [9999999 for _ in self.vertices]

		cost[0] = 0
		_queue = queue.PriorityQueue()
		_queue.put((0, self.vertices[0]))

		total_cost = 0

		while visited != visit_set:
			current_cost, node = _queue.get()

			if node not in visited:
				visited.add(node)
				total_cost += current_cost

				for ix in range(self.n):
					other_node = self.vertices[ix]

					_dist = self.dist(node, other_node)
					if other_node not in visited and cost[ix] > _dist:
						cost[ix] = _dist
						_queue.put((cost[ix], other_node))

		return total_cost

	def solve(self):
		solution = self.prim()
		print("{0:.9f}".format(solution))


if __name__ == '__main__':
	JoinNodes().solve()
