import sys

def optimal_sequence(num):
    coins = [1, 2, 3]
    ops = [m for m in range(num + 1)] # most operations that could be used
    chain = {}
    
    for m in range(1, num + 1):
        for c in coins:
            if c == 1:
                numOps = ops[m - 1] + 1
                resid = 0
            elif c == 2:
                numOps = ops[m // 2] + 1
                resid = m % 2
            elif c == 3:
                numOps = ops[m // 3] + 1
                resid = m % 3
            else:
                return 0

            if (c <= m) and (resid == 0): # if within bounds
                if (numOps <= ops[m]): # and improves on current option
                    ops[m] = numOps # is optimal choice
                    if c == 1: chain[m] = m - 1
                    elif c == 2: chain[m] = m // 2
                    elif c == 3: chain[m] = m // 3

    # Get Steps from Chain
    steps = unravelChain(num, chain)

    return steps


def unravelChain(num, chain):
    steps = []
    _next = num

    while _next in chain.keys():
        steps.append(_next)
        _next = chain[_next] # get operation that was just used

    steps.reverse()

    return steps

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
