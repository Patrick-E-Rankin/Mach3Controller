import socket
import time

UDP_IP = "192.168.29.164"
UDP_PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
        try:   
            f = open('c:\python\coordinates.txt', 'r')
            dataA = f.readline()
            dataA = dataA.rstrip('\n')
            data1 = dataA[:30]
            message = data1.encode('utf-8')
            sock.sendto(message, (UDP_IP, UDP_PORT))
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("End")
            # If you actually want the program to exit
            raise


            

