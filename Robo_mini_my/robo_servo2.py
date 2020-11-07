import serial
import time
import pygame

from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk

arduino = serial.Serial('COM4', 9600)
time.sleep(2)
global seconds_old, cl_1, cl_2, cl_3, cl_4, cl_5, cl_6, cl_7, cl_8, cl_9, \
    cl_10, cl_11, cl_12, cl_13, cl_14, cl_15, cl_16, cl_17
seconds_old = time.time()
# порт0
cl_1 = 0
min_1 = 290
max_1 = 586
mid_1 = 386
# порт1
cl_2 = 0
min_2 = 172
max_2 = 460
mid_2 = 366
# порт2 середина
cl_3 = 0
min_3 = 280
max_3 = 600
mid_3 = 487
# порт3 середина
cl_4 = 0
min_4 = 135
max_4 = 488
mid_4 = 276

cl_5 = 0
min_5 = 130
max_5 = 600
mid_5 = 444

cl_6 = 0
min_6 = 130
max_6 = 600
mid_6 = 314
# good
cl_7 = 0
min_7 = 190
max_7 = 600
mid_7 = 471

cl_8 = 0
min_8 = 138
max_8 = 600
mid_8 = 312

cl_9 = 0
min_9 = 130
max_9 = 550
mid_9 = 266
# порт9
cl_10 = 0
min_10 = 100
max_10 = 600
mid_10 = 480
# руки
cl_11 = 0
min_11 = 130
max_11 = 615
mid_11 = 367

cl_12 = 0
min_12 = 130
max_12 = 615
mid_12 = 368

cl_13 = 0
min_13 = 130
max_13 = 544
mid_13 = 491

cl_14 = 0
min_14 = 224
max_14 = 615
mid_14 = 276

cl_15 = 0
min_15 = 130
max_15 = 615
mid_15 = 386

cl_16 = 0
min_16 = 130
max_16 = 615
mid_16 = 406

cl_17 = 0
min_17 = 130
max_17 = 615
mid_17 = 300



def click1():
    global seconds_old, cl_1
    cl_1 = str('1,'+format(spin1.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_1.encode())
        seconds_old = time.time()
def click2():
    global seconds_old, cl_2
    cl_2 = str('2,'+format(spin2.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_2.encode())
        seconds_old = time.time()
def click3():
    global seconds_old, cl_3
    cl_3 = str('3,'+format(spin3.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_3.encode())
        seconds_old = time.time()
def click4():
    global seconds_old, cl_4
    cl_4 = str('4,'+format(spin4.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_4.encode())
        seconds_old = time.time()
def click5():
    global seconds_old, cl_5
    cl_5 = str('5,'+format(spin5.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_5.encode())
        seconds_old = time.time()
def click6():
    global seconds_old, cl_6
    cl_6 = str('6,'+format(spin6.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_6.encode())
        seconds_old = time.time()
def click7():
    global seconds_old, cl_7
    cl_7 = str('7,'+format(spin7.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_7.encode())
        seconds_old = time.time()
def click8():
    global seconds_old, cl_8
    cl_8 = str('8,'+format(spin8.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_8.encode())
        seconds_old = time.time()
def click9():
    global seconds_old, cl_9
    cl_9 = str('9,'+format(spin9.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_9.encode())
        seconds_old = time.time()
def click10():
    global seconds_old, cl_10
    cl_10 = str('10,'+format(spin10.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_10.encode())
        seconds_old = time.time()
def click11():
    global seconds_old, cl_11
    cl_11 = str('11,'+format(spin11.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_11.encode())
        seconds_old = time.time()
def click12():
    global seconds_old, cl_12
    cl_12 = str('12,'+format(spin12.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_12.encode())
        seconds_old = time.time()
def click13():
    global seconds_old, cl_13
    cl_13 = str('13,'+format(spin13.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_13.encode())
        seconds_old = time.time()
def click14():
    global seconds_old, cl_14
    cl_14 = str('14,'+format(spin14.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_14.encode())
        seconds_old = time.time()

def click15():
    global seconds_old, cl_15
    # arduino.write(b'1')
    # if cl_15 != int(format(spin15.get()):
    cl_15 = str('15,'+format(spin15.get()))
    if (seconds_old + 0.5) <= time.time():
        #str15 = cl_15
        # arduino.write(b'%x' % cl_15)
        #arduino.write(encode(cl_15))
        arduino.write(cl_15.encode())

        seconds_old = time.time()
    else:
        pass

    # time.sleep(1)
    pass

def click16():
    global seconds_old, cl_16
    cl_16 = str('16,'+format(spin16.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_16.encode())
        seconds_old = time.time()
def click17():
    global seconds_old, cl_17
    cl_17 = str('17,'+format(spin17.get()))
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_17.encode())
        seconds_old = time.time()



def butt(event):
    click1()
    click2()
    click3()
    click4()
    click5()
    click6()
    click7()
    click8()
    click9()
    click10()
    click11()
    click12()
    click13()
    click14()
    click15()
    click16()
    click17()


# не использую
def butt_sleep(event):
    if event.keysym == 'Up':
        time.sleep(1)
        butt(event)
    if event.keysym == 'Down':
        time.sleep(1)
        butt(event)



window = Tk()
window.title("Управление SERVO 17 DOF")

#
# отправка начальных данных в ардуину
#
#

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()

var1.set(mid_1)
var2.set(mid_2)
var3.set(mid_3)
var4.set(mid_4)
var5.set(mid_5)
var6.set(mid_6)
var7.set(mid_7)
var8.set(mid_8)
var9.set(mid_9)
var10.set(mid_10)
var11.set(mid_11)
var12.set(mid_12)
var13.set(mid_13)
var14.set(mid_14)
var15.set(mid_15)
var16.set(mid_16)
var17.set(mid_17)

text17 = Label(window, text="17             ", font=("Arial Bold", 20))
text17.grid(column=2, row=0, columnspan=2)
spin17 = Spinbox(window, from_=min_17, to=max_17, width=5, textvariable=var17, command=click17)
spin17.grid(column=2, row=0)

c = Canvas(window, width=350, height=700, bg='white')
# c.pack()
tree1 = PhotoImage(file="E:/GitHub/RoboM/images/robo2.png")
image1 = c.create_image(180, 330, image=tree1)
c.grid(column=2, row=1, rowspan=16)

# Форма
#
# 15
text15 = Label(window, text="15", font=("Arial Bold", 20))
text15.grid(column=0, row=4)
spin15 = Spinbox(window, from_=min_15, to=max_15, width=5, textvariable=var15, command=click15)
spin15.grid(column=1, row=4)
# 13
text13 = Label(window, text="13", font=("Arial Bold", 20))
text13.grid(column=0, row=5)
spin13 = Spinbox(window, from_=min_13, to=max_13, width=5, textvariable=var13, command=click13)
spin13.grid(column=1, row=5)
# 11
text11 = Label(window, text="11", font=("Arial Bold", 20))
text11.grid(column=0, row=8)
spin11 = Spinbox(window, from_=min_11, to=max_11, width=5, textvariable=var11, command=click11)
spin11.grid(column=1, row=8)
# 9
text9 = Label(window, text="9", font=("Arial Bold", 20))
text9.grid(column=0, row=9)
spin9 = Spinbox(window, from_=min_9, to=max_9, width=5, textvariable=var9, command=click9)
spin9.grid(column=1, row=9)
# 7
text7 = Label(window, text="7", font=("Arial Bold", 20))
text7.grid(column=0, row=11)
spin7 = Spinbox(window, from_=min_7, to=max_7, width=5, textvariable=var7, command=click7)
spin7.grid(column=1, row=11)
# 5
text5 = Label(window, text="5", font=("Arial Bold", 20))
text5.grid(column=0, row=12)
spin5 = Spinbox(window, from_=min_5, to=max_5, width=5, textvariable=var5, command=click5)
spin5.grid(column=1, row=12)
# 3
text3 = Label(window, text="3", font=("Arial Bold", 20))
text3.grid(column=0, row=14)
spin3 = Spinbox(window, from_=min_3, to=max_3, width=5, textvariable=var3, command=click3)
spin3.grid(column=1, row=14)
# 1
text1 = Label(window, text="1", font=("Arial Bold", 20))
text1.grid(column=0, row=16)
spin1 = Spinbox(window, from_=min_1, to=max_1, width=5, textvariable=var1, command=click1)
spin1.grid(column=1, row=16)
###################################
##################################
# 16
text16 = Label(window, text="16", font=("Arial Bold", 20))
text16.grid(column=3, row=4)
spin16 = Spinbox(window, from_=min_16, to=max_16, width=5, textvariable=var16, command=click16)
spin16.grid(column=4, row=4)
# 14
text14 = Label(window, text="14", font=("Arial Bold", 20))
text14.grid(column=3, row=5)
spin14 = Spinbox(window, from_=min_14, to=max_14, width=5, textvariable=var14, command=click14)
spin14.grid(column=4, row=5)
# 12
text12 = Label(window, text="12", font=("Arial Bold", 20))
text12.grid(column=3, row=8)
spin12 = Spinbox(window, from_=min_12, to=max_12, width=5, textvariable=var12, command=click12)
spin12.grid(column=4, row=8)
# 10
text10 = Label(window, text="10", font=("Arial Bold", 20))
text10.grid(column=3, row=9)
spin10 = Spinbox(window, from_=min_10, to=max_10, width=5, textvariable=var10, command=click10)
spin10.grid(column=4, row=9)
# 8
text8 = Label(window, text="8", font=("Arial Bold", 20))
text8.grid(column=3, row=11)
spin8 = Spinbox(window, from_=min_8, to=max_8, width=5, textvariable=var8, command=click8)
spin8.grid(column=4, row=11)
# 6
text6 = Label(window, text="6", font=("Arial Bold", 20))
text6.grid(column=3, row=12)
spin6 = Spinbox(window, from_=min_6, to=max_6, width=5, textvariable=var6, command=click6)
spin6.grid(column=4, row=12)
# 4
text4 = Label(window, text="4", font=("Arial Bold", 20))
text4.grid(column=3, row=14)
spin4 = Spinbox(window, from_=min_4, to=max_4, width=5, textvariable=var4, command=click4)
spin4.grid(column=4, row=14)
# 2
text2 = Label(window, text="2", font=("Arial Bold", 20))
text2.grid(column=3, row=16)
spin2 = Spinbox(window, from_=min_2, to=max_2, width=5, textvariable=var2, command=click2)
spin2.grid(column=4, row=16)

window.bind('<Button-1>', butt)
window.bind('<Key>', butt)
#window.bind('<KeyRelease>', butt_sleep)

window.mainloop()

# click15()
