
def copiar_sin_repetidos(self):
    #Genero una instancia de la lista
    copia = LinkedList()
    #Verifico si la lista es vacia caso contrario retorno una lista vacia
    if self.__first != None:
        lista = [self.__first.value]
        #Inicializo la lista  a retornar con el primer valor
        copia._first = LinkedList.Node(self._first.value)
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