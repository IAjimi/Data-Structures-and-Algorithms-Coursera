import sys
from math import floor

def MergeSort(A, _count = 0):
    n = len(A)

    if n == 1:
        return A, _count

    m = floor(n / 2)
    B, _count = MergeSort(A[:m], _count)
    C, _count = MergeSort(A[m:], _count)
    A, _count = Merge(B, C, _count)

    return A, _count

def Merge(B, C, _count = 0):
    ''' B and C are sorted.'''
    D = []

    while B and C:
        b = B[0]
        c = C[0]

        if b <= c:
            D.append(b)
            B.pop(0)
        else:
            _count += len(B) # since sorted
            D.append(c)
            C.pop(0)

    if B: D += B
    if C: D += C

    return D, _count

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(MergeSort(a)[1])
