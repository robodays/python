list1 = [1,2,3,4,5,6,6,6,7] # список
set0 = set(list1)
print(list1)
print(set0)

set1 = set("hello") # множиство
set2 = {3,5,6,8,9,9,45} # множиство
set3 = {a**2 for a in range(10)} # множиство
set4 = frozenset("test") # не изменяемое множество

print(type(set1))
print(set1)
print(type(set2))
print(set2)
print(type(set3))
print(set3)
print(type(set4))
print(set4)
print("========================")

set5={1,2,3,44,5,6,6,7}

print(len(set5))    # 7
print(5 in set5)    # True
print("5" in set5)  # False
x = {44,22,33}
print(set5.isdisjoint(x)) # не имет элементы, хотябы один есть то false, если нет, то true
print(set5 == x) # проверка на полное равенмтво
print("=========================")
#set5.update(x)                  # добавляет новые элементы
#set5.intersection_update(x)     # выводит пересечение одинаковых элементов
#set5.difference_update(x)     # выводит отсутствующие элементы set5 в x
#set5.symmetric_difference_update(x)     # выводит отсутствующие элементы обоих множиств
set5.add(111)  # добавление
set5.remove(7)      # удаление (с ощибкой, если элемент отсутствует)
set5.discard(6)     # удаление (без ошибок)
set5.pop()          # удаляет первый элемент (может рандомный)
set5.clear()        # очистка
print(set5)


