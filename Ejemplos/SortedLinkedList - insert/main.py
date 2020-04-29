import random

from sortedlinkedlist import SortedLinkedList

if __name__ == "__main__":
    my_slist = SortedLinkedList()
    
    for i in range(10):
        my_slist.insert(random.randint(10, 100))

    for item in my_slist:
        print(item)