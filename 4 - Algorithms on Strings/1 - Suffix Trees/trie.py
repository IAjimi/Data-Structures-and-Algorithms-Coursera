import sys


def build_trie(patterns):
    # initialize trie
    tree = {0: dict()}
    _id = 1

    for pattern in patterns:
        current_node = 0  # starting node

        for ix in range(len(pattern)):
            current_symbol = pattern[ix]

            if current_symbol in tree[current_node]:  # move forward
                current_node = tree[current_node][current_symbol]
            else:  # add symbol w/ unique id
                tree[current_node][current_symbol] = _id
                tree[_id] = dict()
                current_node = _id
                _id += 1

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
