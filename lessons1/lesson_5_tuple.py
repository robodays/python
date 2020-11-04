tup1 = (10, 20, 'test', 54.33)      # кортеж
tup2 = tuple("Test test")           # кортеж
tup3 = "Test test", "test1", 33     # кортеж
tup4 = tuple("Test test")           # кортеж
list1 = [10, 20, 'test', 54.33]     # список
el1 = ("Test test")                 # простой элемент
el2 = "Test test"                   # простой элемент


# tup1[0] = 1  # так нелзя
list1[0] = 1

print(tup1.__sizeof__())
print(list1.__sizeof__())
print(tup1)
print(list1)

print(tup2)
print(tup3)
print(tup4)
print(el1)
print(el2)
