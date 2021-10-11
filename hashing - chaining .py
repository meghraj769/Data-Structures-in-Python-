# collision handling with the help of chaining
class hashtable:
	def __init__(self, max):
		self.max = max
		self.arr = [[] for i in range(self.max)]
	
	def gethash(self,key):
		h = 0
		for c in key:
			h+=ord(c)
		return h % self.max

	def __setitem__(self,key,value):
		h = self.gethash(key)
		found = False
		for idx,kvpair in enumerate(self.arr[h]):
			if len(kvpair)==2 and kvpair[0] == key:
				self.arr[h][idx] = (key,value)
				found = True
				break
		if not found:
			self.arr[h].append((key,value))

	def __getitem__(self,key):
		h = self.gethash(key)
		for element in self.arr[h]:
			if element[0] == key:
				return element[1]
			
	def __delitem__(self,key):
		self.arr[self.gethash(key)] = None

	def retarray(self):
		return self.arr  

# n = hashtable(10)
# n["march 6"] = 5
# n["march 17"] = 10
# print(n["march 17"])
# print(n["march 6"])
# print(n["dsyweidwe"])
# print(n.retarray())