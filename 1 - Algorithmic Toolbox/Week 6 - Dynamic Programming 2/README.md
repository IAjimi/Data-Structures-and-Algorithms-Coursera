# Algorithmic Toolbox Week 6

* [Knapsack without repetitions](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%206%20-%20Dynamic%20Programming%202/week6_part1_knapsack.py)
* [Maximizing the value of an arithmetic expression by adding parenthesis](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%206%20-%20Dynamic%20Programming%202/week6_part3_max_parenthesis.py)

---

## Dynamic Programming
### Placing Parenthesis
Consider `1 + 2 - 3 * 4 - 5`. How do we place 
parentheses in an expression to maximize its value?

* Input: a sequence of digits and a sequence of operations
* Output: an order of applying those operations that max. the expression

Assume that the last operation in an optimal parenthesizing
of `5 -8 + 7 * 4 - 8 + 9` is *: `(5 - 8 + 7) * (4 - 8 + 9)`.

It would help to know the min and max values of the subexpressions
`5 - 8 + 7` and `4 - 8 + 9`.

* `min(5 - 8 + 7) = -10`
* `max(5 - 8 + 7) = 4`
* `min(4 - 8 + 9) = -13`
* `max(4 - 8 + 9) = 5`

maximizing the final value of the expression can be achieved here
by taking both max = `-10 * -13 = 130`.

#### Algorithm
Pseudocode:
```
	_min = inf
	_max = -inf

	for k from i to j - 1: # all possible splits
		a = M(i, k) opk M(k + 1, k)
		b = M(i, k) opk m(k + 1, k)
		c = m(i, k) opk M(k + 1, k)
		d = m(i, k) opk m(k + 1, k)

		_min = min(_min, a, b, c, d)
		_max = max(_max, a, b, c, d)

	return _min, _max
```
When computing `M(i, j)` the values of `M(i, k)` and `M(k + 1, j)`
should be already computed.

Solve all subproblems in order of increasing length, i.e., (j - i).

Example:
* Start with (1, 1), (2, 2), etc.
* Move to (2, 1), (3, 2), etc.
* Move to (3, 1), (4, 2), etc.
```
def Parentheses(d1 op1 d2 op2 ... dn):
	for i in range(1, n): # initialize min max values
		m[i, i] = di
		M[i, i] = di

	for s in range(1, n - 1):
		for i in range(1, n - s):
			j = i + s
			m[i, j], M[i, j] = MinAndMax(i, j)

	return M(1, n) # max of initial expression
```
Run-time is `O(n**3)`.

#### Example
Expression: `5 - 8 + 7 * 4 - 8 + 9`

Min matrix:
```
5 -3 -10 -55 -63 -94
   8  15  36 -60 -195
       7  28 -28 -91
           4  -4 -13
                 ...
```

* diagonal has the numbers `5, 8, 7, 4, 8, 9`
* diagonal above that has `(5 - 8), (8 + 7), (7 * 4)`, etc
