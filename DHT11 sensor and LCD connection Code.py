import sys 
import Adafruit_CharLCD as LCD  
import Adafruit_DHT 


lcd = LCD.Adafruit_CharLCD(lcd_rs=7, lcd_en=8, lcd_d4=25, lcd_d5=24, lcd_d6=23, lcd_d7=18, lcd_columns=16, lcd_rows=2, lcd_backlight=0)   

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}* Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. try again!')
    sys.exit(1)     