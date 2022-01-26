# NODE CLASS
class Node():
	def __init__(self, data = None,next = None):
		self.data = data
		self.next = next
		
# LINKED LIST CLASS
class LinkedList():
	def __init__(self):
		self.head = None

# INSERT AN ELEMENT AT THE BEGINNING : Check first if the head is present, if head is not there make the node the head otherwise in the next
#part of the node insert self.head then make the node self.head
	def insert_at_beginning(self,data):
		node = Node(data)
		if self.head is None:
			self.head = node
			return self
		node.next = self.head
		self.head = node

# INSERT AN ELEMENT AT THE END : Check for the head first, if the head is not there make the head equal to the node otherwise take a pointer
#named ptr and iterate to the end of the linkedlist and then make ptr.next = node
	def insert_at_end(self,data):
		node = Node(data)
		if self.head is None:
			self.head = node
			return self

		ptr = self.head
		while ptr.next:
			ptr = ptr.next

		ptr.next  = node

# PRINT THE LIST : check for the head first if the head is not there print empty list otherwise iterate and print along the way
	def print(self):
		if self.head is None:
			print("Empty list")
			return self

		ptr = self.head
		while ptr:
			print(ptr.data)
			ptr = ptr.next

# INSERT A LIST OF VALUES
	def insert_values(self,listt):
		# self.head = None
		for dataa in listt:
			self.insert_at_end(dataa)

# GET THE LENGTH OF THE LIST
	def get_length(self):
		if self.head is None:
			return 0
		c = 1
		ptr = self.head
		while ptr.next:
			ptr = ptr.next
			c+=1
		return c

# INSERT AN ELEMENT BY THE INDEX
	def insert_by_index(self,index,value):		
		if index < 0 or index > self.get_length():
			raise Exception("Invalid index")
		if index == 0:
			self.insert_at_beginning(value)
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

# REMOVE AN ELEMENT BY THE INDEX
	def remove_by_index(self,index):		
		# EXCEPTION HANDLING		
		if self.get_length() == 0:
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
				f=1
				break
			iter = iter.next
		if f==0:
			print("element not found")


if __name__ == "__main__":
	x = LinkedList()
	x.insert_at_beginning(10)
	x.insert_at_beginning(9)
	x.insert_at_beginning(8)
	x.insert_at_end(11)
	x.insert_at_end(12)
	x.insert_values([13,14,15,16,17])
	x.insert_by_index(0,7)
	x.print()
	x.insert_after_value(16, "seventeen")
	x.print()