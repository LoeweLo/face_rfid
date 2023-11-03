from mfrc522 import  MFRC522
from machine import  Pin, PWM,UART
import utime
from time import sleep

pwm = PWM(Pin(28))
pwm.freq(2500)
pwm.duty_u16(65535)
green_led = Pin(14, Pin.OUT)
red_led = Pin(15, Pin.OUT)
# Set up UART communication
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))  # Use UART0 with pins GP0 (RX) and GP1 (TX)

#將卡號由2進為轉換為16進位的字串
def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    mystring=mystring+'\n'    
    return mystring

reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=10, rst=26)
print(".....請將卡片靠近感應器.....")
prev_card_num=None
card_num=''
flag_supression=True
i=0
try :
    while True :
        
        
       
                            
        (stat, tag_type) = reader.request(reader.REQIDL)   #搜尋RFID卡片
        if stat == reader.OK:   #找到卡片
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK :
                card_num = uidToString(uid)
                
                if  prev_card_num!=card_num or flag_supression==False : 
                    flag_supression=True
                    print(".....卡片號碼: %s" % card_num)
                    uart.write(card_num.encode('utf-8'))        
                else:
                    i+=1
                    if i >=2:
                        flag_supression=False
                        i=0
                
                prev_card_num=card_num
        
        utime.sleep_ms(500)
                
                

                
except  KeyboardInterrupt:
    print(".....Bye.....")
