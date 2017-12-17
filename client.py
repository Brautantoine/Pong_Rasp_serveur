#!usr/bin/python

from sense_hat import *
import socket


TCP_IP = '192.168.0.182'
TCP_PORT = 4242
BUFFER_SIZE = 1
Y = 0

sense = SenseHat()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while 1:
	Y = s.recv(BUFFER_SIZE)
	sense.clear()
	sense.set_pixel(4,Y,42,42,180)
s.close()
