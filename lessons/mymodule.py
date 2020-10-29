def myprint():
    print("Вывод метода myprint")

def add(x,y):
    return x+y

if __name__  == "__main__":
    print("Запуск файла mymodule.py")
else:
    print("Запуск через import")