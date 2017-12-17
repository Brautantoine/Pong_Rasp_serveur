#!/usr/bin/python

from turtle import *
import time

reset()

try:
	listen()
	speed(10)
	right(90)
	forward(50)
	circle(50)
	time.sleep(0.5)
	home()
	right(90)
	forward(150)
	circle(150)
	time.sleep(0.5)
	home()
	right(90)
	forward(200)
	circle(200)
	mainloop()

finally:
	bye()
