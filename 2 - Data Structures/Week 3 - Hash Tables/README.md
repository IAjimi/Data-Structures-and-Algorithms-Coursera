## Data Structures Week 3
### Hash Tables

* [Phone Book](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%203%20-%20Hash%20Tables/phone_book.py) 
* [Hashing with Chains](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%203%20-%20Hash%20Tables/hashing_with_chains.py) 
* [Find Pattern in Text](https://github.com/IAjimi/Data-Structures-and-Algorithms-Coursera/blob/master/2%20-%20Data%20Structures/Week%203%20-%20Hash%20Tables/find_pattern_in_text.py) 

---

## Hash Tables
Hash tables allow us to search for elements in `O(1)` time.

### Hash Function
For any set of objects `S` and any integer `m > 0`, a function `h:S -> {0, 1, ..., m-1}` is called a hash function.
`m` is the cardinality of `h`.

A good hash function is:
* deterministic
* fast to compute
* different values for different objects (ideally)
* direct addressing with O(m) memory (ideally)

Although we want a small cardinality m, it is impossible to have all different values if `m < len(S)`.

One solution is to use **chaining**:
* select a hash function h with cardinality m
* create an array of size m
* store chains in each cell of the array

Essentially, we store different elements with the same hash value into an array located at `hash_table[__hash(P)]`.

Instead of requiring our hash table to have different values for different objects,
we can look for a hash table that distribute keys well into different cells.

### Universal Family
Let U be the universe - the set of all possible keys.

A set of hash functions H is a **universal family** if, for any
two keys `x,y` belonging to U, `x != y`, the probability of collision
`P[h(x) = h(y)] <= 1 / m`.

If h is chosen randomly from a universal family, the average
length of the longest chain c is `O(1 + a)`, where `a = n / m` (the number of 
keys stored in the hash table divided by the number of values in hash table).

If h is from a universal family, operations with hash table run on average `O(1 + a)`.

If the load factor is between 0.5 and 1, then we only need `O(n)` memory to store n keys and operations run in `O(1)` on average.

If n is unknown in advance, we can adjust the size of the hash table:
* resize the hash table when a becomes too large
* choose new hash function and rehash all objects

Rehash should be called after *each* operation with the hash table.

Rehashing is an O(n) operation but its amortized running time is O(1) as rehashing is rare (time between rehashes 2x every time).

### Hashing Integers
Take numbers up to length 7 (0 to 9,999,999).
* Convert phone numbers to integers: 148-25-67 = 1,482,567
* Choose prime number bigger than 10**7, e.g., p = 10,000,019
* Choose hash table size, e.g., m = 1,000

The following family is a universal family: `((a*x + b) % p) % m`, where x is the number you want to hash, must be < p and 
`1 <= a <= p - 1` and `0 <= b <= p - 1`.

There are p - 1 variants for a and p variants for b -> p(p - 1)

a and b are picked *randomly*.

### Hashing strings
Denote by `|S|` the length of string S. The hash value of S is then `h(S) = S[0]*S[1]*...*S[|S| - 1]`.

We need
* a way to convert S to integer code (ascii, unicode, etc)
* a big prime number p

Then we can use the following family of hash functions: `sum([(s[i] * x**i) for i in range(len(s))]) % p`, where 
`1 <= x <= p - 1`.

Problem? The cardinality is of size p.
Fix? Follow polyhash by integer hash.

#### Search Pattern in Text
Given a text T and a pattern P, find all occurrences of P in T.

Denote by `S[i .. j]` the substring of string S starting in position i
and ending in position j.

Given T and P, we want all positions i in T s.t. `T[i ... i + len(P) - 1] = P`.

**Naive Algorithm**: for each position i from `0` to `|T| - |P|`, check character-by-character
whether `T[i ... i + len(P) - 1] = P`. If so, append i to the result.

The running time of FindPatternNaive is `O(len(T)*len(P))`: if `T = 'aaaaa'` and 
`P = 'aaaab'`, every call to AreEqual has to make all len(P) comparisons.

****Rabin-Karp's Algorithm****: use hashing to quickly compare P to substrings of T.
* If `h(P) != h(S)`, then P != S.
* Elif `h(P) == h(S)`, call are_equal(P, S).

If `P != S`, the probability that `P[h(P) == h(S)]` is at most `len(P) / p`.

To speed up Rabin-Karp, we use a computational trick that will reduce the amount of time spent
generating hashes: **Hash Recurrence**.

We can show that:
`H[i] = x*H[i+1] + T[i] - (T[i + len(P)]*x**len(P)) % p`

Then, we can compute polyhash for *last* substring and use it to compute hashes for subsequent substrings, one at a time.