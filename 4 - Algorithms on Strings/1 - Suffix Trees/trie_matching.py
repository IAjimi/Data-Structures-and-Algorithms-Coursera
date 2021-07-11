# python3
import sys

NA = -1

def build_trie(patterns):
    tree = {0: dict()}
    _id = 1

    for pattern in patterns:
        current_node = 0

        for ix in range(len(pattern)):
            current_symbol = pattern[ix]

            if current_symbol in tree[current_node]:
                current_node = tree[current_node][current_symbol]
            else:
                tree[current_node][current_symbol] = _id
                tree[_id] = dict()
                current_node = _id
                _id += 1

    return tree

def PrefixTrieMatching(text, trie):
    trie_node = 0

    for ix in range(len(text)):
        symbol = text[ix]

        if trie[trie_node] == dict():  # found end of pattern
            return True
        elif symbol in trie[trie_node]:
            trie_node = trie[trie_node][symbol]
        else:
            #print("no matches found")
            return False

def TrieMatching(Text, Trie):
    matches = []

    for ix in range(len(Text)):
        output = PrefixTrieMatching(Text[ix:] + '*', Trie)  # add $ so is leaf check in PrefixTrieMatching works
        if output:
            matches.append(ix)

    return matches


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    trie = build_trie(patterns)
    ans = TrieMatching(text, trie)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')

    # trie = build_trie(['T'])
    # solution = TrieMatching('AA', trie)
    # print((' '.join(map(str, solution)) + '\n'))
