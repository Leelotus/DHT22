from bluetooth import *
import Adafruit_DHT as dht
from time import sleep

DHT = 4

server_socket= BluetoothSocket(RFCOMM)

port = 1
server_socket.bind(("", port))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print("Accepted connection from ", address)

while True:
    #Read Temp and Hum from DHT22
    h,t = dht.read_retry(dht.DHT22, DHT)
    #Print Temperature and Humidity on Shell window
    client_socket.send('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t,h))
    sleep(5) #Wait 5 seconds and read again


while True:
    data = client_socket.recv(1024)
    print("Received: %s" %data)
    if(data=="q"):
        print("Quit")
        break

client_socket.close()
server_socket.close()