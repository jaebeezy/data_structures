class Node(object):

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST(object):

	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertNode(data, self.root)

	def insertNode(self, data, node):
		if data < node.data:
			if node.left:
				self.insertNode(data, node.left)
			else:
				node.left = Node(data)
		else:
			if node.right:
				self.insertNode(data, node.right)
			else:
				node.right = Node(data)

	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root)

	def removeNode(self, data, node):
		if not node:
			return node

		if data < node.data:
			node.left = self.removeNode(data, node.left)
		elif data > node.data:
			node.right = self.removeNode(data, node.right)
		else:
			if not node.left and not node.right:
				print("Removing a leaf node...")
				del node
				return None
			if not node.left:
				print("Removing a node with a single right child...")
				tempNode = node.right
				del node
				return tempNode
			elif not node.right:
				print("Removing a node with a single left child...")
				tempNode = node.left
				del node
				return tempNode

			print("Removing node with two children...")
			tempNode = self.getPredecessor(node.left)
			node.data = tempNode.data
			node.left = self.removeNode(tempNode.data, node.left)

		return node

	def getPredecessor(self, node):
		if node.right:
			return self.getPredecessor(node.right)
		return node

	def getMinValue(self):
		if self.root: 
			return self.getMin(self.root)

	def getMin(self, node):
		if node.left:
			return self.getMin(node.left)

		return node.data

	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root)

	def getMax(self, node):
		if node.right:
			return self.getMin(node.right)

		return node.data

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root)

	def traverseInOrder(self, node):
		if node.left:
			self.traverseInOrder(node.left)

		print("%s " % node.data)

		if node.right:
			self.traverseInOrder(node.right)


bst = BST()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)
bst.remove(10)

print(bst.traverse())