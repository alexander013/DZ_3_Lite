enter_quantity_elements = int(input('Введите количество элементов: '))
list_element = []
number_1 = int(input('Введите 1 число: '))
list_element.append(number_1)
number_2 = int(input('Введите 2 число: '))
list_element.append(number_2)
number_3 = int(input('Введите 3 число: '))
list_element.append(number_3)
number_4 = int(input('Введите 4 число: '))
list_element.append(number_4)

list_element.sort()
print(list_element)