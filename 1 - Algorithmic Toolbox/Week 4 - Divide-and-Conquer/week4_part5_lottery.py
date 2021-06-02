import sys
from operator import itemgetter

def count_segments(starts, ends, points):
    cnt = [0] * len(points)
    segments = [*zip(starts, ends)]
    segments = sorted(segments,key=itemgetter(1))

    for i in range(len(points)):
        n = 0
        for s in segments:
            if s[0] <= points[i] <= s[1]:
                cnt[i] += 1
            elif points[i] < s[1]:
                break

    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    cnt = count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
