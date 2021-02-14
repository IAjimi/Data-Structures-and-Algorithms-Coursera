import sys

def get_optimal_value(capacity, weights, values):
    V = 0
    unit_val = [values[i] / weights[i] for i in range(len(weights))]

    # Sort unit_value, weights
    sorted_uv_idx = sorted(range(len(unit_val)), key = lambda x:unit_val[x], reverse = True)
    weights = [weights[i] for i in sorted_uv_idx]
    unit_val.sort(reverse = True)

    # Iterate over sorted list
    for i in range(len(unit_val)):
        if capacity == 0:
            return round(V, 4)
        else:
            a = min(weights[i], capacity)
            V += a * unit_val[i]
            weights[i] += -a
            capacity += -a

    return V


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
