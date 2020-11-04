import serial  # Для подключению к портам ардуино
import time
import pygame

from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk


# arduino = serial.Serial('COM4', 9600)
# time.sleep(2)
class MyServoClass:
    id = 0
    begin_servo = 300
    mini = 100
    maxi = 600
    col = 0
    row = 0
    label_wind = []
    spinbox_wind = []
    text_wind = []


    def __init__(self, id_servo, begin_servo=300, mini=100, maxi=600, col=0, row=0):
        self.id = id
        self.begin_servo = begin_servo
        self.mini = mini
        self.maxi = maxi
        self.col = col
        self.row = row

    def col_row(self, col = 0, row = 0):
        self.col = col
        self.row = row

    def get_label(self):
        return Label = Label(window, text="15 <" + str(mid_15) + ">[+-0]", font=("Arial Bold", 16))
    def get_spinbox(self):
        return spin15 = Spinbox(window, from_=min_15, to=max_15, width=5, textvariable=var15, command=click15)
    def get_text(self):
        return text15.grid(column=0, row=3)
        Label = Label(window, text="15 <" + str(mid_15) + ">[+-0]", font=("Arial Bold", 16))
        text15.grid(column=0, row=3)
        spin15 = Spinbox(window, from_=min_15, to=max_15, width=5, textvariable=var15, command=click15)
        spin15.grid(column=1, row=3)

servo_list = [MyServoClass(0, 386, 290, 586, 0, 14),  # 1
              MyServoClass(1, 366, 172, 460, 1, 14),  # 2
              MyServoClass(2, 487, 280, 600, 0, 13),  # 3
              MyServoClass(3, 276, 135, 488, 1, 13),  # 4
              MyServoClass(4, 444, 130, 600, 0, 12),  # 5
              MyServoClass(5, 314, 130, 600, 1, 12),  # 6
              MyServoClass(6, 471, 190, 600, 0, 11),  # 7
              MyServoClass(7, 312, 138, 600, 1, 11),  # 8
              MyServoClass(8, 266, 130, 550, 0, 8),  # 9
              MyServoClass(9, 486, 100, 600, 1, 8),  # 10 было 480
              MyServoClass(10, 367, 130, 615, 0, 5),  # 11 ....
              MyServoClass(11, 368, 130, 615, 1, 5),  # 12 ....
              MyServoClass(12, 491, 130, 544, 0, 4),  # 13 ....
              MyServoClass(13, 276, 224, 615, 1, 4),  # 14 ....
              MyServoClass(14, 386, 130, 615, 0, 3),  # 15 ....
              MyServoClass(15, 406, 130, 615, 1, 3),  # 16 ....
              MyServoClass(16, 300, 130, 615, 1, 14)]  # 17 ....

'''
global seconds_old, cl_1, cl_2, cl_3, cl_4, cl_5, cl_6, cl_7, cl_8, cl_9, \
    cl_10, cl_11, cl_12, cl_13, cl_14, cl_15, cl_16, cl_17
seconds_old = time.time()

# порт0
cl_1 = 0
plm_1 = 0
min_1 = 290
max_1 = 586
mid_1 = 386
# порт1
cl_2 = 0
plm_2 = 0
min_2 = 172
max_2 = 460
mid_2 = 366
# порт2 середина
cl_3 = 0
plm_3 = 0
min_3 = 280
max_3 = 600
mid_3 = 487
# порт3 середина
cl_4 = 0
plm_4 = 0
min_4 = 135
max_4 = 488
mid_4 = 276

cl_5 = 0
plm_5 = 0
min_5 = 130
max_5 = 600
mid_5 = 444

cl_6 = 0
plm_6 = 0
min_6 = 130
max_6 = 600
mid_6 = 314
# good
cl_7 = 0
plm_7 = 0
min_7 = 190
max_7 = 600
mid_7 = 471

cl_8 = 0
plm_8 = 0
min_8 = 138
max_8 = 600
mid_8 = 312

cl_9 = 0
plm_9 = 0
min_9 = 130
max_9 = 550
mid_9 = 266
# порт9
cl_10 = 0
plm_10 = 0
min_10 = 100
max_10 = 600
mid_10 = 486
# руки
cl_11 = 0
plm_11 = 0
min_11 = 130
max_11 = 615
mid_11 = 367

cl_12 = 0
plm_12 = 0
min_12 = 130
max_12 = 615
mid_12 = 368

cl_13 = 0
plm_13 = 0
min_13 = 130
max_13 = 544
mid_13 = 491

cl_14 = 0
plm_14 = 0
min_14 = 224
max_14 = 615
mid_14 = 276

cl_15 = 0
plm_15 = 0
min_15 = 130
max_15 = 615
mid_15 = 386

cl_16 = 0
plm_16 = 0
min_16 = 130
max_16 = 615
mid_16 = 406

cl_17 = 0
plm_17 = 0
min_17 = 130
max_17 = 615
mid_17 = 300

'''
def uno_click():
    # global seconds_old, cl_1, plm_1, mid_1
    cl_1 = str('1,' + format(spin1.get()))
    plm_1 = int(format(spin1.get())) - mid_1
    text1['text'] = "1 <" + str(mid_1) + ">[" + str(plm_1) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_1.encode())
        seconds_old = time.time()

def click1():
    global seconds_old, cl_1, plm_1, mid_1
    cl_1 = str('1,' + format(spin1.get()))
    plm_1 = int(format(spin1.get())) - mid_1
    text1['text'] = "1 <" + str(mid_1) + ">[" + str(plm_1) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_1.encode())
        seconds_old = time.time()


def click2():
    global seconds_old, cl_2, plm_2, mid_2
    cl_2 = str('2,' + format(spin2.get()))
    plm_2 = int(format(spin2.get())) - mid_2
    text2['text'] = "2 <" + str(mid_2) + ">[" + str(plm_2) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_2.encode())
        seconds_old = time.time()


def click3():
    global seconds_old, cl_3, plm_3, mid_3
    cl_3 = str('3,' + format(spin3.get()))
    plm_3 = int(format(spin3.get())) - mid_3
    text3['text'] = "3 <" + str(mid_3) + ">[" + str(plm_3) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_3.encode())
        seconds_old = time.time()


def click4():
    global seconds_old, cl_4, plm_4, mid_4
    cl_4 = str('4,' + format(spin4.get()))
    plm_4 = int(format(spin4.get())) - mid_4
    text4['text'] = "4 <" + str(mid_4) + ">[" + str(plm_4) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_4.encode())
        seconds_old = time.time()


def click5():
    global seconds_old, cl_5, plm_5, mid_5
    cl_5 = str('5,' + format(spin5.get()))
    plm_5 = int(format(spin5.get())) - mid_5
    text5['text'] = "5 <" + str(mid_5) + ">[" + str(plm_5) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_5.encode())
        seconds_old = time.time()


def click6():
    global seconds_old, cl_6, plm_6, mid_6
    cl_6 = str('6,' + format(spin6.get()))
    plm_6 = int(format(spin6.get())) - mid_6
    text6['text'] = "6 <" + str(mid_6) + ">[" + str(plm_6) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_6.encode())
        seconds_old = time.time()


def click7():
    global seconds_old, cl_7, plm_7, mid_7
    cl_7 = str('7,' + format(spin7.get()))
    plm_7 = int(format(spin7.get())) - mid_7
    text7['text'] = "7 <" + str(mid_7) + ">[" + str(plm_7) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_7.encode())
        seconds_old = time.time()


def click8():
    global seconds_old, cl_8, plm_8, mid_8
    cl_8 = str('8,' + format(spin8.get()))
    plm_8 = int(format(spin8.get())) - mid_8
    text8['text'] = "8 <" + str(mid_8) + ">[" + str(plm_8) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_8.encode())
        seconds_old = time.time()


def click9():
    global seconds_old, cl_9, plm_9, mid_9
    cl_9 = str('9,' + format(spin9.get()))
    plm_9 = int(format(spin9.get())) - mid_9
    text9['text'] = "9 <" + str(mid_9) + ">[" + str(plm_9) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_9.encode())
        seconds_old = time.time()


def click10():
    global seconds_old, cl_10, plm_10, mid_10
    cl_10 = str('10,' + format(spin10.get()))
    plm_10 = int(format(spin10.get())) - mid_10
    text10['text'] = "10 <" + str(mid_10) + ">[" + str(plm_10) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_10.encode())
        seconds_old = time.time()


def click11():
    global seconds_old, cl_11, plm_11, mid_11
    cl_11 = str('11,' + format(spin11.get()))
    plm_11 = int(format(spin11.get())) - mid_11
    text11['text'] = "11 <" + str(mid_11) + ">[" + str(plm_11) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_11.encode())
        seconds_old = time.time()


def click12():
    global seconds_old, cl_12, plm_12, mid_12
    cl_12 = str('12,' + format(spin12.get()))
    plm_12 = int(format(spin12.get())) - mid_12
    text12['text'] = "12 <" + str(mid_12) + ">[" + str(plm_12) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_12.encode())
        seconds_old = time.time()


def click13():
    global seconds_old, cl_13, plm_13, mid_13
    cl_13 = str('13,' + format(spin13.get()))
    plm_13 = int(format(spin13.get())) - mid_13
    text13['text'] = "13 <" + str(mid_13) + ">[" + str(plm_13) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_13.encode())
        seconds_old = time.time()


def click14():
    global seconds_old, cl_14, plm_14, mid_14
    cl_14 = str('14,' + format(spin14.get()))
    plm_14 = int(format(spin14.get())) - mid_14
    text14['text'] = "14 <" + str(mid_14) + ">[" + str(plm_14) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_14.encode())
        seconds_old = time.time()


def click15():
    global seconds_old, cl_15, plm_15, mid_15
    cl_15 = str('15,' + format(spin15.get()))
    plm_15 = int(format(spin15.get())) - mid_15
    text15['text'] = "15 <" + str(mid_15) + ">[" + str(plm_15) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_15.encode())
        seconds_old = time.time()


def click16():
    global seconds_old, cl_16, plm_16, mid_16
    cl_16 = str('16,' + format(spin16.get()))
    plm_16 = int(format(spin16.get())) - mid_16
    text16['text'] = "16 <" + str(mid_16) + ">[" + str(plm_16) + "]"
    if (seconds_old + 0.5) <= time.time():
        arduino.write(cl_16.encode())
        seconds_old = time.time()


def click17():
    global seconds_old, cl_17, plm_17, mid_17
    cl_17 = str('17,' + format(spin17.get()))
    plm_17 = int(format(spin17.get())) - mid_17
    text17['text'] = "17 <" + str(mid_17) + ">[" + str(plm_17) + "]"
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

text17 = Label(window, text="17 <" + str(mid_17) + ">[+-0]", font=("Arial Bold", 16))
text17.grid(column=2, row=0, columnspan=2)
spin17 = Spinbox(window, from_=min_17, to=max_17, width=5, textvariable=var17, command=click17)
spin17.grid(column=2, row=0)

c = Canvas(window, width=350, height=700, bg='white')
# c.pack()
tree1 = PhotoImage(file="images/robo3.png")
image1 = c.create_image(180, 314, image=tree1)
c.grid(column=2, row=1, rowspan=16)



# Форма
#
# 15
text15 = Label(window, text="15 <" + str(mid_15) + ">[+-0]", font=("Arial Bold", 16))
text15.grid(column=0, row=3)
spin15 = Spinbox(window, from_=min_15, to=max_15, width=5, textvariable=var15, command=click15)
spin15.grid(column=1, row=3)
# 13
text13 = Label(window, text="13 <" + str(mid_13) + ">[+-0]", font=("Arial Bold", 16))
text13.grid(column=0, row=4)
spin13 = Spinbox(window, from_=min_13, to=max_13, width=5, textvariable=var13, command=click13)
spin13.grid(column=1, row=4)
# 11
text11 = Label(window, text="11 <" + str(mid_11) + ">[+-0]", font=("Arial Bold", 16))
text11.grid(column=0, row=5)
spin11 = Spinbox(window, from_=min_11, to=max_11, width=5, textvariable=var11, command=click11)
spin11.grid(column=1, row=5)
# 9
text9 = Label(window, text="9 <" + str(mid_9) + ">[+-0]", font=("Arial Bold", 16))
text9.grid(column=0, row=8)
spin9 = Spinbox(window, from_=min_9, to=max_9, width=5, textvariable=var9, command=click9)
spin9.grid(column=1, row=8)
# 7
text7 = Label(window, text="7 <" + str(mid_7) + ">[+-0]", font=("Arial Bold", 16))
text7.grid(column=0, row=11)
spin7 = Spinbox(window, from_=min_7, to=max_7, width=5, textvariable=var7, command=click7)
spin7.grid(column=1, row=11)
# 5
text5 = Label(window, text="5 <" + str(mid_5) + ">[+-0]", font=("Arial Bold", 16))
text5.grid(column=0, row=12)
spin5 = Spinbox(window, from_=min_5, to=max_5, width=5, textvariable=var5, command=click5)
spin5.grid(column=1, row=12)
# 3
text3 = Label(window, text="3 <" + str(mid_3) + ">[+-0]", font=("Arial Bold", 16))
text3.grid(column=0, row=13)
spin3 = Spinbox(window, from_=min_3, to=max_3, width=5, textvariable=var3, command=click3)
spin3.grid(column=1, row=13)
# 1
text1 = Label(window, text="1 <" + str(mid_1) + ">[+-0]", font=("Arial Bold", 16))
text1.grid(column=0, row=14)
spin1 = Spinbox(window, from_=min_1, to=max_1, width=5, textvariable=var1, command=click1)
spin1.grid(column=1, row=14)
###################################
##################################
# 16
text16 = Label(window, text="16 <" + str(mid_16) + ">[+-0]", font=("Arial Bold", 16))
text16.grid(column=3, row=3)
spin16 = Spinbox(window, from_=min_16, to=max_16, width=5, textvariable=var16, command=click16)
spin16.grid(column=4, row=3)
# 14
text14 = Label(window, text="14 <" + str(mid_14) + ">[+-0]", font=("Arial Bold", 16))
text14.grid(column=3, row=4)
spin14 = Spinbox(window, from_=min_14, to=max_14, width=5, textvariable=var14, command=click14)
spin14.grid(column=4, row=4)
# 12
text12 = Label(window, text="12 <" + str(mid_12) + ">[+-0]", font=("Arial Bold", 16))
text12.grid(column=3, row=5)
spin12 = Spinbox(window, from_=min_12, to=max_12, width=5, textvariable=var12, command=click12)
spin12.grid(column=4, row=5)
# 10
text10 = Label(window, text="10 <" + str(mid_10) + ">[+-0]", font=("Arial Bold", 16))
text10.grid(column=3, row=8)
spin10 = Spinbox(window, from_=min_10, to=max_10, width=5, textvariable=var10, command=click10)
spin10.grid(column=4, row=8)
# 8
text8 = Label(window, text="8 <" + str(mid_8) + ">[+-0]", font=("Arial Bold", 16))
text8.grid(column=3, row=11)
spin8 = Spinbox(window, from_=min_8, to=max_8, width=5, textvariable=var8, command=click8)
spin8.grid(column=4, row=11)
# 6
text6 = Label(window, text="6 <" + str(mid_6) + ">[+-0]", font=("Arial Bold", 16))
text6.grid(column=3, row=12)
spin6 = Spinbox(window, from_=min_6, to=max_6, width=5, textvariable=var6, command=click6)
spin6.grid(column=4, row=12)
# 4
text4 = Label(window, text="4 <" + str(mid_4) + ">[+-0]>", font=("Arial Bold", 16))
text4.grid(column=3, row=13)
spin4 = Spinbox(window, from_=min_4, to=max_4, width=5, textvariable=var4, command=click4)
spin4.grid(column=4, row=13)
# 2
text2 = Label(window, text="2 <" + str(mid_8) + ">[+-0]", font=("Arial Bold", 16))
text2.grid(column=3, row=14)
spin2 = Spinbox(window, from_=min_2, to=max_2, width=5, textvariable=var2, command=click2)
spin2.grid(column=4, row=14)

window.bind('<Button-1>', butt)
window.bind('<Key>', butt)
# window.bind('<KeyRelease>', butt_sleep)

window.mainloop()

# click15()
