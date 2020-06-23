import minimalmodbus
import serial
import time
import datetime

now = datetime.datetime.now()

# data1 = b'\xFF\x05\x00\x00\xFF\x00\x99\xE4'
# data1 = b'\xFF\x05\x00\x01\xFF\x00\xC8\x24'
# data1 = b'\x01\x05\x00\x01\x01\x00\x9d\x9a' #atsako
# data1 = b'\x01\x05\x00\x00\xFF\x00\x8C\x3A' #relay 1 on
# data1 = b'\x01\x05\x00\x01\xFF\x00\xDD\xFA'  #relay 2 on

# instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('com25',  0, debug = True) # port name, slave address (in decimal)
instrument.serial.bytesize = 8
instrument.serial.baudrate = 9600
instrument.serial.stopbits = 1
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.timeout = 1
print(instrument.serial)

#
# instrument.serial.timeout = 1
time.sleep(1)
#
a = instrument.read_register(0x0000, functioncode=3)
print(a)
# instrument.write_bit(0, True)
# instrument.write_bit(1, True)
# instrument.write_bit(, True)
# a1 = instrument.read_bit(1)
# print(a1)

# instrument.write_register(1,1, functioncode=5)

# pv1_voltage = instrument.read_register(0, functioncode=4)
# print(pv1_voltage)