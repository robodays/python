"""rom tkinter import *

master = Tk()

w = Spinbox(master, from_=0, to=10)
w.pack()

mainloop()

"""
list1 = {}

print(list1)
list1[0] = 10
list1[8] = 80
list1[5] = 50
print(list1)

# a_dict = {"one": 1, "two": 2, "three": 3}
a_dict = ["one", "two", "three"]
print(a_dict[1])
for key in a_dict:
    print(key)
   # print(a_dict[key])

items = [1, 2, 3, 4, 5]

# 1.
for item in items:
    print(item)
print()
# 2.
for i in range(len(items)):
    print(items[i])
print()
# 3.
for i, item in enumerate(items):
    print(i, item)



from tkinter import *



def func():
    top = Toplevel(root)
    #button_top_level = Button(top, text='Нажми', command=lambda: label.config(text='Текст из модального окна')).pack()

    button_top_level = Button(top, text='Нажми', command=lambda: lab('Текст из модального окна'))
    button_top_level.pack()
    #top.grab_set()
    #top.focus_set()
    #top.wait_window()
def lab(tt):
    label.config(text=tt)

root = Tk()
label = Label(root, text='Текст')
label.pack()
button = Button(root, text='openModal', command=func).pack()
root.mainloop()