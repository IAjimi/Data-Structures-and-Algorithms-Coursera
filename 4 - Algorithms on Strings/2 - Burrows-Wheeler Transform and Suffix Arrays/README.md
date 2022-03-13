## Algorithms on Strings Week 2
### Burrows-Wheeler Transform


---

## Burrows-Wheeler Transform
Text compression by run-length encoding: compressing a run of n identical symbols
("AAAAAA" into "6A").

Idea:
* convert repeats to runs
* run-length notation
* have compressed text


1. Get all cyclic rotations of string
2. Store them (with $ sign as first)
3. Now look at the last column (`"smnpbnnaaaaa$a"`) (Burrows-Wheeler Transform)

### Inverting Burrows-Wheeler Transform
Let's try reconstructing `banana` from its Burrows-Wheeler transform, `"annb$aa"`.
We know the 1st column of the transform, `"$aaabnn"`.

If we sort the 2-mer composition of `"banana$"` - sorting it gives us the first 2 columns of the matrix, `["$aaabnn", "b$nnaaa"]`.

We can repeat this for the first matrix - the first row gives us "`$banana`",

### First-Last Property
Problem: more memory issues!

Observation: the ith observation of the first column represents the same letter as the ith observation of the last column.

Start by first observation of first column. It maps to s1 in the last column.
We move to the row where s1 can be found in the first column. a6 is found in the
same row of the last column. We look for the row that holds a6 in the first column.
That row has n3 in the last column.
By now we have "san" (which we will reverse - the last 3 letters of "panamabananas").

We repeat until we find $ in last column.

Performance:
* Memory: `2 * len(text)`
* Time: `O(len(text))`

### Using BWT for Pattern Matching
Searching for ana in panamabananas: 6 rows starting with letter a but only 3 end in n.
With first-last property, we can find where these n map into the 1st column. Then we
look for a in the last column, and match that to As in the first column.

We use 2 pointers: top and bottom. We start with top = 0 and bottom = length(str).
Then top = 1st occurence of symbol in 1st column, bottom = last occurence ...
Then top = 1st occurence of next symbol in last column, bottom = last occurence ...
1st last tells us where this maps to in the 1st column, repeat.
```
def BWMatching(firstcol, lastcol, pattern):
	top = 0
	bottom = len(lastcol) - 1

	while top <= bottom:
		if pattern:
			symbol = pattern[-1]
			pattern = pattern[:-1] # remove last letter

			if positions from top to bottom in lastcolumn contain symbol:
				topIndex = 1st position of symbol between top and bottom in lastcol
				bottomIndex = last ...
				top = lasttofirst(topIndex)
				bottom = lasttofirst(bottomIndex)
			else:
				return 0
		else:
			return bottom - top + 1
```