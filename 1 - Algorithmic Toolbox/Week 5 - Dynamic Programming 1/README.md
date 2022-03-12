## Algorithmic Toolbox Week 5

* [Making change (dynamic programming)](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%205%20-%20Dynamic%20Programming%201/week5_part1_change_dp.py)
* [Primitive calculator](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%205%20-%20Dynamic%20Programming%201/week5_part2_primitive_calculator.py)
* [Minimum edit distance](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%205%20-%20Dynamic%20Programming%201/week5_part3_edit_distance.py)

---
## Dynamic Programming
### Money Exchange
What is the minimum number of coins needed to change x cents for denominations 6, 5, and 1?

Starting from left of array `A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, we derive `MinNumCoins = [0, 1, 2, 3, 4, 1, 1, 2, 3, 4]`.

```
DPChange(money, coins):
	MinNumCoins(0) = 0

	for m in range(1, money):
		for i in range(1, len(coins)):
			if m >= coin[i]:
				NumCoins = MinNumCoins(m - coin[i]) + 1

				if NumCoins < MinNumCoins(m):
					MinNumCoins(m) = NumCoins

	return MinNumCoins(money)
```

### The Alignment Game
Remove all symbols from two strings to maximize the number of points.

We can classify columns as
* matches
* insertions
* deletions
* mismatches

Our point system can give a premium for every match (+1), a penalty for every mismatch (-m), and a penalty for every insertion or deletion (-o).

#### Edit Distance
The **edit distance** is the min number of operations (insertions,
deletions and substitution) to transform one string into another.

Let `D(i, j)` be the edit distance of `A[1 ... i]`and `B[1 ... j]`.

```
D(i, j) = min( 
	D(i, j - 1) + 1, # insertion -> element in B, not A
	D(i - 1, j) + 1, # deletion -> element in A, not B
	D(i - 1, j - 1) + 1 # mismatch, if A[i] != B[j]
	D(i - 1, j - 1) # match, if A[i] == B[j]
	)
```

In other words, `D(i, j)` depends on `D(i - 1, j - 1)`, `D(i - 1, j)` and 
`D(i, j - 1)`, each of which map to an operation.

We can either start from the *very end* of a theoretical optimal arrangement
and going backwards thru recursion **or** move forward from 0,0 onwards.

Iterative solution: filling in a grid, starting at `0,0`, then `0 ... n, 0`
then `0, 0 ... m`, then move diagonally.
```
EditDistance(A, B):
	n, m = len(A), len(B)

	D(i, 0) = i for all i
	D(0, j) = j for all j

	for j from range(1, m):
		for i from range(1, n):
			insertion = D(i, j - 1) + 1
			deletion = D(i - 1, j) + 1
			match = D(i - 1, j - 1)
			mismatch = D(i - 1, j - 1) + 1

			if A[i] == B[j]:
				D(i, j) = min(insertion, deletion, match)
			else:
				D(i, j) = min(insertion, deletion, mismatch)

	return D(n, m)
```
#### Reconstructing an Optimal Alignment
We have computed the edit distance, but how can we find an optimal alignment?

Every edge only has one previous edge. Can find path that way.

Start with last vertex. Choose arbitrary edge.
```
OutputAlignment(i, j):
	if i == 0 and j == 0:
		return
	if backtrack(i, j) == 'down':
		OutputAlignment(i - 1, j)
		print(str(A[i]) + '\n' + '-')
	elif backtrack(i, j) == 'right':
		OutputAlignment(i, j - 1)
		print('-' + '\n' + str(B[j]))
	else:
		OutputAlignment(i - 1, j - 1)
		print(str(A[i]) + '\n' + str(B[j]))
```
<>
```
OutputAlignment(i, j):
	if i == 0 and j == 0:
		return
	if i > 0 and D(i, j) = D(i - 1, j) + 1:
		OutputAlignment(i - 1, j)
		print(str(A[i]) + '\n' + '-')
	elif j > 0 and D(i, j) = D(i, j - 1) + 1:
		OutputAlignment(i, j - 1)
		print('-' + '\n' + str(B[j]))
	else:
		OutputAlignment(i - 1, j - 1)
		print(str(A[i]) + '\n' + str(B[j]))
```

#### Longest Increasing Subsequence
Longest increasing subsequence: `ai1, ai2, ..., aik` s.t. `i1 < i2 < ... < ik` & `ai1 < ai2 < ... < aik` and `k` is maximal.

Consider the last element x of an optimal increasing subsequence & its previous element z. 
* `z < x`
* z should be optimal end of IS sequence if array ends at z
---> subproblem: the length of an optimal IS ending a z-th element

`LIS(i)`: optimal length of a LIS ending at `A[i]`
* `LIS(i) = 1 + max(LIS(j): j < i and A[j] < A[i])`
* base case: `LIS(0) = 1`

When we have a recurrence relation at hand, converting it to a
recursive algorithm with memorization is just a technicality.

**Recursion with memorization**: Store the results in a table T, s.t. `T[i] = LIS(i)`.
```
T = {}

def lis(A, i):
	if i not in T:
		T[i] = 1

		for j in range(i):
			if A[j] < A[i]:
				T[i] = max(T[i], lis(A, j) + 1)

	return T[i]
	
A = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3]
print(max(lis(A, i) for i in range(len(A))))
```

Running time is **quadratic** (`O(n**2)`): there are n serious recursive calls, each `O(n)`.

**Iterative Algorithm**
```
def lis(A):
	T = [None] * len(A)

	for i range(len(A)):
		T[i] = 1

		for j in range(i):
			if A[j] < A[i] and T[i] < T[j] + 1:
				T[i] = T[j] + 1

	return max(T[i] for i in range(len(A)))
```
When computing `T[i], T[j]`, all j < i have already been computed, giving us a 
`O(n**2)` running time.

#### Reconstructing optimal IS
Adjusting the algorithm:
```
def lis(A):
	T = [None] * len(A)
	prev = [None] * len(A)

	for i range(len(A)): # for every element in A
		T[i] = 1
		prev[i] = -1

		for j in range(i): # look at all previous elements
			if A[j] < A[i] and T[i] < T[j] + 1: # if increasing AND gives longer sequence length
				T[i] = T[j] + 1 # update sequence length
				prev[i] = j # update prev

	return max(T[i] for i in range(len(A)))
```

Unwinding solution:
```
last = 0
for i in range(1, len(A)):
	if T[i] > T[last]:
		last = i

	lis = []
	current = last
	while current >= 0:
		lis.append(current)
		current = prev[current]

	lis.reverse()

	return [A[i] for i in lis]
```
This found the solution by converting our recursive algorithm into an
iterative algorithm.

We can also brute force then optimize.

### Knapsack
#### Knapsack with repetitions
Consider an optimal solution and an item in it, `wi`.
If we take this item out then we get an optimal solution
for a knapsack of total weight `W - wi`.

This knapsack has `value(u) = max(value(u - wi) + vi)`.

Recursive Algorithm:
```
T = dict()

def knapsack(w, v, u):
	if u not in T:
		T[u] = 0

		for i in range(len(w)):
			if w[i] <= u:
				T[u] = max(T[u],
					knapsack(w, v, u - w[i]) + v[i])

	return T[u]
```

We can turn this recursive algorithm into an iterative one by gradually 
filling in an array T: `T[u] = value(u)`.
```
def knapsack(W, w, v):
	T = [0] * (W + 1)

	for u in range(1, W + 1): # for every capacity (increasing weight)
		for i in range(len(w)): # for every item
			if w[i] <= u: # if object fits in knapsack
				T[u] = max(T[u], T[u - w[i]] + v[i]) # is it better not to add it or to add it

	return T[W]
```

This has `O(nW)` runtime (n loop and W loop).

Alternatively, we can optimize a brute force solution:

```
def knapsack(W, w, v, items = []):
	weight = sum(w[i] for i in items)
	value = sum(v[i] for i in items)

	for i in range(len(w)):
		if weight + w[i] <= W:
			value = max(value, knapsack(W, w, v, items + [i]))

	return value
```
The only important thing for extending the current set of 
items is the weight of this set.


#### Knapsack without repetitions
If the last item is taken into an optimal solution then
what is left is an optimal solution for a knapsack of total
weight `W - w_n-1` using items `0, 1, ..., n - 2`.

For `0 <= u <= W` and `0 <= i <= n`, `value(u, i)` is the max
value achievable using a knapsack of weight u and the first i
items.

Base case: `value(u, 0) = 0`, `value(0, i) = 0`.

For `i > 0`, the item `i - 1` is either used or unsued:
```
value(u, i) = max(
			value(u - w[i - 1], i - 1) + v[i - 1],
			value(u, i -1)
		)
```
Recursive Algorithm:
```
T = {}

def knapsack(w, v, u, i):
	if (u, i) not in T:
		if i == 0:
			T[u, i] = 0
		else:
			T[u, i] = knapsack(w, v, u, i - 1)

			if u >= w[i - 1]:
				T[u, i] = max(
					T[u, i], 
					knapsack(w, v, u - w[i - 1], i - 1) + v[i - 1]
					)

	return T[u, i]
```
Iterative Algorithm:
```
def knapsack(w, v, u, i):
	T = [[None] * (len(w) + 1) for _ in range(W + 1)]

	for u in range(W + 1):
		T[u][0] = 0

	for i in range(1, len(w) + 1):
		for u in range(W + 1):
			T[u][i] = T[u][i - 1]

			if u >= w[i - 1]:
				T[u][i] = max(
					T[u][i], 
					T[u - w[i - 1]][i - 1] + v[i - 1]
					)

	return T[W][len(w)]
```
* Running time: `O(nW)`
* Space: `O(nW)`

Space can be improved to `O(W)` in the iterative version by
only storing the current column and the previous one.


#### Reconstructing a Solution
We can find an optimal solution by analyzing the 
computed solutions to subproblems.

* Start with `u = W`, `i = n`.
* If `value(u, i) = value(u, i -1)`, then item `i` wasn't taken. 
* Update `i` to `i - 1` and `u` to `u - w[i - 1]`.
```
def knapsack(W, w, v, items, last):
	weight = sum(w[i] for i in items)

	if last == len(w) - 1:
		return (sum(v[i] for i in items))

	value = knapsack(W, w, v, items, last + 1)
	if weight + w[last + 1] <= W:
		items.append(last + 1)
		value = max(value, knapsack(W, w, v, items, last + 1))
		items.pop()

	return value
```

**Important**

If all subproblems must be solved, an iterative algorithm is usually
faster than a recursive one bc no recursive overhead.