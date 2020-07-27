import minimalmodbus
import serial
import time

instrument = minimalmodbus.Instrument('com25',  1)  #, debug = True
instrument.serial.bytesize = 8
instrument.serial.baudrate = 9600
instrument.serial.stopbits = 1
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.timeout = 1

instrument.write_bit(0, False) #set relay 0 off
instrument.write_bit(1, False) #set relay 1 off

instrument.write_bit(0, True)  #set relay 0 on
instrument.write_bit(1, True)  #set relay 1 on

# reading does not seem to work correctly
print(instrument.read_bit(0, functioncode=1))
print(instrument.read_bit(1, functioncode=1))

instrument.serial.close()