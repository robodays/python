"""
Программа для упращённого упоавлени сервопривадами робата через serial порт Ардуино
"""
import serial  # Для подключению к портам ардуино
import time
from tkinter import *

# arduino = serial.Serial('COM4', 9600)
# time.sleep(2)
class MyServoClass:
    """ Класс вывода повторяющихся данных
    id_servo    - id сервопривода
    begin_servo - начальное положение сервопривода
    mini = 100  - минимальное положение значение сервопривода
    maxi = 600  - максимальное положение значение сервопривода
    col = 0     - номер колонки вывода значений
    row = 0     - номер строки вывода значений
    timestamp   - метка времени для правильной отправки в serial порт
    label_wind  - переменная вывода текста в окне
    spinbox_wind- переменная вывода spinbox в окне
    val_var     - значение по умолчанию spinbox
    """
    id_servo = 0
    begin_servo = 300
    mini = 100
    maxi = 600
    col = 0
    row = 0
    timestamp = time.time()
    label_wind = {}
    spinbox_wind = {}
    val_var = {}
    text_wind = {}

    def __init__(self, id_servo, begin_servo=300, mini=100, maxi=600, col=0, row=0):
        """Конструктор объявления сервопривода"""
        self.id_servo = id_servo
        self.begin_servo = begin_servo
        self.mini = mini
        self.maxi = maxi
        self.col = col
        self.row = row

    def get_label(self):
        """Вывод значения сервопривода"""
        self.label_wind[self.id_servo] = Label(window,
                                               text=str(self.id_servo) + " <" + str(self.begin_servo) + ">[+-0]",
                                               font=("Arial Bold", 16))
        self.label_wind[self.id_servo].grid(column=0 if self.col == 0 else 3, row=self.row)
        self.val_var[self.id_servo] = IntVar()
        self.val_var[self.id_servo].set(self.begin_servo)
        self.spinbox_wind[self.id_servo] = Spinbox(window, from_=self.mini, to=self.maxi, width=5,
                                                   textvariable=self.val_var[self.id_servo], command=lambda: self.get_click())
        self.spinbox_wind[self.id_servo].grid(column=1 if self.col == 0 else 4, row=self.row)

    def get_click(self):
        """обработка изменения значение spinbox"""
        send = str(self.id_servo) + "," + str(self.spinbox_wind[self.id_servo].get())
        delt = int(format(self.spinbox_wind[self.id_servo].get())) - self.begin_servo
        self.label_wind[self.id_servo]['text'] = str(self.id_servo) + " <" + str(self.begin_servo) + ">[" + str(
            delt) + "]"
        if (self.timestamp + 0.5) <= time.time():
            # отправка на Ардуино
            #            arduino.write(send.encode())
            self.timestamp = time.time()

    def send_arduino(self):
        """быстрая отправка на ардуино"""
        send = str(self.id_servo) + "," + str(self.begin_servo)
#       arduino.write(send.encode())
        time.sleep(0.1)



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
              MyServoClass(16, 300, 130, 615, 1, 0)]  # 17 ....

def click_button2():
    for key in range(len(servo_list)):
        servo_list[key].send_arduino()
def click_button1():

    window.title("button2 {}".format("clicks"))

# Запуск окна
window = Tk()
window.title("Управление SERVO 17 DOF для Ардуино")
c = Canvas(window, width=350, height=700, bg='white')
tree1 = PhotoImage(file="images/robo3.png")
image1 = c.create_image(180, 314, image=tree1)
c.grid(column=2, row=1, rowspan=16)

# вывод данных из класса
for key in range(len(servo_list)):
    servo_list[key].get_label()

# Вывод кнопок
gen_code = Button(text="Code for Arduino", command=click_button1)
gen_code.grid(column=0, row=0)
servo_start = Button(text="Start Servo", command=click_button2)
servo_start.grid(column=2, row=0)

window.mainloop()

'''
window.bind('<Button-1>', butt)
window.bind('<Key>', butt)
# window.bind('<KeyRelease>', butt_sleep)
'''



