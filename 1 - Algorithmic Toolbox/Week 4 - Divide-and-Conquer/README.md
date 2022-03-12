## Algorithmic Toolbox Week 4

* [Binary search](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%204%20-%20Divide-and-Conquer/week4_part1_binary_search.py)
* [Majority element](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%204%20-%20Divide-and-Conquer/week4_part2_majority_element.py)
* [Lottery](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%204%20-%20Divide-and-Conquer/week4_part5_lottery.py) 
* [Number of Inversions](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/1%20-%20Algorithmic%20Toolbox/Week%204%20-%20Divide-and-Conquer/week4_part4_inversions.py)

---

## Divide & Conquer
Break down problem into smaller subproblems of the same type. Since each subproblem is similar to the original problem, divide & conquer algorithms naturally lead to a **recursive** solution.

Topics covered:
* Search
    * Linear Search
    * Binary Search
    
* Polynomial Multiplication
* Sorting
    * Selection Sort
    * Merge Sort
    * Quick Sort
    * Random Pivot

### Linear Search
Searching in an unsorted array using linear search, i.e., go through the array 1 by 1 and check if element you are looking for is there.

```
LinearSearch(A, low, high, key):
	'''
	Basically check 1st element of array between low and high. 
	If not it, perform LS on array without 1st element in prev array.
	'''
	if high < low:
		return NOT_FOUND
	if A[low] = key:
		return low
	return LinearSearch(A, low+1, high, key)
```

Worst-case runtime? `T(n) = T(n-1) + c = n * c` (c is a constant amount of work, for checking high < low and
A[low] = key)

### Binary Search
* Input: A sorted array, `A[low ... high]` and a key `k`.
* Output: An index i where `A[i] = k`. Otherwise, the greatest index i where `A[i] < k`. Otherwise (`k < A[low]`), the result is `low - 1`.

(The list is sorted - so if the 1st element is `> k`, k is not in the list. Similarly, if the last element is `< k`, then k is not in the list - index would be > length.)

Example:
```
A = [3, 5, 8, 20, 20, 50, 60]
search(A, k=2) -> 0
search(A, k=3) -> 1
search(A, k=4) -> 1
search(A, k=20) -> 4 OR 5
search(A, k=60) -> 7
search(A, k=90) -> 7
```

```
BinarySearch(A, low, high, key):
	if high < low: #empty array
		return low - 1

	mid = floor(low + (high-low) / 2)

	if key == A[mid]
		return mid
	elif key < A[mid]:
		return BinarySearch(A, low, mid - 1, key)
	else:
		return BinarySearch(A, mid + 1, high, key)
```

Example:
```
RecursiveBinarySearch(A, 1, 11, 50)
A = [3, 5, 8, 10, 12, 15, 18, 20, 20, 50, 60]
1st mid is 6. 50 > A[6] so BinarySearch(A, 7, 11, 50).
Mid is 9. 50 > A[9] = 20 so BinarySearch(A, 10, 11, 50).
Mid is 10. 50 = A[10] so return 10.
```

Worst-case runtime? `T(n) = T(floor(n/2)) + c -> O(log_2 n)`

```
IterativeBinarySearch(A, low, high, key):
	while low <= high:
		mid = floor(low + (high - low) / 2)

		if key == A[mid]:
			return mid
		elif key < A[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return low - 1
```

### Polynomial Multiplication
* Input: `n = 3`, `A = [3, 2, 5]`, `B = [5, 1, 2]`
* Output: `[15, 13, 33, 9, 10]`

Example:
```
A(x) = 3x**2 + 2x + 5
B(x) = 5x**2 + x + 2
A(x)B(x) = 15x**4 + 13x**3 + 33x**2 + 9x + 10
```

#### Naive Approach
```
MultPoly(A, B, n):
	product = [0 for i in range(2n-1)]

	for i in range(n-1):
		for j in range(n-1):
			product[i+j] = product[i+j] + A[i] * B[j]

	return product
```

Runtime is `O(n**2)`.

#### Naive Divide and Conquer
Let `A(x) = D(x)x**(n/2) + D0(x)`.

Let `B(x) = E(x)x**(n/2) + E0(x)`.

Then, `AB = (Dx**n/2 + D0)(Ex**(n/2) + E0) = (D1E1)x**n + ...`, which yields 4 polynomials of degree n/2.

Example:
```
A = 4x**3 + 3x**2 + 2x + 1
B = x**3 + 2x**2 + 3x + 4

D1 = 4x + 3
D0 = 2x + 1
E1 = x + 2
E0 = 3x + 4

AB = (D1E1) x ** 4 + (D1E0+D0E1) x ** 2 + D0E0
```

Algorithm:
```
Mult2(A, B, a, b):
	R = [0 for 0 in range(2n-1)]

	if n == 1:
		R[0] = A[a] * B[b]
		return R
	else:
		R[:n-2] = Mult2(A, B, n/2, a, b)
		R[n:2n-2] = Mult2(A, B, n/2, a + n/2, b + n/2)

		D0E1 = Mult2(A, B, n/2, a, b + n/2)
		D1E0 = Mult2(A, B, n/2, a + n/2, b)

		R[n/2:n+n/2-2] += D1E0 + D0E1

		return R
```

Some math leads to the conclusion that the runtime that this is O(n**1.58).

#### Master Theorem
Formula:
If `T(n) = aT(floor(n/b)) + O(n**d)` for `a > 0`, `b > 1`, `d >= 0`
then
* if `d > log_b(a)` then `O(n**d)`
* if `d = log_b(a)` then `O(n**d log(n))`
* if `d < log_b(a)` then `O(n**log_b(a))`

EX: `T(n) = 4 T(n/2) + O(n)`, `a = 4`, `b = 2`, `d = 1`.
Since `d < log_b(a)`, `T(n) = O(log_b(a)) = O(n**2)`.

.... [missing notes]

### Sorting
* Input: `A[1, ..., n]`
* Output: `A[1, ..., n]` in non-decreasing order

#### Selection Sort
Initial array: `[8, 4, 2, 5, 2]`
* Step 1: find minimum (2), swap with 1st element -> `[2, 4, 8, 5, 2]`
* Step 2: repeat with remaining part of array `[4, 8, 5, 2]` -> `[2, 2, 8, 5, 4]`
* Repeat until no elements left to sort

Algorithm:
```
SelectionSort(A):
	for i in range(1, n):
		minIndex = i

		for j from i + 1 to n:
			if A[j] < A[minIndex]:
				minIndex = j

		A[minIndex] = min(A[i:])
		A[i], A[minIndex] =  A[minIndex], A[i]
```

Run time: `O(n**2)`.

#### Merge Sort
Initial array: `[7, 2, 5, 3, 7, 13, 1, 6]`
* Step 1: Split into two halves -> `[7, 2, 5, 3], [7, 13, 1, 6]`
* Step 2: Sort the halves recursively -> `[2, 3, 5, 7], [1, 6, 7, 13]`
* Step 3: take the minimum of both halves, put in result array -> `[1]`, `[2, 3, 5, 7], [6, 7, 13]`
* Step 4: repeat

```
MergeSort(A):
	n = len(A)

	if n == 1:
		return A

	m = floor(n / 2)
	B = MergeSort(A[:m])
	C = MergeSort(A[m+1:])
	A = Merge(B, C)

	return A

Merge(B, C):
	''' B and C are sorted. B is of length p, C is of length q.'''

	n = 0 # position counter
	D = [0 for r in range(p+q)]

	while B and C:
		b = B[0]
		c = C[0]

		if b <= c:
			D[n] = b
			B.pop(0)
		else:
			D[n] = c
			C.pop(0)

		n += 1

	# move the rest of B and C to the end of D

	return D
```

Runtime of Merge is `p + q`.
Runtime of MergeSort is `O(n log n)`.

#### Lower Bound for Comparison-Based Sorting Algorithm
A comparison based sorting algorithm sorts objects by comparing paris of them. 

The selection sort and merge sort algorithms are comparison based.

Any comparison based sorting algorithm performs `O(n log n)` comparisons in the **worst** case to sort n objects.

There are `n` factorial "leaves" in the tree, for every permutation of 2 elements. 

The maximum number of comparisons is at least the depth d.

`d >= log_2(l)` so `log_2(n!) = O(n log n)`.

#### Non Comparison-Based Sorting Algorithms
Example: Counting Sort Algorithm
For `A = [2, 3, 2, 1, 3, 2, 2, 3, 2, 2, 1]`, count appearances of each object: `{1:2, 2:7, 3:3}`.
Then, the sorted array is `[1, 1, 2, 2, 2, ..., 3, 3, 3]`.

For arrays of small integers.

#### Quick Sort
* `A = [6, 4, 8, 2, 9, 3, 9, 4, 7, 6, 1]`
* Step 1: pick the first element in the array. Move it to its final position by moving all 
elements <= A[0] to the left of A[0] and > A[0] to the right of A[0]. -> `A = [1, 4, 2, 3, 4, 6, 6, 9, 7, 8, 9]`
* Step 2: sort the two parts recursively.

```
QuickSort(A, l, r):
	if l >= r:
		return
	m = Partition(A, l, r)
	# A[m] is in final position
	QuickSort(A, l, m - 1)
	QuickSort(A, m + 1, r)
```

#### Partitioning
A pivot is `x = A[l]`.

Move `i` from `l + 1` to `r` maintaining the following invariant:
* `A[k] <= x` for all `l + 1 <= k <= j`
* `A[k] > x` for all `j + 1 <= k <= i`

Example where x = 6:

`[6, 4, 2, 3, 9, 8, 9, 4, 7, 6, 1]`

`[0, r, r, j, b, i, 0, 0, 0, 0, 0]`

Increment `i + 1`, the new element is `9 > 6` so extend blue region:

`[0, r, r, j, b, b, i, 0, 0, 0, 0]`

Increment again, the new element is 4, swap the 1st element in the blue region with 4:

`[6, 4, 2, 3, 4, 8, 9, 9, 7, 6, 1]`

`[0, r, r, r, j, b, b, b, i, 0, 0]`

etc until

`[6, 4, 2, 3, 4, 6, 1, 9, 7, 8, 9]`

`[0, r, r, r, r, r, j, b, b, b, i]`

Swap 6 with last element of red region, 1.

This gives us the final (sorted) array,	`[1, 4, 2, 3, 4, 6, 6, 9, 7, 8, 9]`.

Algorithm:
```
Partition(A, l, r):
	x = A[l] # pivot
	j = l

	for i in range(l + 1, r): # check new element
		if A[i] <= x: # if <= x, move to left region
			j += 1
			swap A[j] and A[i]
		# A[l + 1 ... j] <= x, A[j + 1 ... i] > x

	swap A[l] and A[j]
	return j
```

#### Random Pivot
Worst-case: `T(n) = n + T(n - 1) = n + (n - 1) + (n - 2) + ... = O(n**2)`.

What if we partitioned s.t. that one side is size 5 and the other is size 4?
`T(n) = n + T(n - 5) + T(4) >= n + (n - 5) + (n - 10) + ... = O(n**2)`

What if we partitioned into 2 arrays of equal size?
`T(n) = 2 T(n / 2) + n = O(n log(n))`

So we want a way to select a pivot element so that it always guarantees a 
balanced partition. 

How to do this isn't clear: instead, pick a random pivot.

Why random? half of the elements of A guarantee a balanced partition.

```
RandomizedQuickSort(A, l, r):
	if l >= r: # size?
		return
	k = random number between l and r
	swap A[l] and A[k]
	m = Partition(A, l, r)
	# A[m] is in final position
	QuickSort(A, l, m - 1)
	QuickSort(A, m + 1, r)
```

Assume that all elements of A[1 ... n] are pairwise different. Then the average
running time of RandomizedQuickSort(A) is `O(n log(n))` while the worst running
time is `O(n**2)`.