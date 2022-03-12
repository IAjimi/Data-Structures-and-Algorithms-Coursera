## Data Structures Week 1
### Basic Data Structures

* [Check brackets](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%201%20-%20Basic%20Data%20Structures/week1_part1_check_brackets.py) 
* [Process packages](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%201%20-%20Basic%20Data%20Structures/week1_part3_process_packages.py) 
* [Stack with max](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%201%20-%20Basic%20Data%20Structures/week1_part4_stack_with_max.py) 

---
## Basic Data Structures
### Arrays
Contiguous array of memory consisting of equal-size elements indexed by contiguous integers.

What's special about arrays? **constant-time access**.

### Linked Lists
#### Singly-linked list
Each node contains key + next pointer.

* pushFront(Key): add to front
* Key TopFront(): return front item
* PopFront(): remove front item
* PushBack(Key): add to back
* Key TopBack(): return back item
* PopBack(): remove back item
* Boolean Find(Key): is key in list?
* Erase(Key): remove key from list
* Boolean Empty(): empty lst?
* AddBefore(Node, Key): adds key before node
* AddAfter(Node, Key): adds key after node

PopBack is O(n) -> need to fetch element before last
```
def PushFront(Key):
	node = new_node
	node.key = head
	head = node
	if tail == nil:
		tail = head

def PopFront():
	if head == nil:
		return error
	head = head.next

	if head == nil:
		tail = nil

def PushBack(key):
	node = new_node
	node.key = key
	node.next = nil

	if tail == nil:
		head = tail = node
	else:
		tail.next = node
		tail = node

def PopBack():
	if head == nil:
		return ERROR
	if head == tail:
		head = tail = nil
	else:
		p = head

		while p.next.next != nil:
			p = p.next
		
		p.next = nil
		tail = p

def AddAfter(node, key):
	node2 = new_node
	node2.key = key
	node2.next = node.next
	node.next = node2

	if tail == node:
		tail = node2
```
#### Doubly-Linked List
There is a way to make popping the back and adding before cheap, which is adding an extra point 
that allows us to go forward and backward.

Node contains: key, next pointer, prev pointer.
```
def PushBack(key):
	node = new_node
	node.key = key
	node.next = nil

	if tail == nil:
		head = tail = node
		node.prev = nil
	else:
		tail.next = node
		node.prev = tail
		tail = node

def PopBack():
	if head == nil:
		return ERROR
	if head == tail:
		head = tail = nil
	else:
		tail = tail.prev
		tail.next = nil

def AddAfter(node, key):
	node2 = new_node
	node2.key = key
	node2.next = node.next
	node2.prev = node
	node.next = node2

	if node2.next != nil:
		node2.next.prev = node2

	if tail == node:
		tail = node2
```

Constant time to insert at or remove from the front.

With tail and doubly-linked, constant time to insert at or remove from the back. Also constant time to
insert between nodes or remove a node.

`O(n)` time to find arbitrary element.

### Stacks
#### Balanced Brackets
* Input: a string with `()`, `[]`
* Output: whether they are balanced or not
```
stack = Stack()

for char in str:
	if char in ["(", "["]:
		stack.push(char)
	else:
		if stack.empty(): return False
		top = stack.pop()
		if (top == '[' and char != ']') or (top == '(' and char != ')'):
			return False
	return stack.empty()
```
Can implement with list or linked list.

Each stack operation is `O(1)`: push, pop, top, empty.

### Queue
* Enqueue(key): adds key to collection
* Dequeue(): removes and returns least recently added key
-> stack returns MOST recently added key

Implement with linked list.
Enqueue at the back of the linked list.

### Trees
Node contains: key, children, parent (optional)

#### Traversing a tree
Depth-first (recursive):
```
InOrderTraversal(tree):
	if tree == null:
		return
	InOrderTraversal(tree.left)
	print(tree.key)
	InOrderTraversal(tree.right)

PreOrderTraversal(tree):
	if tree == null:
		return
	print(tree.key)
	PreOrderTraversal(tree.left)
	PreOrderTraversal(tree.right)

PostOrderTraversal(tree):
	if tree == null:
		return
	PostOrderTraversal(tree.left)
	PostOrderTraversal(tree.right)
	print(tree.key)
```

Breadth-first:
```
LevelTraversal(tree):
	if tree.isnull(): return

	q = Queue()
	q.enqueue(tree)

	while not q.empty():
		node = q.dequeue()
		print(node)

		if node.left.notnull():
			q.enqueue(node.left)

		if node.right.notnull():
			q.enqueue(node.right)
```