import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    # Get starts & ends of segments (easier to sort)
    start = [s[0] for s in segments]
    end = [s[1] for s in segments]

    # Sort start, end so that element w leftmost start is at beg of array
    sorted_idx = sorted(range(len(start)), key = lambda x:start[x])
    end = [end[i] for i in sorted_idx]
    start.sort()

    # Iterate
    points = [end[0]]

    for i in range(len(start)):
        if points[-1] < start[i] or points[-1] > end[i]: # point outside segment
            if end[i] < points[-1]: # implies this new end[i] would be shared by both segments
                points[-1] = end[i]
            else:
                points.append(end[i])

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
