class HashTable():
	def __init__(self, bucket_count):
		self.bucket_count = bucket_count
		self.hash_table = [[] for _ in range(bucket_count)]
		self._multiplier = 263
		self._prime = 1000000007

	def __hash(self, string):
		ans = 0
		for c in reversed(string):
			ans = (ans * self._multiplier + ord(c)) % self._prime
		return ans % self.bucket_count

	def add(self, word):
		hash = self.__hash(word)
		if word not in self.hash_table[hash]:
			self.hash_table[hash] = [word] + self.hash_table[hash]

	def delete(self, word):
		hash = self.__hash(word)
		if word in self.hash_table[hash]:
			self.hash_table[hash].remove(word)

	def find(self, word):
		hash = self.__hash(word)
		bucket = self.hash_table[hash]
		if word in bucket:
			print('yes')
		else:
			print('no')

	def check(self, ix):
		ix = int(ix)
		bucket = self.hash_table[ix]
		print(' '.join(bucket))

def read_queries():
	n = int(input())
	return [input().split() for i in range(n)]

def main():
	bucket_count = int(input())
	queries = read_queries()
	pb = HashTable(bucket_count)

	for command, arg in queries:
		if command == 'add':
			pb.add(arg)
		elif command == 'del':
			pb.delete(arg)
		elif command == 'find':
			pb.find(arg)
		elif command == 'check':
			pb.check(arg)

if __name__ == '__main__':
	main()