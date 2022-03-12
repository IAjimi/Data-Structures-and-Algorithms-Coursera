## Data Structures Week 4
### Binary Search Trees

* [Binary Tree Traversal](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%204%20-%20Binary%20Search%20Trees%201/binary_tree_traversal.py) 
* [Check Binary Search Tree](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%204%20-%20Binary%20Search%20Trees%201/check_binary_search_tree.py)

---
## Binary Search Trees
### Local Search Data Structure
A LSD stores a number of elements each with a key coming
from an ordered set. It supports operations:
* RangeSearch(x,y): returns all elements with keys between x and y
* NearestNeighbors(z): returns the element with keys on either side of z.

We need to be able to modify the data structure as we go:
* insert(x)
* delete(x)

#### Sorted Array
* RangeSearch O(log(n))
* Nearest Neighbors O(log(n))
* insert O(n)
* delete O(n)

### Binary Search Tree
Instead of searching an array, search a tree.

We can find a value by picking the right branch. It is also easier to insert into than a sorted array.

Parts of a tree:
* root node
* left node: smallest child
* right child: largest child

X's key is larger than the key of any descendants of its left child
and smaller than the key of any descendant of its right child.
* i.e., consistently smaller stuff on the left, consistently larger on the right.

#### Find Operation
* input: key k, root r
* output: the node in the tree of r with key k

What if the key is not in the tree?
We've figured out where the key *should* be.

```
def find(k, r):
	if r.key == k:
		return r
	elif r.key > k:
		if r.left:
			return find(k, r.left)
		else:
			return r  # where key should be
	elif r.key < k:
		if r.right:
			return find(k, r.right)
		else:
			return r
```
#### Adjacent Elements
* Input: node N
* Output: the node in the tree with the next largest key

If N has a right child, go right (will be bigger than N) then
left until hit null (hit left because slightly smaller than the node
that was bigger than N)

If N has no right child, go left then right until find something > N.
```
def next(N):
	if N.right:
		return left_descendant(N.right)
	else:
		return right_ancestor(N.left)

def left_descendant(N):
	if not N.left:
		return N
	else:
		return left_descendant(N.left)

def right_ancestor(N):
	if N.key < N.parent.key:
		return N.parent
	else:
		return right_ancestor(N.parent)
```
#### Range Search
* input: number x,y and root r
* output: a list of nodes with keys between x and y

Ex:
RangeSearch(5, 12) - search for 5, 6, ... until exceed range
```
def range_search(min_range, max_range, R):
	result = []
	N = find(min_range, R)

	while N.key <= max_range:
		if N.key >= min_range:
			result.append(N)

		N = next(N)

	return result
```
#### Insert
* input: key k and root r
* output: add key k to tree
```
def insert(k, r):
	p = find(k, r)  # will tell us where new node should be!
	# add new node with key k as child of p
```
#### Delete
* input: node n
* output

find the node that's closest to the thing you're deleted

```
def delete(N):
	if not N.right:
		# remove N, promote N.left
	else:
		x = next(n)
		x.left = None
		# replace N by x, promote x.right
```
#### Balance
Find is `O(depth)` so we want left and right subtrees to have approx the same size.

If the tree is **perfectly balanced**:
* each subtree is half the size of its parent
* after `log_2(n)` levels, subtree of size 1
* operations run in `O(log(n))` time

Problem: insertions and deletions can destroy balance!

We need to **rebalance**: rearrange tree to maintain balance.

Rotations:
`[x, y, c, a, b]` where `a < y < b < x < c`
can be changed into
`[y, a, x, b, c]`.
```
def rotate_right(x):
	p = x.parent
	y = x.left
	b = y.right

	y.parent = p
	p.appropriate_Child = y
	x.parent, y.right = y, x
	b.parent, x.left = x, b
```
### AVL Trees
The height of a node is the maximum depth of its subtree.

Calculating height recursively:
* `N.height` is 1 if N is a leaf
* `1 + max(N.left.height, n.right.height)` otherwise

Height is a rough measure of subtree size.

AVL trees have the following property:
for all nodes N, `abs(n.left.height - n.right.height) <= 1`- i.e., 
the difference in length of left and right child should be at most one.

AVL property: 
* `height = O(log(n))`

Proof:
	if `h = 1`, have one node
	otherwise have on subtree of height `h - 1` and another of height at least `h - 2`
	by inductive hypothesis, total number of nodes is at least `F_h = F_h-1 + F_h-2`

We need a new insertion algorithm that rebalances the tree to maintain the AVL property
```
def avl_insert(k, r):
	insert(k, r)
	N = find(k, r)
	rebalance(N)
```
If `abs(n.left.height - n.right.height) <= 1`, all is fine
```
def rebalance(N):
	p = n.parent

	if n.left.height > n.right.height + 1:
		rebalance_right(n)
	elif n.right.height > n.left.height + 1:
		rebalance_left(n)
	
	adjust_height(n)

	if not p:
		rebalance(p)

def adjust_height(n):
	n.height = 1 + max(n.left.height, n.right.height)
```
Basic idea: if subtree is too heavy, rotate to the right.
```
def rebalance_right(N):
	M = N.left

	if M.right.height > M.left.height:
		rotate_left(M)

	rotate_right(N)

	# adjust height on affected nodes
```
Deletions can also change balance
```
def avl_delete(N):
	delete(N)
	M = parent of node replacing N
	rebalance(M)
```
### Merge
In general, merging 2 sorted lists take `O(n)`.
when they are separated it is faster

* input: roots r1 and r2 of trees with all keys in r1's tree
smaller than those in r2's
* output: the root of a new tree with all the elements of both trees

Easy if extra root: we have extra node to add as root, put small
tree to the left, larger tree to the right.
```
def merge_with_root(r1, r2, T):
	T.left = r1
	T.right = r2
	r1.parent = T
	r2.parent = T
	return T
```
If not, we can get a new root by removing the largest element of the left
subtree.
```
def merge(r1, r2):
	T = find(inf, r1)
	delete(T)
	merge_with_root(r1, r2, T)
	return T
```
Problem? this doesn't preserve balance properties.
Solution? Go down side of tree until merge with subtree of 
same height.
```
def avl_tree_merge_with_root():
	... 
	-- kind of gave up on notetaking here
```
Problem? 
We might want to find the 7th largest element, or the median element.

Order Statistics:
* input: the root of a tree T and a number k
* output: the kth smallest element in T

We need to know which subtree to look in and how many elements are in the left
subtree.
