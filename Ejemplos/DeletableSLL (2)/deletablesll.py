### Escriba su código debajo de esta línea ###
from sortedlinkedlist import SortedLinkedList
class DeletableSLL(SortedLinkedList):
    def delete(self, value):
        while self._SortedLinkedList__first != None and self._SortedLinkedList__first.value == value:
            self._SortedLinkedList__first = self._SortedLinkedList__first.next_node   
            self._SortedLinkedList__len -=1
        if self._SortedLinkedList__first != None:
            ant = self._SortedLinkedList__first
            p = self._SortedLinkedList__first.next_node
            while p != None and p.value <= value:
                if p.value == value:
                    ant.next_node = p.next_node
                    p = p.next_node
                    self._SortedLinkedList__len -=1
                else:
                    ant = p
                    p = ant.next_node