def _eval(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return 0

def MinAndMax(op, m, M, i, j):
	_min = 10000000
	_max = -10000000
    
	for k in range(i, j): # all possible splits
		opk = ops[k]
		a = _eval(M[(i, k)], M[(k + 1, j)], opk)
		b = _eval(M[(i, k)], m[(k + 1, j)], opk)
		c = _eval(m[(i, k)], M[(k + 1, j)], opk)
		d = _eval(m[(i, k)], m[(k + 1, j)], opk)
        
		_min = min(_min, a, b, c, d)
		_max = max(_max, a, b, c, d)

	return _min, _max

def Parentheses(d, ops):
	m, M = {}, {}
	n = len(d)

	for i in range(0, n): # initialize min max values
		m[(i, i)] = d[i]
		M[(i, i)] = d[i]

	for s in range(1, n):
		for i in range(0, n - s):
			j = i + s
			m[(i, j)], M[(i, j)] = MinAndMax(ops, m, M, i, j)

	return M[(0, n - 1)] # max of initial expression

if __name__ == "__main__":
    dataset = input()
    d = list(map(int, dataset[0::2]))
    ops = list(dataset[1::2])
    print(Parentheses(d, ops))