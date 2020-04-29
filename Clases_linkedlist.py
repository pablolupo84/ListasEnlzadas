class LinkedList:
	""" Desarrollo de una lista encadenada con las operaciones básicas 
		del tipo lis
	"""
	class Node:
		def __init__(self, value, next_node = None):
			self.value = value
			self.next_node = next_node
	
	def __init__(self):
		self.__first = None
		self.__len = 0
	
	def __str__(self):
		res = ""
		p = self.__first
		while p != None:
			res += str(p.value) + "-"
			p = p.next_node
		return res

	def insert(self, pos, value):
		""" Inserta en la posición pos el value
			En esta implementación se asume que pos >= 0
			No se comprueba que el tipo de pos y value sea int
		"""
		nuevo = LinkedList.Node(value)
		if self.__first == None: # Lista vacía
			self.__first = nuevo
		else:
			if pos == 0: # Se inserta al primero
				nuevo.next_node = self.__first
				self.__first = nuevo
			else: # Se inserta en medio o al final de la lista
				p = self.__first
				ant = p
				cont = 0
				while cont < pos and p != None:
					cont += 1
					ant = p
					p = p.next_node
	
				if p!= None: # Va en medio de la lista
					nuevo.next_node = p.next_node
					ant.next_node = nuevo
				else:  # Va al final de la lista
					ant.next_node = nuevo
		self.__len += 1
		#Queda pendiente el caso de que la posición sea negativa
		#l.insert(-1, 23)
        

	def index(self, value):  
		""" Devuelve la posición de value en la lista.
			Lanza ValueError si no lo encuentra
			No se comprueba que el tipo de value sea int
		"""
		cont = 0
		p = self.__first
		# La doble condición es necesaria para detectar si se llega al final
		# de la lista y el elemento no está. Y se ha de hacer la doble pregunta
		# en el orden aquí escrito
		while p != None and p.value != value:
			cont += 1
			p = p.next_node
	
		if p != None:
			return cont
		else:
			raise ValueError("Valor no encontrado")

	def remove(self, value):
		""" Elimina la primara aparición de value. Si no se encuetra no hace nada
			No se comprueba que el tipo de value sea int
		"""
		if self.__first != None: #¿La lista está vacía?
			if self.__first.value == value: # Se borra el primero
				self.__first = self.__first.next_node
				self.__len -= 1
			else:
				p = self.__first.next_node # hay que buscar el elemento
				while p != None and p.value != value:
					anterior = p
					p = p.next_node
	
				if p != None: #¿Se encontró el elemento en la lista?
					anterior.next_node = p.next_node
					self.__len -= 1

	def count(self, value):
		""" Devuelve el número de veces que aparece value en la lista    
			No se comprueba que el tipo de value sea int
		"""
		cont = 0
		p = self.__first
		while p != None:
			if p.value == value:
				cont += 1
			p = p.next_node
		return cont

	def pop(self, pos = None):
		""" Elimina de la lista el elementos que se encuentra en la posición pos.
			Lanza IndexError si pos no tiene una posición válida.
			No se comprueba que el tipo de pos sea int
		"""
		if self.__first != None: #¿La lista está vacía?
			if pos == None:
				p = self.__first # Borramos el último de la lista
				while p.next_node != None:
					anterior = p
					p = p.next_node

				anterior.next_node = None
				self.__len -= 1

				if self.__len == 0: #¿La lista solamente tenía un elemento?
					self.__first = None
			else:
				if pos >= self.__len:
					raise IndexError("Posición no válida")
				else:
					if pos == 0:# Se elimina el primero de la lista
						self.__first = self.__first.next_node
					else:
						p = self.__first
						cont = 0
						while cont < pos: #Accedemos a la posición pos
							anterior = p
							p = p.next_node
							cont +=1
						anterior.next_node = p.next_node
					self.__len -= 1
		else:
			raise IndexError("Posición no válida")

	def copy(self):
		""" Devuelve una copia de la lista
		"""
		copia = LinkedList()# Objeto a devolver
		if self.__first != None: #¿La lista está vacía?
			#Se copia el primer elemento y desde él se comienza a
			#insertar el resto de nodos
			copia.__first = LinkedList.Node(self.__first.value)
			p = self.__first.next_node
			q = copia.__first
			while p != None:
				q.next_node = LinkedList.Node(p.value)
				q = q.next_node
				p = p.next_node

			copia.__len = self.__len
		return copia
	
	def es_repetido(self,item):
		actual = self.__first
		encontrado = False
		while actual != None and not encontrado:
			if actual.value == item:
				encontrado = True
			else:
				actual = actual.next_node
		return encontrado
	
	def copiar_sin_repetidos(self):
		#Genero una instancia de la lista
		copia = LinkedList()
		#Verifico si la lista es vacia caso contrario retorno una lista vacia
		if self.__first != None:
			lista = [self.__first.value]
			#Inicializo la lista  a retornar con el primer valor
			copia._first = LinkedList.Node(self.__first.value)
			p = self.__first.next_node
			q = copia.__first
			copia.__len += 1
			#mientras no finalice la lista original
			while p != None:
				#Reviso si ya existe en la lista original-caso verdadero avanzo al siguiente nodo
				if p.value in lista:
					p = p.next_node
				else:
					#No se encuentra en la lista repetido y lo copio y aumento el tamañod e la lista
					q.next_node = LinkedList.Node(p.value)
					q = q.next_node
					copia.__len += 1
					lista.append(p.value)
			copia.__last = q
		return copia

	def clear(self):
		""" Elimina todos los elementos de la lista
		"""
		self.__first = None
		self.__len = 0

	def actualizar_info(self, nuevo_valor):
		""" Modifica el atributo value sumándole el parámetro nuevo_valor
			a todos los nodos de la lista
		"""
		if self.__first != None:
			p = self.__first
			while p != None:
				p.value += nuevo_valor
				p = p.next_node

	def pares_impares(self):
		""" Inserta en una lista los pares y en otra los impares
			el objeto self queda inalterado.
			El método devuelve:
			return (pares, impares)
		"""

		pares = LinkedList()
		impares = LinkedList()
		if self.__first != None:
			p = self.__first
			while p != None:
				if p.value % 2 == 0: # Valor par
					pares.insert(0, p.value)
				else:
					impares.insert(0, p.value)
				p = p.next_node    
		return (pares, impares)

	def pares_impares_self(self):
		""" Modifica la lista, colocando los pares al comienzo de la lista
			y los impares al final de la lista. Entre pares e impares da igual
			el orden
			self.__first->7->3->4->6->5->2->8
			self.__first->8->2->6->4->7->3->5
			No se puede crear ningún objeto.
		"""

		if self.__first != None:
			ant = self.__first
			p = self.__first.next_node
			while p != None:
				if p.value % 2 == 0: # Nodo par
					ant.next_node = p.next_node
					p.next_node = self.__first
					self.__first = p
					p = ant.next_node
				else:
					ant = p
					p = p.next_node

	def borrar_posiciones_pares(self):
		""" Elimina de la lista los nodos que se encuentran en posiciones pares
		"""
		if self.__first != None:
			self.__first = self.__first.next_node
			self.__len -= 1
			if self.__len > 1:
				ant = self.__first # Posición impar
				p = ant.next_node #Posición par
				while p != None:
					ant.next_node = p.next_node
					ant = p.next_node
					if ant == None:
						break
					else:
						p = ant.next_node
					self.__len -= 1

	def completar_lista(self):
		""" Los valores de la lista deben ser contiguos. 
			Este método inserta en la lista los valores que faltan para
			que todos los valores sean contiguos.
			Ejemplo:
			Antes de modicar:     Lista.__first ->3->6->7->10
			Después de modificar: Lista.__first ->3->4->5->6->7->8->9->10
			Se han añadido 4 nodos para cubrir los huecos de la lista
		"""

		if self.__first != None and self.__len > 1:
			ant = self.__first
			p = ant.next_node
			while p != None:
				while ant.value + 1 != p.value:
					ant.next_node = LinkedList.Node(ant.value + 1, ant.next_node)
					self.__len += 1
					ant = ant.next_node
				ant = p
				p = p.next_node
				
	def printList(self): 
		temp = self.__first 
		while (temp): 
			print (temp.value,) 
			temp = temp.next_node

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

	def all_type(self,tipo_dato):
		resultado=True
		if self.__first == None:
			print("Lista vacia")
		else:
			n = self.__first
			while n is not None:
				if type(n.value) is not type(tipo_dato):
					resultado=False
					break
				else:
					n = n.next_node
		return resultado