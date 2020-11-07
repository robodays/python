def decorator(func):
    def wrapper():
        print("Текст выводится до функции 1")
        func()
        print("Текст выводится после функции 1")
    return wrapper

def test(func):
    def wrapper():
        print("Текст выводится до функции 2")
        func()
        print("Текст выводится после функции 2")
    return wrapper

@decorator
@test
def show():
    print("Текст метода")

show()