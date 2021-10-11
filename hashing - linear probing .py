#collision handling with the help of linear probing
class hash():
	def __init__(self, max):
		self.max = max
		self.arr = [None for i in range(self.max)]

	def gethash(self,key):
		h = 0
		for char in key:
			h += ord(char)
		return h%self.max

	def disp(self):
		return self.arr

	def __setitem__(self, key, value):
		h = self.gethash(key)

		if self.arr[h] is None:
			self.arr[h] = (key,value)
			return

		i = 0
		while True:
			newindex = (h + i) % self.max
			if self.arr[newindex] is None:
				self.arr[newindex] = (key,value)
				return
			i+=1
			if newindex == h:
				print(f"HASH TABLE IS FULL!!!! hence the element {value} cannot be inserted.\n")
				return
	
	def __delitem__(self,key):
		h = self.gethash(key)

		if self.arr[h] is None:
			print("Invalid key!!!")
			return
		if self.arr[h][0] == key:
			self.arr[h] = None
			return

		i = 0
		while True:
			newindex = (h + i)%self.max
			if self.arr[newindex][0] == key:
				self.arr[newindex] = None
				return
			i+=1
			if newindex == h:
				print("Invalid key!!!!")
				return
