import random
print("Я загадаю число от 0 до 100, а Вы попробуйте его отгадать за 10 попыток: ")
rnd = random.randint(0, 100)
for i in range(1, 10):
    try:
        i_num = int(input())
    except ValueError:
        print("Ошибка! Вы ввели не число!")     # перехват ошыбки ValueError
        break
    except:
        print("Не известная Ошибка!")     # перехват любой ошыбки
    else:
        print("Все выполнелось без ошибок!")    # выполняется без ошыбок
    finally:
        print("Конец кода")                     # выполняется всегда
    if i_num > rnd:
        print("Вы ввели больше моего числа")
    if i_num < rnd:
        print("Вы ввели меньше моего числа")
    if i_num == rnd:
        print(f"Ура! Правильный ответ {i_num}!")
        print(f"Вы угадали за {i} попыток.")
        break


# ошибки
# print(int("string"))
# print(4/0)
# print("string"+1)