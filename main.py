import random

from Clases_linkedlist import *

my_lista_1=LinkedList()

my_lista_1.insert(0,1)
my_lista_1.insert(1,2)
my_lista_1.insert(2,3)
my_lista_1.insert(3,4)
my_lista_1.insert(4,5)
print(my_lista_1)

my_lista_2=my_lista_1.copiar_sin_repetidos()
print(my_lista_2)



