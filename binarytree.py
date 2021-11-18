class binarytreenode():

	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

	def addnode(self, data):				
		if data == self.data:
			return

		if data < self.data:
			if self.left:
				self.left.addnode(data)
			else:
				self.left = binarytreenode(data)
			return
		
		else:	
			if self.right:
				self.right.addnode(data)
			else:
				self.right = binarytreenode(data)
		

	def search(self, val):
		if val == self.data:
			return True

		if val < self.data:
			if self.left:
				return self.left.search(val)
			return False

		if val > self.data:
			if self.right:
				return self.right.search(val)
			return False


	def inorder(self):
		elements = []
		if self.left:
			elements += self.left.inorder()

		elements.append(self.data)

		if self.right:
			elements += self.right.inorder()

		return elements


	def find_min(self):
		ptr = self
		while ptr.left:
			ptr = ptr.left
		return "the minimum element is " + str(ptr.data)

	def find_max(self):
		ptr = self
		while ptr.right:
			ptr = ptr.right
		return "the maximum element is " + str(ptr.data)

	def calculate_sum(self):
		return sum(elements)

	def delete(self, val):
		if self.data is None:
			return

		if val < self.data:
			if self.left:
				self.left = self.left.delete(val)
			else:
				return

		if val > self.data:
			if self.right:
				self.right = self.right.delete(val)
			else:
				return

		else:
			if self.left is None:
				temp = self.right
				self = None
				return temp

			if self.right is None:
				temp = self.left
				self = None
				return temp

			node = self.right
			while node.left:
				node = node.left

			self.data = node.data
			self.right = self.right.delete(node.data)

		return self



		




listfortree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
root = binarytreenode(1)
for x in listfortree:
	root.addnode(x)

print(root.inorder())
root.delete(33)
root.delete(5)
root.delete(2)
root.delete(7)
root.delete(9)
root.delete(14)
print(root.inorder())
