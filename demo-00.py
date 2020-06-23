import minimalmodbus
import serial
import time
import datetime

now = datetime.datetime.now()

# data1 = b'\xFF\x05\x00\x00\xFF\x00\x99\xE4'
# data1 = b'\xFF\x05\x00\x01\xFF\x00\xC8\x24'
# data1 = b'\x01\x05\x00\x01\x01\x00\x9d\x9a' #atsako
# data1 = b'\x01\x05\x00\x00\xFF\x00\x8C\x3A' #relay 1 on
data1 = b'\x01\x05\x02\x00\x07\x00\xCE\x42' #flash for 700 ms

ser = serial.Serial('com25', baudrate = 9600, bytesize = 8, stopbits = 1, parity = serial.PARITY_NONE)

ser.write(data1)

while True:
    print(ser.read(1))