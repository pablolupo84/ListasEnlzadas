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

    def insert(self, value):
        if len(self) == 0 or value <= self.__first.value:
            self.__first = self.Node(value, self.__first)
        else:
            current = self.__first
            
            while current.next_node != None and current.next_node.value < value:
                current = current.next_node
                
            current.next_node = self.Node(value, current.next_node)

        self.__len += 1

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

    