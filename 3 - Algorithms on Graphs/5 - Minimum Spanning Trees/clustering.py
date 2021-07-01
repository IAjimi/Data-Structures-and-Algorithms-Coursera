import sys

class Clustering():
	def __init__(self):
		input = sys.stdin.read()
		data = list(map(int, input.split()))
		n = data[0]
		data = data[1:]
		x = data[0:2 * n:2]
		y = data[1:2 * n:2]
		k = data[-1]

		self.n = n
		self.k = k
		self.vertices = list(zip(x, y))
		self.edges, self.distances = self.calc_all_dist()

	def calc_dist(self, node1, node2):
		x1, y1 = node1
		x2, y2 = node2
		return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

	def calc_all_dist(self):
		edges = [(ix, jx) for ix in range(self.n) for jx in range(ix + 1, self.n)]
		distances = [self.calc_dist(self.vertices[ix], self.vertices[jx]) for ix in range(self.n) for jx in range(ix + 1, self.n)]
		return edges, distances

	def kruskal(self):
		"""
		The clustering is done using Kruskal's algorithm. The algorithm is terminated when the points have
		been grouped into k distinct sets. The weight of the next node that would've joined either set
		is then equal to the smallest remaining distance between the points of the k sets.

		I didn't feel like implementing a disjoint set structure so I instead created 2 dictionaries:
		* vertice_set_mapping: links a vertices index in self.vertices to a set number (what set does vertice v belong to?)
		* all_sets: links a set number to a set (what vertices are in set s?)

		Suppose we are joining node 1 (ix 1) and node 2 (ix 2)'s.
		This is before the join:
			vertice_set_mapping = {0: 1, 1: 1, 2: 2, 3: 3, 4: 3}
			all_sets = {1: set(0, 1), 2: set(2), 3: set(3, 4)}
		This is after the join:
			vertice_set_mapping = {0: 1, 1: 1, 2: 1, 3: 3, 4: 3}
			all_sets = {1: set(0, 1, 2), 3: set(3, 4)}
		"""
		vertice_set_mapping = {ix: ix for ix in range(self.n)}
		all_sets = {ix: set([ix]) for ix in range(self.n)}

		# Sort edges by weight
		sorted_edges = [(edge, dist) for dist, edge in sorted(zip(self.distances, self.edges))]

		# Iterate over edges
		for ix in range(len(sorted_edges)):
			# Get name of node 1, node 2 set
			node1, node2 = sorted_edges[ix][0]
			node1_set_name = vertice_set_mapping[node1]
			node2_set_name = vertice_set_mapping[node2]

			if node1_set_name != node2_set_name:
				# Check whether clustering is complete
				if len(all_sets) <= self.k:
					return sorted_edges[ix][1]

				# Get node 1, node 2 sets
				node1_set = all_sets[node1_set_name]
				node2_set = all_sets[node2_set_name]

				# Merge sets
				all_sets[node1_set_name] = node1_set.union(node2_set)  # add set 2 to set 1
				del all_sets[node2_set_name]  # remove node 2's set

				# Update set pointers
				for node in all_sets[node1_set_name]:
					vertice_set_mapping[node] = node1_set_name

		return sorted_edges[-1][1]


	def solve(self):
		solution = self.kruskal()
		print("{0:.9f}".format(solution))


if __name__ == '__main__':
	Clustering().solve()

