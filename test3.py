#Include the library files
import I2C_LCD_driver
from time import sleep
from gpiozero import DistanceSensor

# Create a object for the LCD
lcd = I2C_LCD_driver.lcd()

ultrasonic = DistanceSensor(echo=17,trigger=27)

# Starting text
lcd.lcd_display_string("Digital Ruler",1,2)


for a in range (0,16):
    lcd.lcd_display_string(".",2,a)
    sleep(0.2)
lcd.lcd_clear()

lcd.lcd_display_string("Wait..",1,0)

def Distance():
    value = ultrasonic.distance # Get the distance
    cm = int(value*100) # Convert to CM
    
    
    lcd.lcd_display_string("Distance :",1,0)
    lcd.lcd_display_string(str(cm)+"CM ",1,10)
    
    A = "STOP"
    B = "GO"
     # نقوم بتعديل الدالة الشرطية لتتكامل مع الريبوت بحيث في حالة وجود حاجز على بعد 20سم يقف الريبوت
    if cm <= 20 :
        lcd.lcd_display_string(A,2,0)
        lcd.lcd_display_string("  ",2,6)
    else :
        lcd.lcd_display_string(B,2,6)
        lcd.lcd_display_string("    ",2,0)
    # نقوم بتعديل الكود بحيث في حالة وجود حاجز يقوم الربوت بالوقوف

    
    print(value)
    sleep(0.05)

while True:
    Distance()


