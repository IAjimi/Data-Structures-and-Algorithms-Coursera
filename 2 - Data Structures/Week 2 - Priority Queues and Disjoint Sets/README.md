## Data Structures Week 2
### Priority Queues and Disjoint Sets

* [Build Heap](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%203%20-%20Priority%20Queues%20and%20Disjoint%20Sets/build_heap.py) 
* [Job Queue](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%203%20-%20Priority%20Queues%20and%20Disjoint%20Sets/job_queue.py) 

---
## Priority Queues and Disjoint Sets
### Dynamic Arrays
Abstract data type with the following **constant time** operations:
* get(ix)
* set(ix, val)

As well as
* pushback(val)
* remove(ix)
* size()

Implementation:
* `arr`: dynamically allocated array
* capacity: size of `arr`
* size: # of objects currently in array

Suppose we have `arr` of size 0 and capacity 2. 
We push `a` and `b` into `arr` and now want to add a new element.
We create a new `arr` of size 0 and capacity 4, and copy over `a`
and `b` into this new `arr`.

```
def Get(i):

def Set(i, val):
	if i < 0 and i >=

def PushBack(val):
	if size == capacity:
		allocate new_array[2*capacity]

		for i from 0 to size - 1:
			new_arr[i] = arr[i]

		rm arr
		arr = new_array
		capactiy = 2* capacity

def ...

def Size():
	return size
```

Runtime:
* get(i): O(1)
* set(i, val): O(1)
* PushBack(val): O(n)
* Remove(i): O(n)
* Size(): O(1)

In Python, lists are dynamic by default.

### Priority Queues
Queue: 
* PushBack(e): adds an element to the back of the queue
* PopFront(): extracts an element from the front of the queue

A Priority Queue is a **generalization** of a queue where each
element is assigned a priority and elements come out in order by
priority.

#### Scheduling Job
We want to process jobs one by one in order of decreasing priority.
To add a job in the set of scheduled jobs, call `Insert(job)`.
To process a job with the highest priority, get it by calling `ExtractMax()`.

Definition: A Priority Queue is an abstract data type supporting the following main operations:
* Insert(p) adds a new element with priority p
* ExtractMax() extracts an element with maximum priority

Additional Operations:
* Remove(ix): removes element pointed by ix
* GetMax(): returns element w/ max priority
* ChangePriority(ix, p): changes the priority of an element pointed by ix to p.

#### Naive Implementation
Unsorted Array / List:
* Insert(e): Add e at the end, O(1)
* ExtractMax(): Scan array for max, O(n)

Sorted Array:
* Insert(e): find position for e (`O(log n)`), shift all elements to the right of by 1 (`O(n)`),
insert e (`O(1)`) ---> `O(n)`
* ExtractMax(): extract last element, `O(1)`

Sorted List:
(e.g., [2, 3, 9, 10, 16] organized with pointers
to previous/next element, e.g., 3 points to: [2, 9])
* ExtractMax(): extract last element, `O(1)`
* Insert(e): find position for e (`O(n)`)

#### Binary Heaps
Binary max-heap is a **binary tree** (each node has 0, 1, or 2 children)
where the value of each node is **at least** (>=) the values of its children.

Note: previously, we defined the height of a tree as the number of nodes on a longest path from the root 
to a leaf. In this module, we use a slightly different definition of the height: 
we define it to be equal to the **number of edges** on the longest path from the root to a leaf.

Sample Tree:
* 42: [29, 18]
* 29: [14, 7]
* 14: [11]
* 7: []
* 18: [12, 7]

Basic Operations:
* GetMax: return root value, O(1)
* Insert: we can't just add the node anywhere, because a node
can only have 2 children max. We could attach 32 to 7 (still binary tree but max-heap property is violated). To fix this, we swap the 
problematic node with its parent until the property is satisfied.
    * Important: while "SiftUp", the heap property is violated on at most one edge. We move incrementally upwards, which implies that, at most, the running time is O(tree height).
* ExtractMax: we can't just get rid of the root. Instead, swap
the root with an end node, e.g., was 42 with 12. This violates
the heap property. We "SiftDown" (swap the problematic node with the largest child) until the heap property is satisfied. In this case,
we swap 12 with 29, then 12 with 14.
* ChangePriority: change the priority and let the changed element
sift up or down depending on whether its priority decreased or increased, e.g., change 12 to 35.Swap 35 with 18, swap 35 with 18
again.
* Remove: change the priority to inf, let it sift up, then extract
maximum (replace root by some random element, let it sift down). Runtime is at most O(tree height).

GetMax is `O(1)` and all other operations are in time `O(tree height)`.

#### Completeness
A binary tree is **complete** if all its levels are filled except possibly the last one, 
which is filled from left to right.

Advantage:
* Store as array
    * parent(i) = floor(i/2)
    * leftchild(i) = 2i
    * rightchild(i) = 2i + 1

#### Pseudo Code
* H is array containing heap
* MaxSize is the size of the array + the max number of nodes in the heap
size is the actual size of the array

Ex:
```
ix = [1, 2,  3,  4,  5,  6,  7,  8, 9, 10, 11, 12, 13]
H = [42, 29, 18, 14, 7, 18, 12, 11, 5, 30, 29, 2, 8]
MaxSize = 13
size = 9
```
bc size is 9, we ignore all the elements after element 9, 5

This tree is given to us implicitely: for any node, we can
compute the number of its parent and the numbers of its two parents.

```
def Parent(i):
	return math.floor(i / 2)

def LeftChild(i):
	return 2 * i

def RightChild(i):
	return 2 * i + 1

def SiftUp(i):
	while i > 1 and H[Parent(i)] < H[i]:
		swap H[Parent(i)] and H[i]
		i = Parent(i)

def SiftDown(i):
	maxIndex = i
	l = LeftChild(i)

	if l <= size and H[l] > H[maxIndex]:
		maxIndex = l

	r = rightChild(i)
	if r <= size and H[r] > H[maxIndex]:
		maxIndex = r

	if i != maxIndex:
		swap H[i] and H[maxIndex]
		SiftDown(maxIndex)

def Insert(p):
	if size == maxSize:
		return ERROR

	size += 1
	H[size] = p
	SiftUp(size)

def ExtractMax():
	result = H[1]
	H[1] = H[size] # replace by last leaf
	size += - 1
	SiftDown(1)
	return result

def Remove(i):
	H[i] = inf
	SiftUp(i)
	ExtractMax()

def ChangePriority(i, p):
	oldp = H[i]
	H[i] = p
	if p > oldp:
		SiftUp(i)
	else:
		SiftDown(i)
```

#### Heap Sort
Binary heaps can be used to implement the **heap sort** algorithm, a fast and space efficient sorting algorithm.

Instead of scanning a whole array, we use a smart data structure.

```
HeadSort(A[1 ... n]):
	create an empty priority queue
	for i from 1 to n:
		Insert(A[1])
	for i from n to 1:
		A[i] = ExtractMax()
```

The resulting algorithm is comparison-based and has running time `O(n log n)`. 

#### Turn Array into a Heap
```
def BuildHeap(A[1 ... n]):
	size = n
	for i from floor(n/2) to 1:
		SiftDown(i)
```
#### In Place Heap Sort
```
def HeapSort(A[1 ... n]):
	BuildHeap(A)
	repeat (n - 1) times:
		swap A[1] and A[size]
		size += -1
		SiftDown(1)
```
### Disjoint Set
A disjoint-set data structure supports the following operations:
* `MakeSet(x)` creates a singleton set {x}
* `Find(x)` returns ID of the set containing x
* `Union(x, y)` merges two sets containing x and y

#### Naive Implementation
For sets of integers (1, 2, ..., n), we can use the smallest element of a set as its ID.

Use array `smallest[1...n]`: `smallest[i]` stores the smallest element in the set `i` belongs to.

EX:
```
{9,3,2,4,7}
{5}
{6,1,8}

val =      [1, 2, 3, 4, 5, 6, 7, 8, 9]
smallest = [1, 2, 2, 2, 5, 1, 2, 1, 2]


def MakeSet(i):
	smallest[i] = i

def Find(i):
	return smallest[i]
```
Running time: `O(1)`
```
def Union(i, j):
	i_id = Find(i) # id of i's set
	j_id = Find(j)

	if i_id == j_id:
		return

	m = min(i_id, j_id) # new set id, since we id with min
	for k in range(1, n): # update the set id for all elements in set i and j
		if smallest[k] in {i_id, j_id}:
			smallest[k] = m
```

Running time: `O(n)`

The union operations is our bottleneck.

What basic data structure allows for efficient merging? 
* Idea: represent a set as a **linked list**, use the list tail as ID of the set.

EX: we can merge two lists by just updating one pointer.
* `[9, 3, 2, 4, 7]`
* `[6, 1, 8]`
just updated 7 to point to 6

Performance:
* Pros: Union is `O(1)`
* Cons: Find is `O(n)` as we need to traverse the list to find its tail

#### Efficient Implementation
Represent each set as a rooted tree, where the ID of the set is the root of the tree. 

Use array `parent[1 ... n]`: `parent[i]` is the parent of i, or i if it is the root.
```
def MakeSet(i):
	parent[i] = i

def Find(i):
	while i != parent[i]:
		i = parent[i]
	return i
```
Runtime: `O(tree height)`

How do we merge two trees? Hang one of the trees under the root of the other one. 
We would want to hang the shorter tree, since we would like to keep the trees shallow (union by rank heuristic).

To quickly find the height of a tree, we will keep the height of each subtree
in an array `rank[1 ... n]` where `rank[i]` is the height of the subtreet whose root is i.
```
def MakeSet(i):
	parent[i] = i
	rank[i] = 0

def Find(i):
	while i != parent[i]:
		i = parent[i]
	return i

def Union(i,j):
	i_id = Find(i) # id of i's set
	j_id = Find(j)

	if i_id == j_id:
		return

	if rank[i_id] > rank[j_id]:
		parent[j_id] = i_id
	else:
		parent[i_id] = j_id

		if rank[i_id] == rank[j_id]:
			rank[j_id] += 1
```
The height of any tree in the forest is at most `log2(n)`.
Any tree of height k in the forest has at least 2^k nodes.
