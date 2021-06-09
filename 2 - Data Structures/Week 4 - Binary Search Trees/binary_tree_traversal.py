import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.result = []
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.key[i] = a
			self.left[i] = b
			self.right[i] = c


	def InOrderTraversal(self, node_ix):
		if self.left[node_ix] != -1:
			self.InOrderTraversal(self.left[node_ix])

		self.result.append(self.key[node_ix])

		if self.right[node_ix] != -1:
			self.InOrderTraversal(self.right[node_ix])

	def inOrder(self):
		self.result = []
		self.InOrderTraversal(0)
		return self.result

	def preOrderTraversal(self, node_ix):
		self.result.append(self.key[node_ix])

		if self.left[node_ix] != -1:
			self.preOrderTraversal(self.left[node_ix])

		if self.right[node_ix] != -1:
			self.preOrderTraversal(self.right[node_ix])

	def preOrder(self):
		self.result = []
		self.preOrderTraversal(0)
		return self.result

	def postOrderTraversal(self, node_ix):
		if self.left[node_ix] != -1:
			self.postOrderTraversal(self.left[node_ix])

		if self.right[node_ix] != -1:
			self.postOrderTraversal(self.right[node_ix])

		self.result.append(self.key[node_ix])

	def postOrder(self):
		self.result = []
		self.postOrderTraversal(0)
		return self.result


def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
