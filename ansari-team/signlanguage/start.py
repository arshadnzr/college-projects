import RPi.GPIO as GPIO 
#import lcddriver
from time import * 

#lcd = lcddriver.lcd()
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN) 
#lcd.lcd_display_string("       PROJECT", 1)
#lcd.lcd_display_string("An Electronic Assistant", 2)
#lcd.lcd_display_string("   For Deaf-Mute", 3)
sleep(3)
#lcd.lcd_clear()


while True:
    button_state=GPIO.input(10) 
    if(button_state==0):
        print("Gesture Mode")
        import set_hand_hist
        #lcd.lcd_clear()
        #lcd.lcd_display_string("   Gesture mode", 2)
        #lcd.lcd_display_string("       Activated", 3)
        sleep(2)
        #lcd.lcd_clear()
        import fun_util
        fun_util.recognize()
    else:
        print("Speach Mode")
        #lcd.lcd_clear()
        #lcd.lcd_display_string("   Speech mode", 2)
        #lcd.lcd_display_string("       Activated", 3)
        sleep(2)
        #lcd.lcd_clear() 
        import speach 
        speech.rec()