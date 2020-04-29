import random

from doublelinkedlist import DoubleLinkedList

if __name__ == "__main__":
    my_list = DoubleLinkedList()
    data = [random.randint(10, 15) for i in range(10)]
    
    for value in data:
        my_list.insert_as_first(value)

    for item in my_list:
        print(item)