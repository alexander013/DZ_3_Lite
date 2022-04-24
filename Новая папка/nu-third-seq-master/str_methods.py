# Строки

# Объявление
friend = 'Максим Александрович Попов'
friend = "Максим Александрович Попов"

friend = 'Максим "Александрович" Попов'
friend = "Максим 'Александрович' Попов"

friend = 'Максим \'Александрович\' Попов'
# print(friend)

friend = 'Максим Александрович \n Попов'

print(friend)

friend = 'Максим Александрович \\n Попов'

print(friend)

friend = ''
# friend = ' '

# Индексы - индексы начинаются с 0
friend = 'Максим Александрович Попов'

print(friend[2])
print(friend[5])
print(friend[6])

# Отрицательные индексы
print(friend[-2])
print(friend[-1])

letter = friend[2]
print(type(letter))

# Срезы
hello = 'hello world'
# lo wo
print(hello[3:8])

# hello
print(hello[:5])

# world
print(hello[6:])

print(hello[1:-1])

# Функции и методы строки
# 1. Функции -
friend = 'Максим Александрович Попов'
friend_fio_length = len(friend)
print(friend_fio_length)

friend = 'Максим'
friend_fio_length = len(friend)
print(friend_fio_length)

# 2. Метод
friend_upper = friend.upper()

print(friend_upper)

# 3. Оператор На вхождение подстроки в строку
friend = 'Максим Александрович Попов'

letters = 'андр'

print(letters in friend)
print('Андр' in friend)

if letters in friend:
    print('Есть')

# Методы строк
friend = 'Максим александрович Попов'
# Надо заменить фамилию на Иванов
print(friend[:21] + 'Иванов')

# Метод для замены подстроки строкой
new_friend = friend.replace('Попов', 'Иванов')
print(new_friend)

# help(str)
# print(dir(str))
# Популярные методы
print(friend.upper())
print(friend.lower())
print(friend.title())
print(friend.isdigit())
# Метод split
print(friend.split(' '))

goods = 'стол;;;стул;;;диван'
print(goods.split(';;;'))

goods = 'столseparator/;стулseparator/;диван'
print(goods.split('separator/;'))

bad_data = 'стол;стул,диван кравать'

print(bad_data.replace(';', ' ').replace(',', ' ').split())

# Форматирование строк
age = 20
name = 'Макс'
# 1. конкатенация +
info = 'Имя: ' + name + ' age: ' + str(age)
print(info)

# 2. format
info = 'Имя: {} age: {}'.format(name, age)
print(info)

# 3. f
info = f'Имя: {name} age: {age}'
print(info)

# Неизменяемость строк (изменяемые и неизменяемые типы)
friend = 'Максим александрович Попов'
upper_friend = friend.upper()
print(upper_friend)

friend = friend.upper()
print(friend)
# friend[0] = 'А'

l = []
l.append(1)
print(l)
