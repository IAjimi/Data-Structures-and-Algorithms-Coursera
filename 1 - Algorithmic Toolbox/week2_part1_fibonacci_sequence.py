def calc_fib(n):
    counter = 1
    prev_two = [0, 1]

    if n <= counter:
        return prev_two[n]
    else:
        while counter < n:
            new_fib = sum(prev_two)
            prev_two = [prev_two[1]] + [new_fib]
            counter += 1

        return new_fib

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
