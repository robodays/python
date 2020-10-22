i = 0
while i < 10:
    print(i)
    i += 1

for j in "hell world":
    if j == "w":
        continue    # Начать итерацию заного
    if j == "a":
        break   # полный выход из цикла
    print(j*2, end="")
else:   # выполняется если не сработал brake
    print("    Буквы \"а\" нет")

for a in [0,3]:
    print(a)

for a in range(6):
    print(a)

list1=list(range(1, 10, 2))
print(list1)

for a in [0,3]:
    print(a)

a_dict = {"one": 1, "two": 2, "three": 3}

for key in a_dict:
    print(key)
    print(a_dict[key])
