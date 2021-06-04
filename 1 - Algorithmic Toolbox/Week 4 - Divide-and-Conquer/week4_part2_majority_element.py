import sys

def get_majority_element(n, a):
    a.sort()

    _count = 1
    search_count = n / 2

    for i in range(n - 1):
        if a[i] == a[i + 1]:
            _count += 1
        else:
            _count = 1
        
        if _count > search_count:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(n, a))
