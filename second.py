# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 15:22:37 2023

@author: camer
"""

import time
import serial

ser = serial.Serial('COM12',9600)
while 1:
    try:
        file = open('test1.txt')
        line = file.readline()
        ser.write(line)
        file.close()
        time.sleep(3)
    except:
        time.sleep(.2)