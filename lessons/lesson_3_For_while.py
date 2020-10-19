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
