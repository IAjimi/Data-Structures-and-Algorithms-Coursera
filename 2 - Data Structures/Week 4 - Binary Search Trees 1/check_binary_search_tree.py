import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
	def __init__(self, n, key, left, right):
		self.n = n
		self.key = key
		self.left = left
		self.right = right

	def isBST(self, node_ix, mini, maxi):
		if node_ix == -1:
			return True

		if self.key[node_ix] < mini:
			return False
		if self.key[node_ix] > maxi:
			return False

		return self.isBST(self.left[node_ix], mini, self.key[node_ix]) and self.isBST(self.right[node_ix], self.key[node_ix], maxi)

	def solve(self):
		if self.n > 0:
			mini, maxi = float('-inf'), float('inf')
			bool = self.isBST(0, mini, maxi)
		else:
			bool = True


		if bool:
			return 'CORRECT'
		else:
			return "INCORRECT"

def read():
	n = int(sys.stdin.readline())
	key = [0 for i in range(n)]
	left = [0 for i in range(n)]
	right = [0 for i in range(n)]
	for i in range(n):
		[a, b, c] = map(int, sys.stdin.readline().split())
		key[i] = a
		left[i] = b
		right[i] = c

	return n, key, left, right

def main():
	n, key, left, right = read()
	tree = TreeOrders(n, key, left, right)
	solution = tree.solve()
	print(solution)

threading.Thread(target=main).start()