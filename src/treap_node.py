import random 

# A Treap Node
class TreapNode:
	def __init__(self, key):
		self.key = key
		self.priority = random.randint(0, 99)
		self.left = None
		self.right = None