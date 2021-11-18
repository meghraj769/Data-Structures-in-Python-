from collections import deque

class queue():
	def __init__(self):
		self.container = deque()

	def enqueue(self, val):
		self.container.appendleft(val)

	def dequeue(self):
		return self.container.pop()

	def length(self):
		return len(self.container)

	def isempty(self):
		return len(self.container) == 0

	def front(self):
		return self.container[-1]



def producenos(n):
	binarynos = queue()
	binarynos.enqueue("1")

	for i in range(n):
		front = binarynos.front()
		print("    ",front)
		binarynos.enqueue(front + "0")
		binarynos.enqueue(front + "1")

		binarynos.dequeue()


if __name__ == "__main__":
	producenos(10)