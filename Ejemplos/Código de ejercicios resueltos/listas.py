class Listas:
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
        nuevo = Listas.Node(value)
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
        copia = Listas()# Objeto a devolver
        if self.__first != None: #¿La lista está vacía?
            #Se copia el primer elemento y desde él se comienza a
            #insertar el resto de nodos
            copia.__first = Listas.Node(self.__first.value)
            p = self.__first.next_node
            q = copia.__first
            while p != None:
                q.next_node = Listas.Node(p.value)
                q = q.next_node
                p = p.next_node
                
            copia.__len = self.__len
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
        
        pares = Listas()
        impares = Listas()
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
                    ant.next_node = Listas.Node(ant.value + 1, ant.next_node)
                    self.__len += 1
                    ant = ant.next_node
                ant = p
                p = p.next_node
                
        
