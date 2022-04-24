# Объявление
friends = []
friends = [1, True, 'max', 1.2]
friends = ['max', 'kate', 'john', 'leo']

# индексы
print(friends[1])
print(friends[-1])

# срезы
print(friends[1:3])

# Функции
# Длина
print(len(friends))

# Оператор вхождения
print('max' in friends)
print('poll' in friends)

# Основные методы (действия)
# Добавление, Изменение, Удаление
# Добавление в конец
friends.append('poll')

# Изменение
friends.insert(2, 'maria')
print(friends)

# Удаление
# 1. remove
friends.remove('maria')
print(friends)

friends.append('maria')
friends.append('maria')

friends.remove('maria')
friends.remove('maria')
print(friends)



# 2. изменение
friends[3] = 'leonid'

print(friends)

# 3. удаление по индексу
del friends[1]

print(friends)

friends.sort()
friends.reverse()

print(friends)