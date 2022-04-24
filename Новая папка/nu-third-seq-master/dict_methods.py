# словари
name = 'max'
age = 20
has_car = True

friend = (name, age, has_car)

friend_inverse = (age, has_car, name)

# Словарь, объявление
friend = {
    'name': 'max',
    'age': 20,
    'has_car': True
}

print(type(friend))

# Индексы? У словаря есть ключи и мы можем их использовать
print(friend['age'])
print(friend['has_car'])

# Функции
print(len(friend))

# Оператор вхождения
# Проверяет по ключам
print('name' in friend)

# Методы (Действия), Добавить, удалить, изменить
# Добавить, Изменить
print(friend)
friend['has_wife'] = False
print(friend)
friend['has_wife'] = True
print(friend)

# Удалить
del friend['has_wife']
print(friend)

# Методы, получить значения
# ключи
print(friend.keys())
print(type(friend.keys()))
print(list(friend.keys()))
# значения
print(list(friend.values()))
# пары ключ значение - кортежи
print(list(friend.items()))

print('max' in friend.values())

