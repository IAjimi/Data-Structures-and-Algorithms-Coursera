def arrange_heap(heap):
	swap = []
	for ix in range(len(heap)-1, 0, -1):
		current = ix
		prev_node = ix // 2 if ix % 2 != 0 else ix // 2 - 1

		while heap[prev_node] > heap[current]:
			swap.append((prev_node, current))
			current = prev_node
			prev_node = current // 2 if current % 2 != 0 else current // 2 - 1

		if current != ix:
			#swap.append((ix, current))  # this minimizes number of swaps
			heap[ix], heap[current] = heap[current], heap[ix]

	return swap

def main():
	n = int(input())
	data = list(map(int, input().split()))
	assert len(data) == n

	swaps = arrange_heap(data)

	print(len(swaps))
	for i, j in swaps:
		print(i, j)


if __name__ == '__main__':
	main()
