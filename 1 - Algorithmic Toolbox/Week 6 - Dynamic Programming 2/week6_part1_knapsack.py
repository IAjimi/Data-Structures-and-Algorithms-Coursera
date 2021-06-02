import sys

def knapsack(W, w, v):
    T = [[None] * (len(w) + 1) for _ in range(W + 1)] # empty list for every capacity

    for u in range(W + 1): # initialized with 0 in 1st val
        T[u][0] = 0

    for i in range(1, len(w) + 1): # for every item
        for u in range(W + 1): # for every capacity
            T[u][i] = T[u][i - 1] # current val = value of previous item (either taken or not)

            if u >= w[i - 1]: # if current capacity allows
                T[u][i] = max( # either stay as is
                    T[u][i], 
                    T[u - w[i - 1]][i - 1] + v[i - 1] # or add object
                    )

    return T[W][len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(knapsack(W, w, w)) # here, value = weights
