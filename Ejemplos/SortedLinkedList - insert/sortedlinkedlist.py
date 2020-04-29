class SortedLinkedList:
    class Node:
        def __init__(self, value, next_node = None):
            self.value = value
            self.next_node = next_node
        
    def __init__(self):
        self.__first = None
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
        
    def insert(self, value):
        nuevo= SortedLinkedList.Node(value)
        p= self.__first
        ant= p
        if self.__first == None:
            self.__first = nuevo
        else:
            if p.value < value:
                while p != None:
                    if p.value < value:
                        ant = p
                        p = p.next_node
                    else:
                        p= p.next_node
                nuevo.next_node = ant.next_node
                ant.next_node = nuevo
            else:
                self.__first = SortedLinkedList.Node(value, self.__first)
        self.__len +=1