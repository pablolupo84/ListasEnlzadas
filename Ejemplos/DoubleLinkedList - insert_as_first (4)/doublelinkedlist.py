class DoubleLinkedList:
    class Node:
        def __init__(self, value, prev_node = None, next_node = None):
            self.prev_node = prev_node
            self.value = value
            self.next_node = next_node
        
    def __init__(self):
        self.__first = self.__last = None
        self.__len = 0
        
    def __len__(self):
        return self.__len

    def __iter__(self):
        self.__current = self.__first
        return self

    def __next__(self):
        if self.__current != None:
            result = self.__current.value
            self.__current = self.__current.next_node
            return result
        else:
            raise StopIteration

    # Escriba su código debajo de esta línea
    def insert_as_first(self, value):
        nuevo = DoubleLinkedList.Node(value)
        if self.__first == None:
            self.__first = nuevo
            self.__len +=1
        else:
            nuevo.next_node = self.__first
            self.__first.prev_node = nuevo
            self.__first = nuevo
            self.__len +=1
        
            
            
            
            
            
            
            
            
            
            
            
            
            
    