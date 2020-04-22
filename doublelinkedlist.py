class DoubleLinkedList:
	class Node:
		def __init__(self,value,prev_node=None,next_node=None):
			self.prev_node=prev_node
			self.value=value
			self.next_node=next_node

	def __init__(self):
		self.__first=self.__last=None
		self.__len=0

	def __len__(self):
		return self.__len

	def __iter__(self):
		self.__current = self.__first
		return self

	def __next__(self):
		if self.__current !=None:
			result = self.__current.value
			self.__current=self.__current.next_node
			return result
		else:
			raise StopIteration

	def printList(self): 
		temp = self.__first 
		while (temp): 
			print (temp.value,) 
			temp = temp.next_node
  
	#Escriba su codigo debajo de esta linea
	def insert_as_first(self,value):
		new_node=DoubleLinkedList.Node(value)
		if self.__first==None:
			self.__first=new_node
			self.__len+=1
		else:
			new_node.next_node=self.__first
			self.__first.prev_node=new_node
			self.__first=new_node
			self.__len+=1
	
	def insert_at_end(self, value):
		new_node=DoubleLinkedList.Node(value)
		if self.__first==None:
			self.__first = new_node
			self.__len+=1
		else:
			last = self.__first
			while last.next_node is not None:
				last = last.next_node
			last.next_node = new_node
			new_node.prev_node = last
			self.__len+=1
	
	def insert_after_item(self, item, value):
		if self.__first == None:
			print("Lista vacia")
		else:
			n = self.__first
			while n is not None:
				if n.value == item:
					break
				n = n.next_node
			if n is None:
				print("item no encontrado")
			else:
				new_node=DoubleLinkedList.Node(value)
				new_node.prev_node = n
				new_node.next_node = n.next_node
				if n.next_node is not None:
					n.next_node.prev_node = new_node
				n.next_node = new_node

	def insert_before_item(self, item, value):
		if self.__first is None:
			print("Lista vacia")
		else:
			n = self.__first
			while n is not None:
				if n.value == item:
					break
				n = n.next_node
			if n is None:
				print("item no encontradot")
			else:
				new_node=DoubleLinkedList.Node(value)
				new_node.next_node = n
				new_node.prev_node = n.prev_node
				if n.prev_node is not None:
					n.prev_node.next_node = new_node
				n.prev_node = new_node

	def recorrer_lista(self):
		if self.__first is None:
			print("Lista vaci")
		else:
			n = self.__first
			while n is not None:
				print(n.value , " ")
				n = n.next_node

	def delete_at_start(self):
		if self.__first is None:
			print("The list has no element to delete")
		if self.__first.next_node is None:
			self.__first = None
		self.__first = self.__first.next_node
		self.prev_node = None

	def delete_at_end(self):
		if self.__first is None:
			print("The list has no element to delete")
		if self.__first.next_node is None:
			self.__first = None
		n = self.__first
		while n.next_node is not None:
			n = n.next_node
		n.prev_node.next_node = None

	def delete_element_by_value(self, item):
		if self.__first is None:
			print("The list has no element to delete")
		if self.__first.next_node is None:
			if self.__first.value == item:
				self.__first = None
			else:
				print("Item not found") 
		if self.__first.value == item:
			self.__first = self.__first.next_node
			self.__first.prev_node = None
		n = self.__first
		while n.next_node is not None:
			if n.value == item:
				break;
			n = n.next_node
		if n.next_node is not None:
			n.prev_node.next_node = n.next_node
			n.next_node.prev_node = n.prev_node
		else:
			if n.item == item:
				n.prev_node.next_node = None
			else:
				print("Element not found")