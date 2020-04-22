class LinkedList:
    """
    Lista simplemente encadenada
    
    Atributos
    ---------
    __first: (Node) referencia al primer nodo de la lista
    __len  : (int) almacena el número de elementos de la lista
        
    Métodos
    -------
    _len_: devuelve la longitud (número de elementos) de la lista
    
    Clases
    ------
    LinkedList.Node: clase para representar los nodos de la lista encadenada
    """

    def _init_(self):
        """__first se inicializa a None y __len a 0"""
        
        self.__first = None
        self.__len = 0
        
    def _len_(self):
        """Devuelve el número de nodos de la lista"""
        
        return self.__len
    
    class Node:
        """
        Nodos de una lista simplemente encadenada
        
        Atributos
        ---------
        value    : (cualquier tipo) valor
        next_node: (Node) referencia al siguiente nodo de la lista
        """
        
        def _init_(self, value, next_node = None):
            """
            Parámetros
            ----------
            value    : valor para el atributo value
            next_node: valor para el atributo next_node
            """
            self.value = value
            self.next_node = next_node
        

    # NO MODIFIQUE ESTA LÍNEA ni el código que está por encima
    # Escriba su solución a partir de la siguiente línea

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
                
                