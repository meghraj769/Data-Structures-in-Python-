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

	# def getiterlist(self,h):
	# 	#returns a list of indices in probing order
	# 	# h = self.gethash(key)
	# 	iterlist = [*range(h,len(self.arr))] + [*range(0,h)]
	# 	return iterlist 

	# def __setitem__(self,key,value):
	# 	h = self.gethash(key)

	# 	if self.arr[h] is None:
	# 		self.arr[h] = (key,value)

	# 	else:
	# 		iterlist = self.getiterlist(h)
	# 		full = True
	# 		for i in iterlist:
	# 			if self.arr[i] is None:
	# 				self.arr[i] = (key,value)
	# 				full = False
	# 				break

	# 		if full:
	# 			print(f"\nThe hashable list is full so the element \"{value}\" cannot be inserted\n")


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
		


# a = hashing(10)
# a["march 1"] = 10
# a["march 2"] = 12
# a["march 3"] = 13
# a["march 4"] = 15
# a["march 5"] = 25
# a["march 6"] = 35
# a["march 7"] = 90
# print(a.disp())

# print("\n\nAfter deletion:::\n\n")
# del a["march 9"]
# print(a.disp())

a = hash(10)
a["march 1"] = 10
a["march 2"] = 12
a["march 3"] = 13
a["march 4"] = 15
a["march 5"] = 25
a["march 6"] = 35
a["march 7"] = 90
print(a.disp())