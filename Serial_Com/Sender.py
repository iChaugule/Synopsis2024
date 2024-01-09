#!/usr/bin/env python
import time
import serial

ser = serial.Serial( port='/dev/ttyACM0', baudrate = 9600, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial Ready")

ser.write("reverse\n".encode('utf-8'))

while(ser.in_waiting == 0):
    time.sleep(.1)

response = ser.readline().decode('utf-8').rstrip()

print(response)