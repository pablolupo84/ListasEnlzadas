import random

from doublelinkedlist import DoubleLinkedList

if __name__ == '__main__':
	my_list = DoubleLinkedList()
	data=[random.randint(10,15) for i in range(10)]

	print (data)
	for value in data:
	 	my_list.insert_as_first(value)
	# 	my_list.insert_at_end(value)

	print('insert_after_item')
	my_list.insert_after_item(10,6)
	my_list.printList()
	print('insert_before_item')
	my_list.insert_before_item(10,6)
	my_list.printList()
	print("Longitud: {}".format(len(my_list)))
	print("---------------")
	my_list.recorrer_lista()
	print('delete_at_start')
	my_list.delete_at_start()
	my_list.printList()
	print('delete_at_end')
	my_list.delete_at_end()
	my_list.printList()
	print('delete_element_by_value')
	my_list.delete_element_by_value(6)
	my_list.printList()
	my_list.insert_as_first("nombre")

	print(my_list.all_type(1))
	


	# for item in my_list:
	# 	print(item)
