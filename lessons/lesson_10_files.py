f = open("text.txt", 'r')
print(f.read(5))
print("==============")
print(f.read())
f.close()
f = open("text.txt")
for line in f:
    print(line)
f.close()

f = open("text.txt", 'a') # w стирает файл, перезаписывает
f.write("1223458\n")
f.close()

f = open("text.txt")
print(f.read())
print("Имя файла: ", f.name)
print("Файл закрыт: ", f.closed)
print("В каком режиме файл открыт: ", f.mode)
# print("Пробелы: ", f.softspace)
print("Мы находимся на позиции: ", f.tell())
# Возвращаемся в начало 0
f.seek(20)
print ("Я на позиции:", f.tell())

# проверка файла на существование
import os.path
print(os.path.isfile("text.txt"))

f.close()

with open("text1.txt","wt") as f:
    i = int(input())
    #  rez=str('25/' + str(i) + ' = ' + str(25 / i))
    #  print(rez)
    f.write(str(("25/" + str(i) + " = " + str(25 / i))))

