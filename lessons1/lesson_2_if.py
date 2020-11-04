num = input("Введите число:")
if int(num) > 0:
    if int(num) > 10:
        print("Вы ввели больше 10")
        if int(num) > 50:
            print("Вы ввели больше 50")
elif int(num) < -10:
    print("Вы ввели меньше -10")
else:
    print("Вы ввели меньше 0 и больше -10")

name = input("Test")
prt = "Да Test" if name == "Test" else "Не Test"
print(prt)
