
/*
 * scl grin а5
 * sda yellow а4
 * 
 * 
 * 
 */

// Подклоючаем библиотеку Servo
#include <Servo.h> 
//#include <Wire.h>

// Подключаем серво через i2c
#include <Wire.h>                       // Подключаем библиотеку Wire
#include <Adafruit_PWMServoDriver.h>    // Подключаем библиотеку Adafruit_PWMServoDriver

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40); // Установка адреса I2C 0x40

Servo myservo[17]; // create servo object to control a servo

// описание класса
class MyServoClass {  // класс Color
  public:
  MyServoClass(int id, int begin_servo, int mini, int maxi); // конструктор
  int getBegServo();                                        //1. Возвращаем начальное значение угла серва
  int getGlobalServo();                                      //2. Выводим значение угола серва
  int setGlServo(int new_gl);                               //3. Присваевание глобальному значению угла
  int setZeroServo();                                       //4. Быстрое возвращение серва в начальное значение
  int setSlowServo(int add_angle,int stepp, int delayy);    //5. Плавное перемещение серва на значение add_angle от начального
  int setFastServo(int new_angle);                          //6. Быстрое движение серва на задоное значение угла
  int getRServo(int new_angle, int stepp, int delayy);      //7. Движение серва OLD
  int setTwoSlowServo(int add_angle,int stepp, int delayy, int two, int two_add_angle, int two_begin_servo, int two_global_servo);
  int setManySlowServo(int a1, int b1, int c1);
  private:
  int _id; // обнуление
  int _min; // обнуление
  int _max; // обнуление
  int _pos; // обнуление
  int _step; // обнуление
  int _begin_servo; // начальная позиция серва
  int _global_servo; // глобальная позиция серва на данный момент
  int _new_val_servo;
  int _set_servo; // значение из serial порта
  int _orient; // выбор направления возварата серва в положение по умолчание
};
/*
 * конструктор описание
 * 
 * begin_servo начальное положение серва (последнее положение)
 * id номер серва
 * mini мин значение
 * maxi макс значение
 * 
 */
MyServoClass::MyServoClass(int id, int begin_servo=300, int mini=100, int maxi=600) { // конструктор
  _id=id;
  _begin_servo=begin_servo;
  _global_servo=begin_servo; 
  _min=mini;
  _max=maxi;
}

/*
 * Возвращаем начальное значение угла серва
 * 
 * return int _begin_servo
 */
int MyServoClass::getBegServo(){
  return _begin_servo;  
  
}

/*
 * Выводим значение угола серва
 * 
 * int output   _global_servo 
 */
int MyServoClass::getGlobalServo(){
  
  return  _global_servo; 
}

/*
 * Присваевание глобальному значению угла
 * 
 * input int new_angle
 * 
 * return _global_servo
 */
int MyServoClass::setGlServo(int new_angle){  
  _global_servo=new_angle;
  return _global_servo;
}
/*
 * Быстрое возвращение серва в начальное значение 
 * 
 * return _global_servo
 */
int MyServoClass::setZeroServo(){
  _global_servo= _begin_servo;
  pwm.setPWM(_id, 0, _begin_servo);
    Serial.print(_id);
    Serial.print(',');
    Serial.println(_begin_servo);
  return _global_servo;
}

/*
 * Плавное перемещение серва на значение add_angle от начального
 * 
 * input 
 * int add_angle значение откланения угла от начального
 * int stepp=1 шаг движения серва
 * int delayy=0 задержка при движении по умолчанию нулевая
 * 
 */
int MyServoClass::setSlowServo(int add_angle,int stepp=1, int delayy=0){
  int new_angle=0;
  if (add_angle==0)new_angle=_begin_servo;// присваеваем начальное значение
  else new_angle=_begin_servo+add_angle;
  //abs(stepp); не требуется 
  if (new_angle>_global_servo){
    for (int i=_global_servo; i<new_angle; i+=stepp)
    {
        pwm.setPWM(_id, 0, i);
        _global_servo=i;
        delay(delayy);    
    }     
  }
  else if (new_angle<_global_servo){
    for (int i=_global_servo; i>new_angle; i-=stepp)
    {
        pwm.setPWM(_id, 0, i);
        _global_servo=i;
        delay(delayy);    
    }   
  }
    
  Serial.print("ERR global_servo");
  Serial.print(_global_servo);
  Serial.print("add_angle");
  Serial.print(add_angle);
  Serial.print(',');
  Serial.println(' ');

  return _global_servo;

}


  /* 
   *  Быстрое движение серва на задоное значение угла
   *  
   *  input
   *  int new_angle
   *  
   *  return _global_servo
   */
  int MyServoClass::setFastServo(int new_angle){
     pwm.setPWM(_id, 0, new_angle);
     _global_servo= new_angle;
       Serial.print(_id);
       Serial.print(',');
       Serial.println(new_angle);
     return _global_servo;
   }

/*
 * Движение серва
 * 
 * input
 * int new_angle  новое значение угла серва
 * int step  шаг движения серва
 * int delayy  задержка движения серва
 * 
 * output _global_servo
 */
int MyServoClass::getRServo(int new_angle, int stepp, int delayy) {
  if (new_angle>_global_servo){
    for (int i=_global_servo; i<new_angle; i+=stepp)
    {
        pwm.setPWM(_id, 0, i);
        _global_servo=i;
        delay(delayy);    
    }     
  }
  else if (new_angle<_global_servo){
    for (int i=_global_servo; i>new_angle; i-=stepp)
    {
        pwm.setPWM(_id, 0, i);
        _global_servo=i;
        delay(delayy);    
    }   
  }

  return _global_servo;
}

/*
 * Плавное перемещение серва на значение add_angle от начального
 * 
 * input 
 * int add_angle значение откланения угла от начального
 * int stepp=1 шаг движения серва
 * int delayy=0 задержка при движении по умолчанию нулевая
 * 
 */
 int MyServoClass::setTwoSlowServo(int add_angle,int stepp, int delayy, int two, int two_add_angle,  int two_begin_servo, int two_global_servo){
  //if (two >= 0 ){
    int two_val = 0;
    int two_new_angle=0;
    //int two_global_servo=serv_obj[two].getGlobalServo();
      
    if (two_add_angle==0) two_new_angle=two_begin_servo;// присваеваем начальное значение
    else two_new_angle=two_begin_servo+two_add_angle;

  Serial.print("two ");
  Serial.print(two);
  Serial.print(" ");
  Serial.print("two_new_angle ");
  Serial.print(two_new_angle);
  
  Serial.print(" ");
  Serial.print("two_add_angle ");
  Serial.print(two_add_angle);
  Serial.print(" ");
  Serial.print("two_begin_servo ");
  Serial.print(two_begin_servo);
  Serial.print(" ");
  Serial.print("two_global_servo ");
  Serial.println(two_global_servo);
    

  //}


  
  int new_angle=0;
  int old_global_servo=_global_servo;
  if (add_angle==0)new_angle=_begin_servo;// присваеваем начальное значение
  else new_angle=_begin_servo+add_angle;
  if (new_angle>_global_servo){
    for (int val=_global_servo; val<new_angle; val+=stepp)
    {
        pwm.setPWM(_id, 0, val);
        if (two >= 0){
          two_val = map(val, old_global_servo, new_angle, two_global_servo, two_new_angle);
          pwm.setPWM(two, 0, two_val);
        }
        _global_servo=val;
        delay(delayy);
  /*Serial.print("_id");
  Serial.print(_id);
  Serial.print(" ");
  Serial.print("val");
  Serial.println(val);    
  Serial.print(" ");
  Serial.print("two");
  Serial.print(two);
  Serial.print(" ");
  Serial.print("two_val");
  Serial.println(two_val);
  String str="";
  //String str="mappp("+val;
  //str= str+", "+_global_servo+", ";
  str=str+"mappp("+val+", "+old_global_servo+", "+new_angle+", "+two_global_servo+", "+two_new_angle+")";    
  Serial.println(str);    */
    }     
  }
  else if (new_angle<_global_servo){
    for (int val=_global_servo; val>new_angle; val-=stepp)
    {
        pwm.setPWM(_id, 0, val);
        if (two >= 0){
          two_val = map(val, old_global_servo, new_angle, two_global_servo, two_new_angle);
          pwm.setPWM(two, 0, two_val);
        }
        _global_servo=val;
        delay(delayy);    
  /*Serial.print("_id");
  Serial.print(_id);
  Serial.print(" ");
  Serial.print("val");
  Serial.println(val);    
  Serial.print(" ");
  Serial.print("two");
  Serial.print(two);
  Serial.print(" ");
  Serial.print("two_val");
  Serial.println(two_val);    
  String str="";
  str=str+"mappp("+val+", "+old_global_servo+", "+new_angle+", "+two_global_servo+", "+two_new_angle+")";    
  Serial.println(str);    */
    }   
  }
  /*  
  Serial.print("ERR global_servo");
  Serial.print(_global_servo);
  Serial.print("add_angle");
  Serial.print(add_angle);
  Serial.print(',');
  Serial.println(' ');
*/
  return two_new_angle;

}


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  int MyServoClass::setManySlowServo(int a1, int b1, int c1){
  //if (two >= 0 ){
  //  int two_val = 0;
  //  int two_new_angle=0;
    //int two_global_servo=serv_obj[two].getGlobalServo();

    int serv1=serv_obj[a1].getGlobalServo()
  Serial.print("serv1 ");
  Serial.print(two);
  Serial.print(" ");
  Serial.print("two_new_angle ");
  Serial.print(two_new_angle);
    
 /*     
    if (two_add_angle==0) two_new_angle=two_begin_servo;// присваеваем начальное значение
    else two_new_angle=two_begin_servo+two_add_angle;

  Serial.print("two ");
  Serial.print(two);
  Serial.print(" ");
  Serial.print("two_new_angle ");
  Serial.print(two_new_angle);
  
  Serial.print(" ");
  Serial.print("two_add_angle ");
  Serial.print(two_add_angle);
  Serial.print(" ");
  Serial.print("two_begin_servo ");
  Serial.print(two_begin_servo);
  Serial.print(" ");
  Serial.print("two_global_servo ");
  Serial.println(two_global_servo);
    

  //}


  
  int new_angle=0;
  int old_global_servo=_global_servo;
  if (add_angle==0)new_angle=_begin_servo;// присваеваем начальное значение
  else new_angle=_begin_servo+add_angle;
  if (new_angle>_global_servo){
    for (int val=_global_servo; val<new_angle; val+=stepp)
    {
        pwm.setPWM(_id, 0, val);
        if (two >= 0){
          two_val = map(val, old_global_servo, new_angle, two_global_servo, two_new_angle);
          pwm.setPWM(two, 0, two_val);
        }
        _global_servo=val;
        delay(delayy);
*/
        
  /*Serial.print("_id");
  Serial.print(_id);
  Serial.print(" ");
  Serial.print("val");
  Serial.println(val);    
  Serial.print(" ");
  Serial.print("two");
  Serial.print(two);
  Serial.print(" ");
  Serial.print("two_val");
  Serial.println(two_val);
  String str="";
  //String str="mappp("+val;
  //str= str+", "+_global_servo+", ";
  str=str+"mappp("+val+", "+old_global_servo+", "+new_angle+", "+two_global_servo+", "+two_new_angle+")";    
  Serial.println(str);    */
 /*   }     
  }
  else if (new_angle<_global_servo){
    for (int val=_global_servo; val>new_angle; val-=stepp)
    {
        pwm.setPWM(_id, 0, val);
        if (two >= 0){
          two_val = map(val, old_global_servo, new_angle, two_global_servo, two_new_angle);
          pwm.setPWM(two, 0, two_val);
        }
        _global_servo=val;
        delay(delayy);    
  /*Serial.print("_id");
  Serial.print(_id);
  Serial.print(" ");
  Serial.print("val");
  Serial.println(val);    
  Serial.print(" ");
  Serial.print("two");
  Serial.print(two);
  Serial.print(" ");
  Serial.print("two_val");
  Serial.println(two_val);    
  String str="";
  str=str+"mappp("+val+", "+old_global_servo+", "+new_angle+", "+two_global_servo+", "+two_new_angle+")";    
  Serial.println(str);    */
   /* }   
  }
  /*  
  Serial.print("ERR global_servo");
  Serial.print(_global_servo);
  Serial.print("add_angle");
  Serial.print(add_angle);
  Serial.print(',');
  Serial.println(' ');
*/
 return 0;

}





/*
 * обявление сервоприводов
 * 
 * begin_servo начальное положение серва (последнее положение)
 * mini
 * maxi
 * 
 */
MyServoClass serv_obj[17]={
           MyServoClass(0,386,290,586),                  // 1
           MyServoClass(1,366,172,460),                  // 2
           MyServoClass(2,487,280,600),                  // 3
           MyServoClass(3,276,135,488),                  // 4
           MyServoClass(4,444,130,600),                  // 5
           MyServoClass(5,314,130,600),                  // 6
           MyServoClass(6,471,190,600),                  // 7
           MyServoClass(7,312,138,600),                  // 8
           MyServoClass(8,266,130,550),                  // 9
           MyServoClass(9,486,100,600),                  // 10 было 480
           MyServoClass(10,367,130,615),                  // 11 ....
           MyServoClass(11,368,130,615),                  // 12 ....
           MyServoClass(12,491,130,544),                  // 13 ....
           MyServoClass(13,276,224,615),                  // 14 ....
           MyServoClass(14,386,130,615),                  // 15 ....
           MyServoClass(15,406,130,615),                  // 16 ....
           MyServoClass(16,300,130,615)                   // 17 ....
           };               
           
int pos = 0; // обнуление
int one = 0;
int begin_r_arm = 90; // начальная позиция серва
int global_r_arm = begin_r_arm; // глобальная позиция серва на данный момент
int new_arm=0;
int tx_rx; // значение из serial порта
int orient; // выбор направления возварата серва в положение по умолчание
void setup() 
{

    // сервы через i2c
    pwm.begin();                          // Инициализация
    pwm.setPWMFreq(60);                   // Частота следования импульсов 60 Гц
    delay(1000);       

  
  // подключаем сериал порт
  Serial.begin(9600);
  Serial.setTimeout(50); // установить таймаут
}
void loop() {

 
  //блюпуп
  if (Serial.available())
  {
    tx_rx = Serial.read();
 // движение серва сесть
    if ( tx_rx == '0')
    {
      for (int i=0;i<16;i++)
      {
        serv_obj[i].setZeroServo();
      }
    }


    if ( tx_rx == '1')
    {
      int del1=0;
      int delays=10;
                           //serv_obj[14-1].setSlowServo(213,1,delays);       //1. 14 +213(489)(276 0) /\Р> Правая Рука поднять
              //delay(del1);
              //      serv_obj[10-1].setSlowServo(10,1,delays);       //1. нов 10 +10(490)(480 0)/\Т> Таз в право
      delay(del1);
      serv_obj[2-1].setSlowServo(30,1,delays);        //2. 2 +37(403)(366 0)/\С> Правая Ступня наклонить
      delay(del1);
      serv_obj[7-1].setSlowServo(+49,1,delays);        //3. 7 +49(520)(471 0)  <Б/\ Левое Бедро вперед
      delay(del1);

      
  serv_obj[16-1].setGlServo(serv_obj[15-1].setTwoSlowServo(+100,1, 0, 16-1, +100,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo()));     
      
     // serv_obj[15-1].setSlowServo(100,1,10);        //3.++ 15 +100(486)(386 0) <Р\/  Левая Рука назад
     // serv_obj[16-1].setSlowServo(100,1,10);        //3.++ 16 +100(506)(406 0) /\Р> Правая Рука вперёд
                            //      serv_obj[14-1].setSlowServo(0,1,delays);       //4. 14 0(276 0)  @Р> опускаем Правую Руку в 0
                            //      serv_obj[13-1].setSlowServo(-213,1,delays);       //5.1. 13 -213(278)(491 0)  <Р/\ поднемаем Левую Руку
      delay(del1);
      serv_obj[3-1].setSlowServo(-20,1,delays);        //5+нов2 3 -20(467)(487 0) <И\/ Левая Икра назад
      delay(del1);
      serv_obj[2-1].setSlowServo(0,1,delays);        //6. 2  0(366 0)  @С> возвращаем Правую Ступню в 0
              //delay(del1);
              //      serv_obj[10-1].setSlowServo(0,1,delays);        //6.нов 10 0(480 0) @Т>возвращаем Таз в 0
      delay(del1);
      serv_obj[1-1].setSlowServo(-30,1,delays);        //7.2. 1 -37(349)(386 0) <С/\ Левая Ступня наклонить
              // delay(del1);
              //      serv_obj[9-1].setSlowServo(-10,1,delays);        //7. нов 9 -10(256)(266 0) <Т/\ таз в лево
       delay(del1);
 //     serv_obj[3-1].setSlowServo(0,1,delays);       //+нов2 3 0(487 0) <И@ Левая Икра в 0
 //     delay(del1);
 //     serv_obj[7-1].setSlowServo(0,1,delays);        //8. 7 0(471 0) <Б@ возаращаем Левое Бедро в 0
 serv_obj[7-1].setGlServo(serv_obj[3-1].setTwoSlowServo(0,1, 10, 7-1, 0,  serv_obj[7-1].getBegServo(), serv_obj[7-1].getGlobalServo()));     
             //  delay(del1);
              //     serv_obj[15-1].setSlowServo(06,1,delays);        //9.++ 15 0(386 0) <Р@Левая Рука в 0
              //  delay(del1);
              //     serv_obj[16-1].setSlowServo(0,1,delays);        //9.++ 16 0(406 0) @Р>Правая Рукав 0

              /////delay(del1);
      serv_obj[8-1].setSlowServo(-49,1,delays);        //3. 8 -49(263)(312 0) /\Б> Правое Бедро вперед 
      delay(del1);
      //serv_obj[B].setGlServo(serv_obj[A].setTwoSlowServo(A-100,1, 10, B16-1, B-100,  serv_obj[B].getBegServo(), serv_obj[B].getGlobalServo()));
  serv_obj[16-1].setGlServo(serv_obj[15-1].setTwoSlowServo(-100,1, 0, 16-1, -100,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo()));     
//      serv_obj[15-1].setSlowServo(-100,1,1);       //3.++ 15 -100(286)(386 0) <Р/\ Левая Рука вперёд
//      serv_obj[16-1].setSlowServo(-100,1,1);        //3.++ 16 -100(306)(406 0) \/Р> Правая Рука назад
      delay(del1);
                            //        serv_obj[13-1].setSlowServo(0,1,delays);       //4. 13 0(491 0) <Р@ отпускае Левую Руку в 0
                              //        serv_obj[14-1].setSlowServo(213,1,delays);       //5. 14 +213(489)(276 0) /\Р> поднимаем Правую Руку
      serv_obj[4-1].setSlowServo(20,1,delays);        //5.+нов2 4 +20(296)(276 0) \/И>  Правая Икра назад
      delay(del1);
      serv_obj[1-1].setSlowServo(0,1,delays);        //6. 1 0(386 0) <С@ возвращаем Левую Ступню в 0
      delay(del1);
      serv_obj[2-1].setSlowServo(+30,1,delays);        //7. 2 +37(403)(366 0) /\С> Правую Ступню наклонить
              // delay(del1);
               //      serv_obj[9-1].setSlowServo(0,1,delays);        //7.нов 9 0(266 0) <Т@ возвращаем таз в 0
      delay(del1);
//      serv_obj[4-1].setSlowServo(0,1,delays);        //7.+нов2 4 0(276 0) @И>  Правая Икра в 0
//      delay(del1);
//      serv_obj[8-1].setSlowServo(0,1,delays);        //8. 8 0(312 0) @Б> возвращаем Правое Бедро в 0
serv_obj[8-1].setGlServo(serv_obj[4-1].setTwoSlowServo(0,1, 10, 8-1, 0,  serv_obj[8-1].getBegServo(), serv_obj[8-1].getGlobalServo()));     
      delay(del1);
//      serv_obj[15-1].setSlowServo(0,1,delays);        //9.++ 15 0(386 0) <Р@ Левая Рука в 0
//      serv_obj[16-1].setSlowServo(0,1,delays);        //9.++ 16 0(406 0) @Р> Правая Рука в 0
 
   
  /* 
   serv_obj[16-1].setGlServo(serv_obj[15-1].setTwoSlowServo(0,1, 0, 16-1, 0,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo()));
      delay(del1);
                                 //   !!!!      руку с зада возвращаем в бок т.е. 15 в 0
                          //        serv_obj[14-1].setSlowServo(276);       //9. 14 276 @Р> отпускаем Правую Руку в 0
      serv_obj[2-1].setSlowServo(0,1,delays);        //10. 2 0(366 0) @С> Правая Ступня возвращаем в 0
                    //МЫ СТОИМ РОВНО
                    
                    //!но мы возврощаемся положение стоя 0000 левая ступня в 0 и опускаем руку в низ в 0
                    //serv_obj[13-1].setSlowServo(0,1,delays);        //9. 13 0(491 0) отпускаем левую руку в 0
                    //serv_obj[1-1].setSlowServo(0,1,delays);       //10. 1 0(386 0) левая ступня возвращаем в 0
                    //МЫ СТОИМ РОВНО
      delay(del1);
*/



    }

    if ( tx_rx == '2')
    {
     int del1=10;
      int delays=10;
 /*      //serv_obj[15-1].setTwoSlowServo(-100,1, 10, 16-1, -100,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo());
       serv_obj[16-1].setGlServo(serv_obj[15-1].setTwoSlowServo(-100,1, 10, 16-1, -100,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo()));     
*/

      serv_obj[16-1].setGlServo(serv_obj[15-1].setTwoSlowServo(0,1, 0, 16-1, 0,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo()));
      delay(del1);
      serv_obj[2-1].setSlowServo(0,1,delays);        //10. 2 0(366 0) @С> Правая Ступня возвращаем в 0

      delay(del1);

    }
    if ( tx_rx == '3')
    {
      int del1=10;
      int delays=10;
                           //serv_obj[14-1].setSlowServo(213,1,delays);       //1. 14 +213(489)(276 0) /\Р> Правая Рука поднять
              //delay(del1);
              //      serv_obj[10-1].setSlowServo(10,1,delays);       //1. нов 10 +10(490)(480 0)/\Т> Таз в право
      delay(del1);
      serv_obj[2-1].setSlowServo(37,1,delays);        //2. 2 +37(403)(366 0)/\С> Правая Ступня наклонить
      delay(del1);
      serv_obj[7-1].setSlowServo(+49,1,delays);        //3. 7 +49(520)(471 0)  <Б/\ Левое Бедро вперед
      delay(del1);
      serv_obj[15-1].setSlowServo(100,1,1);        //3.++ 15 +100(486)(386 0) <Р\/  Левая Рука назад
      serv_obj[16-1].setSlowServo(100,1,1);        //3.++ 16 +100(506)(406 0) /\Р> Правая Рука вперёд
                            //      serv_obj[14-1].setSlowServo(0,1,delays);       //4. 14 0(276 0)  @Р> опускаем Правую Руку в 0
                            //      serv_obj[13-1].setSlowServo(-213,1,delays);       //5.1. 13 -213(278)(491 0)  <Р/\ поднемаем Левую Руку
      delay(del1);
      serv_obj[3-1].setSlowServo(-20,1,delays);        //5+нов2 3 -20(467)(487 0) <И\/ Левая Икра назад
      delay(del1);
      serv_obj[2-1].setSlowServo(0,1,delays);        //6. 2  0(366 0)  @С> возвращаем Правую Ступню в 0
              //delay(del1);
              //      serv_obj[10-1].setSlowServo(0,1,delays);        //6.нов 10 0(480 0) @Т>возвращаем Таз в 0
      delay(del1);
      serv_obj[1-1].setSlowServo(-37,1,delays);        //7.2. 1 -37(349)(386 0) <С/\ Левая Ступня наклонить
              // delay(del1);
              //      serv_obj[9-1].setSlowServo(-10,1,delays);        //7. нов 9 -10(256)(266 0) <Т/\ таз в лево
       delay(del1);
      serv_obj[3-1].setSlowServo(0,1,delays);       //+нов2 3 0(487 0) <И@ Левая Икра в 0
      delay(del1);
      serv_obj[7-1].setSlowServo(0,1,delays);        //8. 7 0(471 0) <Б@ возаращаем Левое Бедро в 0
              //  delay(del1);
              //     serv_obj[15-1].setSlowServo(06,1,delays);        //9.++ 15 0(386 0) <Р@Левая Рука в 0
              //  delay(del1);
              //     serv_obj[16-1].setSlowServo(0,1,delays);        //9.++ 16 0(406 0) @Р>Правая Рукав 0

              /////delay(del1);
      serv_obj[8-1].setSlowServo(-49,1,delays);        //3. 8 -49(263)(312 0) /\Б> Правое Бедро вперед 
      delay(del1);
      serv_obj[15-1].setSlowServo(-100,1,1);       //3.++ 15 -100(286)(386 0) <Р/\ Левая Рука вперёд
      serv_obj[16-1].setSlowServo(-100,1,1);        //3.++ 16 -100(306)(406 0) \/Р> Правая Рука назад
      delay(del1);
                            //        serv_obj[13-1].setSlowServo(0,1,delays);       //4. 13 0(491 0) <Р@ отпускае Левую Руку в 0
                              //        serv_obj[14-1].setSlowServo(213,1,delays);       //5. 14 +213(489)(276 0) /\Р> поднимаем Правую Руку
      serv_obj[4-1].setSlowServo(20,1,delays);        //5.+нов2 4 +20(296)(276 0) \/И>  Правая Икра назад
      delay(del1);
      serv_obj[1-1].setSlowServo(0,1,delays);        //6. 1 0(386 0) <С@ возвращаем Левую Ступню в 0
      delay(del1);
      serv_obj[2-1].setSlowServo(+37,1,delays);        //7. 2 +37(403)(366 0) /\С> Правую Ступню наклонить
              // delay(del1);
               //      serv_obj[9-1].setSlowServo(0,1,delays);        //7.нов 9 0(266 0) <Т@ возвращаем таз в 0
      delay(del1);
      serv_obj[4-1].setSlowServo(0,1,delays);        //7.+нов2 4 0(276 0) @И>  Правая Икра в 0
      delay(del1);
      serv_obj[8-1].setSlowServo(0,1,delays);        //8. 8 0(312 0) @Б> возвращаем Правое Бедро в 0
      delay(del1);
      serv_obj[15-1].getRServo(0,1,1);        //9.++ 15 0(386 0) <Р@ Левая Рука в 0
      serv_obj[16-1].getRServo(0,1,1);        //9.++ 16 0(406 0) @Р> Правая Рука в 0
      delay(del1);
                                 //   !!!!      руку с зада возвращаем в бок т.е. 15 в 0
                          //        serv_obj[14-1].setSlowServo(276);       //9. 14 276 @Р> отпускаем Правую Руку в 0
      serv_obj[2-1].setSlowServo(0,1,delays);        //10. 2 0(366 0) @С> Правая Ступня возвращаем в 0
                    //МЫ СТОИМ РОВНО
                    
                    //!но мы возврощаемся положение стоя 0000 левая ступня в 0 и опускаем руку в низ в 0
                    //serv_obj[13-1].setSlowServo(0,1,delays);        //9. 13 0(491 0) отпускаем левую руку в 0
                    //serv_obj[1-1].setSlowServo(0,1,delays);       //10. 1 0(386 0) левая ступня возвращаем в 0
                    //МЫ СТОИМ РОВНО
      delay(del1);

    }

    if ( tx_rx == '4')
    {
       int del1=1;
      int delays=10;
                           //serv_obj[14-1].setSlowServo(213,1,delays);       //1. 14 +213(489)(276 0) /\Р> Правая Рука поднять
              //delay(del1);
              //      serv_obj[10-1].setSlowServo(10,1,delays);       //1. нов 10 +10(490)(480 0)/\Т> Таз в право
      delay(del1);
      serv_obj[2-1].setSlowServo(37,1,delays);        //2. 2 +37(403)(366 0)/\С> Правая Ступня наклонить
      delay(del1);
      serv_obj[7-1].setSlowServo(+49,1,delays);        //3. 7 +49(520)(471 0)  <Б/\ Левое Бедро вперед
      delay(del1);
      serv_obj[15-1].setSlowServo(100,1,1);        //3.++ 15 +100(486)(386 0) <Р\/  Левая Рука назад
      serv_obj[16-1].setSlowServo(100,1,1);        //3.++ 16 +100(506)(406 0) /\Р> Правая Рука вперёд
                            //      serv_obj[14-1].setSlowServo(0,1,delays);       //4. 14 0(276 0)  @Р> опускаем Правую Руку в 0
                            //      serv_obj[13-1].setSlowServo(-213,1,delays);       //5.1. 13 -213(278)(491 0)  <Р/\ поднемаем Левую Руку
      delay(del1);
      serv_obj[3-1].setSlowServo(-20,1,delays);        //5+нов2 3 -20(467)(487 0) <И\/ Левая Икра назад
      delay(del1);
      serv_obj[2-1].setSlowServo(0,1,delays);        //6. 2  0(366 0)  @С> возвращаем Правую Ступню в 0
              //delay(del1);
              //      serv_obj[10-1].setSlowServo(0,1,delays);        //6.нов 10 0(480 0) @Т>возвращаем Таз в 0
      delay(del1);
      serv_obj[1-1].setSlowServo(-37,1,delays);        //7.2. 1 -37(349)(386 0) <С/\ Левая Ступня наклонить
              // delay(del1);
              //      serv_obj[9-1].setSlowServo(-10,1,delays);        //7. нов 9 -10(256)(266 0) <Т/\ таз в лево
       delay(del1);
      serv_obj[3-1].setSlowServo(0,1,delays);       //+нов2 3 0(487 0) <И@ Левая Икра в 0
      delay(del1);
      serv_obj[7-1].setSlowServo(0,1,delays);        //8. 7 0(471 0) <Б@ возаращаем Левое Бедро в 0
              //  delay(del1);
              //     serv_obj[15-1].setSlowServo(06,1,delays);        //9.++ 15 0(386 0) <Р@Левая Рука в 0
              //  delay(del1);
              //     serv_obj[16-1].setSlowServo(0,1,delays);        //9.++ 16 0(406 0) @Р>Правая Рукав 0

              /////delay(del1);
      serv_obj[8-1].setSlowServo(-49,1,delays);        //3. 8 -49(263)(312 0) /\Б> Правое Бедро вперед 
      delay(del1);
      serv_obj[15-1].setSlowServo(-100,1,1);       //3.++ 15 -100(286)(386 0) <Р/\ Левая Рука вперёд
      serv_obj[16-1].setSlowServo(-100,1,1);        //3.++ 16 -100(306)(406 0) \/Р> Правая Рука назад
      delay(del1);
                            //        serv_obj[13-1].setSlowServo(0,1,delays);       //4. 13 0(491 0) <Р@ отпускае Левую Руку в 0
                              //        serv_obj[14-1].setSlowServo(213,1,delays);       //5. 14 +213(489)(276 0) /\Р> поднимаем Правую Руку
      serv_obj[4-1].setSlowServo(20,1,delays);        //5.+нов2 4 +20(296)(276 0) \/И>  Правая Икра назад
      delay(del1);
      serv_obj[1-1].setSlowServo(0,1,delays);        //6. 1 0(386 0) <С@ возвращаем Левую Ступню в 0
      delay(del1);
      serv_obj[2-1].setSlowServo(+37,1,delays);        //7. 2 +37(403)(366 0) /\С> Правую Ступню наклонить
              // delay(del1);
               //      serv_obj[9-1].setSlowServo(0,1,delays);        //7.нов 9 0(266 0) <Т@ возвращаем таз в 0
      delay(del1);
      serv_obj[4-1].setSlowServo(0,1,delays);        //7.+нов2 4 0(276 0) @И>  Правая Икра в 0
      delay(del1);
      serv_obj[8-1].setSlowServo(0,1,delays);        //8. 8 0(312 0) @Б> возвращаем Правое Бедро в 0
      delay(del1);
      serv_obj[15-1].getRServo(0,1,1);        //9.++ 15 0(386 0) <Р@ Левая Рука в 0
      serv_obj[16-1].getRServo(0,1,1);        //9.++ 16 0(406 0) @Р> Правая Рука в 0
      delay(del1);
                                 //   !!!!      руку с зада возвращаем в бок т.е. 15 в 0
                          //        serv_obj[14-1].setSlowServo(276);       //9. 14 276 @Р> отпускаем Правую Руку в 0
      serv_obj[2-1].setSlowServo(0,1,delays);        //10. 2 0(366 0) @С> Правая Ступня возвращаем в 0
                    //МЫ СТОИМ РОВНО
                    
                    //!но мы возврощаемся положение стоя 0000 левая ступня в 0 и опускаем руку в низ в 0
                    //serv_obj[13-1].setSlowServo(0,1,delays);        //9. 13 0(491 0) отпускаем левую руку в 0
                    //serv_obj[1-1].setSlowServo(0,1,delays);       //10. 1 0(386 0) левая ступня возвращаем в 0
                    //МЫ СТОИМ РОВНО
      delay(del1);

    }

     if ( tx_rx == '5')
    {
         serv_obj[10-1].setFastServo(491);
         serv_obj[2-1].setFastServo(402);
         delay(1000);       
         serv_obj[7-1].setFastServo(530);
         serv_obj[4-1].setFastServo(213);
         delay(1000); 
         serv_obj[10-1].setFastServo(480);
         serv_obj[2-1].setFastServo(366);
         delay(1000);       
         serv_obj[7-1].setFastServo(500);
         serv_obj[4-1].setFastServo(276);

    }

    if ( tx_rx == '6')
    {
         serv_obj[9-1].setFastServo(255);
         serv_obj[1-1].setFastServo(360);
         delay(1000);       
         serv_obj[8-1].setFastServo(245);
         serv_obj[3-1].setFastServo(530);
         delay(1000); 
         serv_obj[9-1].setFastServo(266);
         serv_obj[1-1].setFastServo(386);
         delay(1000);       
         serv_obj[8-1].setFastServo(298);
         serv_obj[3-1].setFastServo(512);


    }
    if ( tx_rx == '7')
    {
         serv_obj[10-1].setFastServo(491);
         serv_obj[2-1].setFastServo(402);
         delay(1000);       
         serv_obj[7-1].setFastServo(530);
         serv_obj[4-1].setFastServo(213);
         delay(1000); 
         serv_obj[10-1].setFastServo(480);
         serv_obj[2-1].setFastServo(366);
         delay(1000);       
         serv_obj[7-1].setFastServo(500);
         serv_obj[4-1].setFastServo(276);
         
          delay(1000);
         serv_obj[9-1].setFastServo(255);
         serv_obj[1-1].setFastServo(360);
         delay(1000);       
         serv_obj[8-1].setFastServo(245);
         serv_obj[3-1].setFastServo(530);
         delay(1000); 
         serv_obj[9-1].setFastServo(266);
         serv_obj[1-1].setFastServo(386);
         delay(1000);       
         serv_obj[8-1].setFastServo(298);
         serv_obj[3-1].setFastServo(512);


    }    
    if ( tx_rx == '8')
    {
       for (int i=0;i<10;i++)
      {
         serv_obj[10-1].setFastServo(491);
         serv_obj[2-1].setFastServo(402);
         delay(100);       
         serv_obj[7-1].setFastServo(530);
         serv_obj[4-1].setFastServo(213);
         delay(100); 
         serv_obj[10-1].setFastServo(480);
         serv_obj[2-1].setFastServo(366);
         delay(100);       
         serv_obj[7-1].setFastServo(500);
         serv_obj[4-1].setFastServo(276);
         
          delay(100);
         serv_obj[9-1].setFastServo(255);
         serv_obj[1-1].setFastServo(360);
         delay(100);       
         serv_obj[8-1].setFastServo(245);
         serv_obj[3-1].setFastServo(530);
         delay(100); 
         serv_obj[9-1].setFastServo(266);
         serv_obj[1-1].setFastServo(386);
         delay(100);       
         serv_obj[8-1].setFastServo(298);
         serv_obj[3-1].setFastServo(512);
        delay(100);       

      }
    }
    if ( tx_rx == '9')
    {
    int del1=1000;
      int delays=10;
                           //serv_obj[14-1].setSlowServo(213,1,delays);       //1. 14 +213(489)(276 0) /\Р> Правая Рука поднять
              //delay(del1);
              //      serv_obj[10-1].setSlowServo(10,1,delays);       //1. нов 10 +10(490)(480 0)/\Т> Таз в право
      delay(del1);
      serv_obj[2-1].setSlowServo(37,1,delays);        //2. 2 +37(403)(366 0)/\С> Правая Ступня наклонить
      delay(del1);
      serv_obj[7-1].setSlowServo(+49,1,delays);        //3. 7 +49(520)(471 0)  <Б/\ Левое Бедро вперед
      delay(del1);

      
      serv_obj[16-1].setGlServo(serv_obj[15-1].setTwoSlowServo(+100,1, 10, 16-1, +100,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo()));     
      
     // serv_obj[15-1].setSlowServo(100,1,10);        //3.++ 15 +100(486)(386 0) <Р\/  Левая Рука назад
     // serv_obj[16-1].setSlowServo(100,1,10);        //3.++ 16 +100(506)(406 0) /\Р> Правая Рука вперёд
                            //      serv_obj[14-1].setSlowServo(0,1,delays);       //4. 14 0(276 0)  @Р> опускаем Правую Руку в 0
                            //      serv_obj[13-1].setSlowServo(-213,1,delays);       //5.1. 13 -213(278)(491 0)  <Р/\ поднемаем Левую Руку
      delay(del1);
      serv_obj[3-1].setSlowServo(-20,1,delays);        //5+нов2 3 -20(467)(487 0) <И\/ Левая Икра назад
      delay(del1);
      serv_obj[2-1].setSlowServo(0,1,delays);        //6. 2  0(366 0)  @С> возвращаем Правую Ступню в 0
              //delay(del1);
              //      serv_obj[10-1].setSlowServo(0,1,delays);        //6.нов 10 0(480 0) @Т>возвращаем Таз в 0
      delay(del1);
      serv_obj[1-1].setSlowServo(-37,1,delays);        //7.2. 1 -37(349)(386 0) <С/\ Левая Ступня наклонить
              // delay(del1);
              //      serv_obj[9-1].setSlowServo(-10,1,delays);        //7. нов 9 -10(256)(266 0) <Т/\ таз в лево
       delay(del1);
      serv_obj[3-1].setSlowServo(0,1,delays);       //+нов2 3 0(487 0) <И@ Левая Икра в 0
      delay(del1);
      serv_obj[7-1].setSlowServo(0,1,delays);        //8. 7 0(471 0) <Б@ возаращаем Левое Бедро в 0
              //  delay(del1);
              //     serv_obj[15-1].setSlowServo(06,1,delays);        //9.++ 15 0(386 0) <Р@Левая Рука в 0
              //  delay(del1);
              //     serv_obj[16-1].setSlowServo(0,1,delays);        //9.++ 16 0(406 0) @Р>Правая Рукав 0

              /////delay(del1);
      serv_obj[8-1].setSlowServo(-49,1,delays);        //3. 8 -49(263)(312 0) /\Б> Правое Бедро вперед 
      delay(del1);
      //serv_obj[B].setGlServo(serv_obj[A].setTwoSlowServo(A-100,1, 10, B16-1, B-100,  serv_obj[B].getBegServo(), serv_obj[B].getGlobalServo()));
      serv_obj[16-1].setGlServo(serv_obj[15-1].setTwoSlowServo(-100,1, 10, 16-1, -100,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo()));     
//      serv_obj[15-1].setSlowServo(-100,1,1);       //3.++ 15 -100(286)(386 0) <Р/\ Левая Рука вперёд
//      serv_obj[16-1].setSlowServo(-100,1,1);        //3.++ 16 -100(306)(406 0) \/Р> Правая Рука назад
      delay(del1);
                            //        serv_obj[13-1].setSlowServo(0,1,delays);       //4. 13 0(491 0) <Р@ отпускае Левую Руку в 0
                              //        serv_obj[14-1].setSlowServo(213,1,delays);       //5. 14 +213(489)(276 0) /\Р> поднимаем Правую Руку
      serv_obj[4-1].setSlowServo(20,1,delays);        //5.+нов2 4 +20(296)(276 0) \/И>  Правая Икра назад
      delay(del1);
      serv_obj[1-1].setSlowServo(0,1,delays);        //6. 1 0(386 0) <С@ возвращаем Левую Ступню в 0
      delay(del1);
      serv_obj[2-1].setSlowServo(+37,1,delays);        //7. 2 +37(403)(366 0) /\С> Правую Ступню наклонить
              // delay(del1);
               //      serv_obj[9-1].setSlowServo(0,1,delays);        //7.нов 9 0(266 0) <Т@ возвращаем таз в 0
      delay(del1);
      serv_obj[4-1].setSlowServo(0,1,delays);        //7.+нов2 4 0(276 0) @И>  Правая Икра в 0
      delay(del1);
      serv_obj[8-1].setSlowServo(0,1,delays);        //8. 8 0(312 0) @Б> возвращаем Правое Бедро в 0
      delay(del1);
//      serv_obj[15-1].setSlowServo(0,1,delays);        //9.++ 15 0(386 0) <Р@ Левая Рука в 0
//      serv_obj[16-1].setSlowServo(0,1,delays);        //9.++ 16 0(406 0) @Р> Правая Рука в 0
      serv_obj[16-1].setGlServo(serv_obj[15-1].setTwoSlowServo(0,1, 10, 16-1, 0,  serv_obj[16-1].getBegServo(), serv_obj[16-1].getGlobalServo()));
      delay(del1);
                                 //   !!!!      руку с зада возвращаем в бок т.е. 15 в 0
                          //        serv_obj[14-1].setSlowServo(276);       //9. 14 276 @Р> отпускаем Правую Руку в 0
      serv_obj[2-1].setSlowServo(0,1,delays);        //10. 2 0(366 0) @С> Правая Ступня возвращаем в 0
                    //МЫ СТОИМ РОВНО
                    
                    //!но мы возврощаемся положение стоя 0000 левая ступня в 0 и опускаем руку в низ в 0
                    //serv_obj[13-1].setSlowServo(0,1,delays);        //9. 13 0(491 0) отпускаем левую руку в 0
                    //serv_obj[1-1].setSlowServo(0,1,delays);       //10. 1 0(386 0) левая ступня возвращаем в 0
                    //МЫ СТОИМ РОВНО
      delay(del1);



      
    }

    
  }
  delay(100);
}
