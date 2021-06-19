class SubstringFinder:
    def __init__(self, pattern, text, _prime, _multiplier):
        self.pattern = pattern
        self.pattern_length = len(pattern)
        self.text = text
        self.text_length = len(text)
        self._prime = _prime
        self._multiplier = _multiplier
        self.hash_table = [None for _ in range(self.text_length - self.pattern_length + 1)]

    def PolyHash(self, string):
        hash = 0

        for s in reversed(string):
            hash = (hash * self._multiplier + ord(s)) % self._prime

        return hash

    def PrecomputeHashes(self):
        string = self.text[self.text_length - self.pattern_length:self.text_length]
        self.hash_table[self.text_length - self.pattern_length] = self.PolyHash(string)
        y = 1

        for i in range(0, self.pattern_length):
            y = (y * self._multiplier) % self._prime

        for i in range(self.text_length - self.pattern_length - 1, -1, -1):
            old_hash_adj = self._multiplier * self.hash_table[i + 1]
            new_left_str = ord(self.text[i])
            old_right_str = ord(self.text[i + self.pattern_length])

            self.hash_table[i] = (old_hash_adj + new_left_str - y * old_right_str) % self._prime

    def RabinKarp(self):
        result = []
        pHash = self.PolyHash(self.pattern)
        self.PrecomputeHashes()

        for i in range(self.text_length - self.pattern_length + 1):
            tHash = self.hash_table[i]

            if pHash != tHash:
                continue

            substr = self.text[i: i + self.pattern_length]
            if substr == self.pattern:
                result.append(i)

        return result

def read_input():
    return (input().rstrip(), input().rstrip())

def main(_prime, _multiplier):
    pattern, text = read_input()
    result = SubstringFinder(pattern, text, _prime, _multiplier).RabinKarp()
    for r in result:
        print(r)

if __name__ == '__main__':
    main(_prime=100057, _multiplier=557)
