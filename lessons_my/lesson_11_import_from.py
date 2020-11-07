import math, time   # можно так
import os           # но правильней и лучше так
import platform
import random as r
import mymodule as my
from mymodule import myprint as m, add
try:
    import nonamemodule
except ModuleNotFoundError:
    print("Модуль nonamemodul не существует!")
print(math.pi)
print(math.e)
print(math.cos(90))
print(math.sin(90))
print(time.time())
print(os.getcwd())
# os.uname()
print(platform.uname())
print(platform.platform())
print(r.random())

# через import
my.myprint()
print(my.add(4,6))
# через from
m()
print(add(1,2))
