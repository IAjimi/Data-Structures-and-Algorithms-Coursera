## Algorithms on Strings Week 1
### Suffix Trees

* [Trie](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/4%20-%20Algorithms%20on%20Strings/1%20-%20Suffix%20Trees/trie.py)
* [Trie Matching](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/4%20-%20Algorithms%20on%20Strings/1%20-%20Suffix%20Trees/trie_matching.py)
* [Trie Matching Extended](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/4%20-%20Algorithms%20on%20Strings/1%20-%20Suffix%20Trees/trie_matching_extended.py)
* Suffix Tree

---
## Tries & Suffix Trees
### Brute Force Approach
* single pattern: `O(len(text) * len(pattern))`
* multiple patterns: `O(len(text) * len(patternS))`

### Trie
Idea: represent the pattern as a path in a tree

Trie Matching: drive `Trie(patterns)` along text at each position of text.

Runtime: `O(len(text) * len(longest pattern))`
```
def trie_construction(patterns):
	Trie = graph with single node root

	for pattern in patterns:
		current_node = root

		for i in range(len(pattern)):
			symbol = pattern[i]

			if edge from current_node to symbol:
				current_node = end node of this edge 
			else:
				# add new node new_node to Trie
				# add new edge from current_node to new_node with label symbol
				current_node = new_node

	return Trie

def prefix_trie_matching(text, trie):
	symbol = text[0]
	v = trie root

	while True:
		if v is a leaf in Trie:
			return pattern spelled from root to v
		elif there is an edge (v, w) labeled by symbol:
			symbol = next letter of Text
			v = w
		else:
			print("no match")
			return

def trie_matching(text, trie):
	while text:
		prefix_trie_matching(text, trie)
		text = text[1:]
```
### Suffix Tree
Trie can be impractical memory-wise:

* generate all suffixes of text
* form a trie out of these suffixes (suffix trie)
	* add position of suffix to the leaves
* for each pattern, check if it can be spelled from the root downward in suffix trie
	* walk down to leaf to find position of pattern

Memory: `len(text) * (len(text) - 1) / 2`

Solution?
* instead of having each node be a letter, have the full string
    * ex: instead of `b -> a -> n -> a -> n -> a -> s`, store "bananas"
* then, since each suffix adds one leaf, `# vertices < 2 * len(text)`
  
New memory footprint: `O(len(text))`

We can do better: instead of storing the full string ("bananas"), store starting
position and length -> `"bananas" = (6, 8)`

