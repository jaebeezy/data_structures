class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None 
		self.prevNode = None 

class DoublyLinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0 

	def insertStart(data):
		self.size += 1
		newNode = Node(data)

		if not self.head