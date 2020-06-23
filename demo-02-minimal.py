import minimalmodbus
import serial
import time

instrument = minimalmodbus.Instrument('com25',  1)  #, debug = True
instrument.serial.bytesize = 8
instrument.serial.baudrate = 9600
instrument.serial.stopbits = 1
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.timeout = 1

instrument.write_bit(0, False)
# instrument.write_bit(1, True)

# print(instrument.read_bit(0, functioncode=1))
# while True:
#     print(instrument.read_bit(0, functioncode=1))
#     time.sleep(0.1)
#     print(instrument.read_bit(1, functioncode=1))
#     time.sleep(0.1)
# print(instrument.read_bit(2, functioncode=1))
#
# instrument.write_bit(0x0200, 0x0700)


instrument.serial.close()