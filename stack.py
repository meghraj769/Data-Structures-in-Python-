class stack():
	def __init__(self):
		self.data = []

	def push(self,element):
		self.data.append(element)
		print(f"After pushing element \"{element}\" into the stack, it looks like: ")
		print("-->".join(self.data))
		return

	def pop(self):
		return self.data.pop()

	def peek(self):
		print(self.data[-1])
		return

	def disp(self):
		print("STACK ELEMENTS:")
		print("-->".join(self.data))
		return


x = stack()
x.push("1")
x.push("2")
x.push("3")
x.push("4")
x.push("5")
x.push("6")
x.push("7")
x.push("8")
x.disp()
x.peek()
x.pop()
x.peek()