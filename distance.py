#Import the library files
from i2c_lcd import I2cLcd
from lcd_api import LcdApi
from machine import Pin,I2C
import time

Trig = Pin(2,Pin.OUT)#Include the Trig pin
Echo = Pin(3,Pin.IN)#Include the Echo pin

i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)#Include the I2C pins
I2C_ADDR = i2c.scan()[0]#Scan I2C addres
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)#Initialize the I2C module

#Get the distance
def distance():
    Trig.value(0)
    time.sleep_us(4)
    Trig.value(1)
    time.sleep_us(10)
    Trig.value(0)
      
    while Echo.value() == 0:
       low = time.ticks_us()
       
    while Echo.value() == 1:
       high = time.ticks_us()
       
    t = high - low
    return t

#Start text
def startText():
    lcd.move_to(0,0)  
    lcd.putstr("Distance Loading")
    for i in range(0,15):
        lcd.move_to(i,1)
        lcd.putstr(".")
        time.sleep(0.3)
        
startText()#Start text
lcd.clear()#Clear the display

while True:
    dis = distance()#Get the distance
    cm = dis/29/2#Time convert to the cm
    cm = int(cm)
    inch = dis/74/2#Time convert to the inch
    inch = int(inch)
    
    lcd.move_to(0,0)#Set the cursor
    lcd.putstr("Distance - ")
    lcd.putstr(str(cm)+ "cm ")#Print the distance
    
    lcd.move_to(0,1)
    lcd.putstr("Distance - ")
    lcd.putstr(str(inch)+ "inch ")
    
   
    
    
    

