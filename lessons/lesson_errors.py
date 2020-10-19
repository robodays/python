
import random
print("Я загадаю число от 0 до 100, а Вы попробуйте его отгадать за 10 попыток: ")
rnd = random.randint(0, 100)
for i in range(1, 10):
    try:
        i_num = int(input())
        if i_num > rnd:
            print("Вы ввели больше моего числа")
        if i_num < rnd:
            print("Вы ввели меньше моего числа")
        if i_num == rnd:
            print(f"Вы угадали за {i} попыток")
            break
    except ValueError:
        print("Ошибка! Вы ввели не число!")     # перехват ошыбки ValueError
    except:
        print("Не известная Ошибка!")     # перехват любой ошыбки
    else:
        print("Все выполнелось без ошибок!")    # выполняется без ошыбок
    finally:
        print("Конец кода")                     # выполняется всегда
