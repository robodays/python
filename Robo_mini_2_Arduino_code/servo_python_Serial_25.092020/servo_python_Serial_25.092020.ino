// Подклоючаем библиотеку Servo
#include <Servo.h> 
//#include <Wire.h>


// Подключаем серво через i2c
#include <Wire.h>                       // Подключаем библиотеку Wire
#include <Adafruit_PWMServoDriver.h>    // Подключаем библиотеку Adafruit_PWMServoDriver

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40); // Установка адреса I2C 0x40

#define SERVOMIN 300//150                   // Минимальная длительность импульса для сервопривода
#define SERVOMAX 450 //600                   // Максимальная длина импульса для сервопривода

int ServoArray[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17};

#define SERVO_0 0                       // Номер порта (0 - 15)
#define SERVO_1 1
#define SERVO_2 2
#define SERVO_3 3
#define SERVO_4 4
#define SERVO_5 5
#define SERVO_6 6
#define SERVO_7 7
#define SERVO_8 8
#define SERVO_9 9
#define SERVO_10 10
#define SERVO_11 11
#define SERVO_12 12
#define SERVO_13 13
#define SERVO_14 14
#define SERVO_15 15
#define SERVO_16 16
#define SERVO_17 17


// Создаем объект обычный
Servo Servo1;


String datafromUser,valueServo;
int indexServo;


void setup() {

    // сервы через i2c
    pwm.begin();                          // Инициализация
    pwm.setPWMFreq(60);                   // Частота следования импульсов 60 Гц
    delay(1000);                            // Пауза

    // серв обычный
    // Servo1.attach(servoPin); //серво


  //
  
  // код для настроек
  //pinMode( LED_BUILTIN , OUTPUT );

  // подключаем сериал порт
  Serial.begin(9600);
  Serial.setTimeout(50); // установить таймаут
}

void loop() {

  // код для повторения в цикле
  if(Serial.available() > 0)
  {
    //datafromUser=Serial.read();
    datafromUser=Serial.readString();
    if (datafromUser.indexOf(",")>0)  {
      String indexServo_str=datafromUser.substring(0,datafromUser.indexOf(","));
      indexServo=indexServo_str.toInt();
      valueServo=datafromUser.substring(datafromUser.indexOf(",")+1);
      Serial.println(indexServo);
      Serial.println(valueServo);         

      Serial.println(datafromUser);
      Serial.println(indexServo);
      Serial.println(valueServo);
      
      pwm.setPWM(indexServo, 0, valueServo.toInt());     
    }
  }

}
