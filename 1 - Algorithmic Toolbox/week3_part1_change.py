import sys

def get_change(m):
    coin_number = 0

    for n in [10, 5]:
    	coin_number += m // n
    	m = m % n

    return coin_number + m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
