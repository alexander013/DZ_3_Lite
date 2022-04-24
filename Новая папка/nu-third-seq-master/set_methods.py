# set
# set набор уникальных данных
# Объявление
office = {'max', 'kate', 'john', 'leo', 'leo'}

print(type(office))
print(office)

office.add('leo')

print(office)

# 1. уникальность
office = ['max', 'kate', 'john', 'leo', 'leo']

print(set(office))

# 2. операции с множествами
office = {'max', 'kate', 'john', 'leo'}
freelance = {'max', 'kate', 'poll'}

# только в офисе
print(office-freelance)
# только на фрилансе
print(freelance-office)
# и там и там
print(office&freelance)
# объединениен
print(office|freelance)

for item in office:
    print(item)