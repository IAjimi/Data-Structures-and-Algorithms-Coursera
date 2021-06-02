import sys
from math import floor

def binary_search(A, low, high, key):
    mid = floor(low + (high - low) / 2)

    if high < low or mid < low or mid >= len(A):
        return - 1
    elif key == A[mid]:
        return mid
    elif key < A[mid]:
        return binary_search(a, low, mid - 1, key)
    else:
        return binary_search(a, mid + 1, high, key)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, 0, len(a), x), end = ' ')
