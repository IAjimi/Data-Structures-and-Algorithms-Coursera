from collections import deque
from typing import List


def remove_smaller(d: List[int], n: int) -> List[int]:
    """
    Remove all elements smaller than n from d.
    d is by design sorted in decreasing order, so iterating
    from right to left.
    """
    while d and d[-1] < n:
        d.pop()
    return d if d else deque([])


def shrink_window(d: List[int], n: int) -> List[int]:
    """Remove value n from d."""
    if n in d:
        d.remove(n)
    return d

def max_sliding_window(sequence: List[int], m: int) -> List[int]:
    """Return the maximum element for every subsequence of size m of sequence."""
    d = deque([])
    maximums = []

    for i, n in enumerate(sequence):
        d = remove_smaller(d, n)
        d.append(n)

        if i >= m - 1:
            d = shrink_window(d, sequence[i - m])
            maximums.append(d[0])

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

