import sys

def get_fibonacci_last_digit(n):
    ''' Faster than my initial solution that used a list and a counter,
    since no actual list for list or counter!'''
    if n <= 1:
        return n

    previous, current = 0, 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))