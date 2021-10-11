# hashing without collision handling
class hashtable:
	def __init__(self, max):
		self.max = max
		self.arr = [None for i in range(self.max)]
	
	def gethash(self,key):
		h = 0
		for c in key:
			h+=ord(c)
		return h % self.max

	def __setitem__(self,key,value):
		self.arr[self.gethash(key)] = value

	def __getitem__(self,key):
		return self.arr[self.gethash(key)]

	def __delitem__(self,key):
		self.arr[self.gethash(key)] = None

	def retarray(self):
		return self.arr

# n = hashtable(10)
# n["march 6"] = 5
# n["march 17"] = 10
# print(n["march 17"])
# print(n["march 6"])
# print(n.retarray())