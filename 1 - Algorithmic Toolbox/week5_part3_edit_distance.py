import sys

def edit_distance(A, B):
    n, m = len(A) + 1, len(B) + 1

    D = {}
    for i in range(n): D[(i, 0)] = i
    for j in range(m): D[(0, j)] = j

    for j in range(1, m):
    	for i in range(1, n):
    		insertion = D[(i, j - 1)] + 1
    		deletion = D[(i - 1, j)] + 1
    		match = D[(i - 1, j - 1)]
    		mismatch = D[(i - 1, j - 1)] + 1

    		if A[i - 1] == B[j - 1]:
    			D[(i, j)] = min(insertion, deletion, match)
    		else:
    			D[(i, j)] = min(insertion, deletion, mismatch)

    return D[(n - 1, m - 1)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
