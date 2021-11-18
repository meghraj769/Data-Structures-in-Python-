# class TreeNode():
# 	def __init__(self,name):
# 		self.name = name
# 		self.child = []
# 		self.parent = None

# 	def add_child(self,childnode):
# 		self.child.append(childnode)
# 		childnode.parent = self

# 	def getlevel(self):
# 		level = 0
# 		p = self

# 		while p.parent:
# 			level += 1
# 			p = p.parent

# 		return level	

# 	def disptree(self):
# 		spaces = " " * self.getlevel() * 3
# 		prefix = spaces + "|__" if self.parent else ""
# 		print(prefix + self.name)
# 		if self.child:
# 			for child in self.child:
# 				child.disptree()

# root = TreeNode("Electronics")

# laptop = TreeNode("Laptop")
# laptop.add_child(TreeNode("Mac"))
# laptop.add_child(TreeNode("Surface"))
# laptop.add_child(TreeNode("Thinkpad"))

# cellphone = TreeNode("Cell Phone")
# cellphone.add_child(TreeNode("iPhone"))
# cellphone.add_child(TreeNode("Google Pixel"))
# cellphone.add_child(TreeNode("Vivo"))

# tv = TreeNode("TV")
# tv.add_child(TreeNode("Samsung"))
# # tv.add_child(TreeNode("LG"))

# root.add_child(laptop)
# root.add_child(cellphone)
# root.add_child(tv)

# root.disptree()



























# # electronics = treenode("electronics")

# # laptop = treenode("laptop")
# # electronics.addchild(laptop)

# # mobile = treenode("mobile") 
# # electronics.addchild(mobile)

# # tv = treenode("tv")
# # electronics.addchild(tv)

# # laptop.addchild(treenode("lenovo"))
# # laptop.addchild(treenode("hp"))
# # laptop.addchild(treenode("dell"))

# # mobile.addchild(treenode("realme"))
# # mobile.addchild(treenode("acer"))
# # mobile.addchild(treenode("samsung"))

# # tv.addchild(treenode("lg"))
# # tv.addchild(treenode("havells"))
# # tv.addchild(treenode("tcl"))

# # electronics.disptree()
# # # print("the level of electronics is ",electronics.getlevel())
# # # print("the level of laptop is ",laptop.getlevel())
# # # print("the level of mobile is ",mobile.getlevel())
# # # print("the level of tv is ",tv.getlevel())



#exercise starts
class TreeNode():
	def __init__(self, name, designation):
		self.name = name
		self.designation = designation
		self.child = []
		self.parent = None

	def add_child(self, childnode):
		self.child.append(childnode)
		childnode.parent = self

	def getlvl(self):
		lvl = 0
		ptr = self
		while ptr.parent:
			lvl += 1
			ptr = ptr.parent
		return lvl

	def print_tree(self, cr):
		if cr == "name":
			spaces = " " * self.getlvl() *3
			prefix = spaces + "|__" if self.parent else ""
			print(prefix + self.name)
			if self.child:
				for child in self.child:
					child.print_tree("name")

		elif cr == "designation":
			spaces = " " * self.getlvl() *3
			prefix = spaces + "|__" if self.parent else ""
			print(prefix + self.designation)
			if self.child:
				for child in self.child:
					child.print_tree("designation")

		elif cr == "both":
			spaces = " " * self.getlvl() *3
			prefix = spaces + "|__" if self.parent else ""
			print(prefix + self.name + " (" + self.designation + ")")
			if self.child:
				for child in self.child:
					child.print_tree("both")

		else:
			print("tameez mei")



def build_management_tree():
    # CTO Hierarchy
	infra_head = TreeNode("Vishwa","Infrastructure Head")
	infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
	infra_head.add_child(TreeNode("Abhijit", "App Manager"))

	cto = TreeNode("Chinmay", "CTO")
	cto.add_child(infra_head)
	cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
	hr_head = TreeNode("Gels","HR Head")

	hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
	hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

	ceo = TreeNode("Nilupul", "CEO")
	ceo.add_child(cto)
	ceo.add_child(hr_head)

	return ceo


if __name__ == '__main__':
	root_node = build_management_tree()
	root_node.print_tree("name")
	root_node.print_tree("designation")
	root_node.print_tree("both")
	root_node.print_tree("oth")