# NODE CLASS
class Node():
	def __init__(self, data = None,next = None):
		self.data = data
		self.next = next
		
# LINKED LIST CLASS
class LinkedList():

	def __init__(self,nodee):
		self.head = nodee

# INSERT AN ELEMENT AT THE BEGINNING
	def insert_at_beginning(self,data):
		node = Node(data)
		node.next = self.head
		self.head = node

# INSERT AN ELEMENT AT THE END
	def insert_at_end(self,data):
		node = Node(data)
		if self.head is None:
			self.head = node
			return

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next  = node

# PRINT THE LIST
	def print(self):
		if self.head is None:
			print("Empty list")
			return 

		itr = self.head
		while itr:
			print(itr.data)
			itr = itr.next

# INSERT A LIST OF VALUES
	def insert_values(self,listt):
		# self.head = None
		for dataa in listt:
			self.insert_at_end(dataa)

# GET THE LENGTH OF THE LIST
	def get_length(self):
		c = 1
		itr = self.head
		while itr.next:
			itr = itr.next
			c+=1
		return c

# REMOVE AN ELEMENT BY THE INDEX
	def remove_by_index(self,index):
		
		# EXCEPTION HANDLING
		
		if self.get_length == 0:
			print("Empty list")
			return
		
		if index>=self.get_length() or index<0:
			raise Exception("Invalid Index")

		if index == 0:
			self.head = self.head.next
			return

		# DELETION STARTS
		count = 0
		iter = self.head
		while iter:
			if count == index -1:
				iter.next = iter.next.next
				break
			count+=1
			iter = iter.next

# INSERT AN ELEMENT BY THE INDEX
	def insert_by_index(self,index,value):
		
		if index < 0 or index > self.get_length():
			raise Exception("Invalid index")

		if index == 0:
			node = Node(value)
			node.next = self.head
			self.head = node
			return

		count = 0
		iter = self.head
		while iter:
			if count == index - 1:
				node = Node(value)
				node.next = iter.next
				iter.next = node
				break
			
			iter = iter.next
			count+=1

	def insert_after_value(self, data_after, data_to_insert):
		f = 0
		iter = self.head
		while iter:
			if data_after == iter.data:
				f=1
				node = Node(data_to_insert)
				node.next=iter.next
				iter.next=node
				break
			iter=iter.next
		if f==0:
			print("element not found")


	def remove_by_value(self, data):
		if self.get_length()==1:
			if self.head.data == data:
				self.head = None
				return

		f=0
		iter = self.head
		while iter.next:
			if iter.next.data == data:
				iter.next = iter.next.next
				# f=1
				break
			iter = iter.next
		# if f==0:
		# 	print("element not found")


if __name__ == "__main__":
	# ll = LinkedList(Node(27))
	# ll.insert_values(["dfg","rtior","dfjdsfk","dfjkfk"])
	# ll.printlist()
	# print("\n\n\n")
	# # ll.insert_after_value("rtior","bh")
	# # ll.printlist()
	# # print("\n\n\n")
	# # ll.insert_after_value("rti","ui")
	# ll.remove_by_value("rtior")
	# ll.printlist()

	ll = LinkedList(Node(1))
	ll.insert_values(["banana","mango","grapes","orange"])
	ll.print()
	print("\n\n\n")
	ll.insert_after_value("mango","apple") # insert apple after mango
	ll.print()
	print("\n\n\n")
	ll.remove_by_value("orange") # remove orange from linked list
	ll.print()
	print("\n\n\n")
	ll.remove_by_value("figs")
	ll.print()
	print("\n\n\n")
	ll.remove_by_value("banana")
	ll.remove_by_value("mango")
	ll.remove_by_value("apple")
	ll.remove_by_value("grapes")
	ll.print()
