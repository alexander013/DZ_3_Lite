# list
friends = ['max', 'kate', 'john', 'leo']

for friend in friends:
    hello = f'Hello, {friend}'
    print(hello)

# str
friend = 'Максим Александрович Попов'
for letter in friend:
    print(letter)

# dict
friend = {
    'name': 'max',
    'age': 20,
    'has_car': True
}

# по ключам
for key in friend:
    print(key)
    print(friend[key])

# только значения
for val in friend.values():
    print(val)

# по парам ключ значение
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)


name, age, has_car = ('max', 23, True)
print(name, age, has_car)


friends = ['max', 'kate', 'john', 'leo']

for friend in friends[:2]:
    hello = f'Hello, {friend}'
    print(hello)