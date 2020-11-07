list1 = []  # пустой список
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [80, 90, 100]
list4 = [80, 90, [100, 101, 102], 'test']
print(list1)
print(list2)
print(list3)

list1.append(120)   # добавление в конец списка
list2.extend(list3) # добавление списка 3 в конец списка 2
list2.insert(1, 25) # добавление элемента на 1(2)-у позицию
list2.remove(30)    # удаляем первый найденый элемент 30
list2.pop(0)        # удаление нулевого элемента

print(list2.index(40))  # возвращает индекс элемента 40
print(list2.count(40))  # возвращает количество элементов 40 в списке

list2.sort()        # сортировка по возрастанию
list2.reverse()     # реверс списка
list2.clear()       # очистка списка

print(list1)
print(list2)
print(list3)
print(list4)
#=====================
print("==============================")
print(list4[1])     # выводим второй элемент, индекс 1
print(list4[-1])    # выводим первый элемент с конца
print(list4[-2])    # выводим второй элемент с конца

i = 0
while i < 4:
    print(list4[i])  # выводим элемент i
    i+=1

print(list4[0:4:3])     # item[start:stop:step]
print(list4[-1::-1])     # item[start:stop:step] реверс

print("==============================")

# list5[a + b + с for a in 'TEST' for b in 'test' for c in '1234']
list5 = [a + b + c for a in 'TEST' if a != 'T' for b in 'test' if b != 's' for c in '1234' if c != '1']
tup6 = (a + b + c for a in 'TEST' if a != 'T' for b in 'test' if b != 's' for c in '1234' if c != '1')
print(list5)
# print(tup6)

items = [1, 2, 3, 4, 5]

# 1.
for item in items:
    print(item)

print()

# 2.
for i in range(len(items)):
    print(items[i])

print()


# 3.
for i, item in enumerate(items):
    print(i, item)
