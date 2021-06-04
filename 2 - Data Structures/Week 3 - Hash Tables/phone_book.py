class PhoneBook():
	def __init__(self):
		self.book = {}

	def add(self, number, name):
		self.book[number] = name

	def delete(self, number):
		if number in self.book:
			del self.book[number]

	def find(self, number):
		if number in self.book:
			print(self.book[number])
		else:
			print('not found')

def read_queries():
	n = int(input())
	return [input().split() for i in range(n)]

def main():
	queries = read_queries()
	pb = PhoneBook()

	for q in queries:
		if q[0] == 'add':
			pb.add(q[1], q[2])
		elif q[0] == 'del':
			pb.delete(q[1])
		elif q[0] == 'find':
			pb.find(q[1])

if __name__ == '__main__':
	main()