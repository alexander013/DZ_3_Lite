element_1 = input('Введите числа: ')
element_1_list = element_1.split(',')
print(element_1_list)

element_2 = input('Введите числа: ')
element_2_list = element_2.split(',')
print(element_2_list)

i = 0
while i != len(element_1_list):
    if element_1_list[i] in element_2_list:
        element_1_list.pop(i)
    else:
        i += 1
print(element_1_list)
