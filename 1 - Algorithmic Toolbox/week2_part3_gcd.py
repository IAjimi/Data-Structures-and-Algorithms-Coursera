import sys

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        a = a % b
        return gcd_recursive(b, a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_recursive(a, b))
