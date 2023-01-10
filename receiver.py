import serial
import datetime
import time
import os

arduino_port = "COM4"
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)
print("Connected to Arduino port: " + arduino_port)

print(str(ser.readline())[2:][:-3])

while True:
    pot1 = str(ser.readline())[2:][:-5]

    pot2 = str(ser.readline())[2:][:-5]

    stick_x1 = str(ser.readline())[2:][:-5]
    stick_y1 = str(ser.readline())[2:][:-5]

    stick_x2 = str(ser.readline())[2:][:-5]
    stick_y2 = str(ser.readline())[2:][:-5]

    string_to_print = f"Potentiometer 1 Value: {pot1}" + "\t" + f"Potentiometer 2 Value: {pot2}" + "\t" + \
        f"Stick 1 (x,y): ({stick_x1},{stick_y1})" + "\t" + \
        f"Stick 2 (x,y): ({stick_x2},{stick_y2})"

    #os.system("cls")

    print(string_to_print)



