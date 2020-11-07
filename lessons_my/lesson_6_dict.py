dict1 = {'name1': 1, 'name2': 2}
dict2 = {a: a**2 for a in range(10)}
dict2 = {a: a**2 for a in range(10)}
dict3 = dict(name1='Имя1', name2="Имя2")
dict4 = dict([('2', 25), ('name', 36), (4, 40)])
dict5 = dict.fromkeys(['a', 'b', 3], 1)
dict3['name1'] = 'ИМЯ1'
dict3['name3'] = 111

print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)

person = {'name': {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'},
          'address': ['г. Андрюшки', 'ул. Васильковская д. 23б', 'кв.12'],
          'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}}
print(person['phone']['mobile_phone'])

print(person.keys())       # dict_keys(['name', 'address', 'phone'])
print(person.values())
print(person.copy())
print(person)
print(person.get('phone'))     # {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}
print(person.get('phone1'))    # None
print(person.items())
print('=========================')

# print(person.pop())
print(person.popitem())
