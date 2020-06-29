import socket
import time
import select
import keyboard

LISTEN_IP = ""
RCV_PORT = 8081
sockrcv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockrcv.bind((LISTEN_IP, RCV_PORT))

#sockrcv.settimeout(0)
while True:
    try:
        
        data, addr = sockrcv.recvfrom(1024) # buffer size is 1024 bytes
       
        
        tmp = data.decode("utf-8")
        print(tmp)
        if tmp == "Y+":
            keyboard.press('up')
        if tmp == "STOPY+":
            keyboard.release('up')
        
        if tmp == "Y-":
            keyboard.press('down')
        if tmp == "STOPY-":
            keyboard.release('down')
        
        if tmp == "X-":
            keyboard.press('left')
        if tmp == "STOPX-":
            keyboard.release('left')
            
        if tmp == "X+":
            keyboard.press('right')
        if tmp == "STOPX+":
            keyboard.release('right')
        
        if tmp == "Z+":
            keyboard.press('page up')
        if tmp == "STOPZ+":
            keyboard.release('page up')
            
        if tmp == "Z-":
            keyboard.press('page down')
        if tmp == "STOPZ-":
            keyboard.release('page down')
            
        if tmp == "X0":
            keyboard.press_and_release('alt+x')
        if tmp == "Y0":
            keyboard.press_and_release('alt+y')
        if tmp == "Z0":
            keyboard.press_and_release('alt+z')
            
        if tmp == "HOME":
            keyboard.press_and_release('ctrl+home')
        if tmp == "ZPROBE":
            keyboard.press_and_release('F4')
        if tmp == "RESET":
            keyboard.press_and_release('space')
            
        if tmp == "PLAY":
            keyboard.press_and_release('alt+r')
        if tmp == "PAUSE":
            keyboard.press_and_release('alt+p')
        if tmp == "STOP":
            keyboard.press_and_release('alt+s')
        
    except KeyboardInterrupt:
        print("End")
        # If you actually want the program to exit
        raise
             