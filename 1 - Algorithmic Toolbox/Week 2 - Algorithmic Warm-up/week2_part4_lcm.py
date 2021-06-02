import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        a = a % b
        return gcd(b, a)

def lcm(a, b):
    _lcm = b / gcd(a,b)
    _lcm = _lcm * a
    return int(_lcm)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

