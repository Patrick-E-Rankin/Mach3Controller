#https://github.com/Patrick-E-Rankin/Mach3-Controller
import socket
import time

UDP_IP = "192.168.29.255" #we are sending it to the broadcast address, change this to your devices ip or just take your regular ip address and change last 3 digits to 255
UDP_PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
        try:   
            f = open('c:\python\coordinates.txt', 'r') #you can make this whatever folder Mach3 saves the coordinates to
            dataA = f.readline()
            dataA = dataA.rstrip('\n')
            data1 = dataA[:30] #should probably change this to 24
            message = data1.encode('utf-8') #we need to encode this to send over UDP
            sock.sendto(message, (UDP_IP, UDP_PORT))
            time.sleep(0.1) #every 100ms is fast enough
        except KeyboardInterrupt:
            print("End")
            # If you actually want the program to exit
            raise


            

