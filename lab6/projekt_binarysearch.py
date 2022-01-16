#Marcin Głód, ISI NS, Algorytmy i struktury danych
from typing import Any

class BinaryNode:
	value:Any
	left_child: 'BinaryNode'
	right_child: 'BinaryNode'

	def __init__(self, value=None):
		self.value = value
		self.left_child = None
		self.right_child = None

	def min(self):
		if (self.left_child is not None):
			return min(self.left_child)
		else:
			return self.value

class BinarySearchTree:
	root: BinaryNode

	def __init__(self):
		self.root=None

	def insert(self, value:Any)-> None:
		if (self.root == None):
			self.root = BinaryNode(value)
		else: 
			self._insert(self.root, value)
	def _insert(self, node: BinaryNode, val: Any) ->BinaryNode:
		if (val<node.value):
			if (node.left_child==None):
				node.left_child = BinaryNode(val)
			else:
				node.left_child = self._insert(node.left_child, val)
		if (val>node.value):
			if (node.right_child==None):
				node.right_child = BinaryNode(val)
			else:
				node.right_child = self._insert(node.right_child, val)
		if (val == node.value):
			print("saw that one already")

	def insertlist(self, lista: list[any])->None:
		x = len(lista)
		for i in range(x):
			self.insert(lista[i])
			

	def contains(self, value: Any) ->bool:
		if (self.root is not None):
			if (value == self.root.value):
				return True
			elif (value < self.root.value):
				if self.root.left_child is not None:
					return self._contains(self.root.left_child, value)
			elif (value > self.root.value):
				if self.root.right_child is not None:
					 return self._contains(self.root.right_child, value)

	def _contains(self, node: BinaryNode, value: Any)->bool:
			if (value == node.value):
				return True
			elif (value < node.value):
				if node.left_child is not None:
					_contains(node.left_child, value)
				else:
					return False
			elif (value > node.value):
				if node.right_child is not None:
					_contains(node.right_child, value)
				else:
					return False

	def remove(self, value: Any) ->None:
		if (self.root is None):
			return None
		else: 
			self._remove(self.root, value)

	def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
		if (node.value == value):
			if (node.left_child == None) and (node.right_child == None):
				return None
			elif (node.left_child == None):
				return node.right_child
			elif (node.right_child == None):
				return node.left_child
		elif (node.value > value):
			self._remove(node.left_child, value)
		elif (node.value < value):
			self._remove(node.right_child, value)

	def show(self) -> None:
		if self.root is not None:
			self._show(self.root)
	def _show(self, node: BinaryNode):
		if node is not None:
			self._show(node.left_child)
			print(str(node.value))
			self._show(node.right_child)


tree = BinarySearchTree()
tree.insert(8)
tree.insert(4)
tree.insert(11)
#from random import randint
#for i in range(10):
#	tree.insert(randint(1,30))
 
print(tree.contains(4))
print(tree.contains(22))
tree.show()
tree.remove(4)
tree.show()
