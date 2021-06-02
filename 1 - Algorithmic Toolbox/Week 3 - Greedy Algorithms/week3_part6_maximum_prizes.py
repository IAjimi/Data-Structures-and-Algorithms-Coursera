import sys

def optimal_summands(n):
    _sum = 0
    numbers = []

    if n == 1: 
        numbers.append(1)

    for i in range(1, n):
        if _sum + i + (i + 1) > n:
            numbers.append(n - _sum)
            return numbers
        else:
            _sum += i
            numbers.append(i)

    return numbers

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
