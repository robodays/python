def func1 (x):
    return x

def func2 (x,y):
    return x+y

def func3 (x,y):
    rezult2 = x + y
    return rezult2

def func4 (x):
    def add (y):
        return x + y
    return add

def func5 ():
    pass

def func6 (x,y,z = 2):
    rezult = x + y
    rezult *= z
    return rezult

def func7 (*arguments):     # кортеж tuple
    return arguments

def func8 (**arguments):    # словарь dict
    return arguments


print(func1(25))
print(func2(25,25))
print(func3(25,30))
print(func3("Hello ","World"))
test = func4(100)
print(test(200))
print(func5())
print(func6(2,4))
print(func6(2,4,3))
print("================")
print(func7('web',34.15,20))
print(func8(name = 'web', price = 34.15, poin = 20))
print("================")

rezult2 = lambda x, y : x * y
print(rezult2(10, 11))
func9 = lambda *arguments: arguments
print(func9("test1", "test2"))


print("================")

print(rezult2(3,4))
print(rezult2("test ",4))
print((lambda x, y : x * y)(4,5))
print(func9('web',34.15,20))