import minimalmodbus
import serial
import time

instrument = minimalmodbus.Instrument(port='com25',  slaveaddress=1, debug = True)  #
instrument.serial.bytesize = 8
instrument.serial.baudrate = 9600
instrument.serial.stopbits = 1
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.timeout = 1

instrument.write_bit(0, False) #set relay 0 off
instrument.write_bit(1, False) #set relay 1 off

instrument.write_bit(0, True)  #set relay 0 on
instrument.write_bit(1, True)  #set relay 1 on

# reading does not seem to work well
print(instrument.read_bit(registeraddress=0, functioncode=1))
print(instrument.read_bit(registeraddress=1, functioncode=1))

# blink
instrument._perform_command(5, '\x02\x00\x07\x00') # custom command to blink 700ms relay 0
instrument._perform_command(5, '\x02\x01\x06\x00') # custom command to blink 600ms relay 1

# flip
instrument._perform_command(5, '\x00\x00\x55\x00') # flip status relay 0
instrument._perform_command(5, '\x00\x01\x55\x00') # flip status relay 1

# all flip
instrument._perform_command(5, '\x00\x00\x5A\x00') # flip all

# all relays on/off
instrument._perform_command(0x0F, '\x00\x00\x00\x08\x01\x00') # flip status relay 1
instrument._perform_command(0x0F, '\x00\x00\x00\x08\x01\xFF') # flip status relay 1

# Read all interfaces input status
# NOTE: reads status of pins In1 and In2 - not relay status
instrument._perform_command(2, '\x00\x00\x00\x08') # flip status relay 1


# Read No. 0 relay status: 01 01 00 00 00 01 FD CA
# not sure it works
instrument._perform_command(1, '\x00\x00\x00\x01') # flip status relay 1
instrument._perform_command(1, '\x00\x01\x00\x01') # flip status relay 1
# 01 01 00 00 00 01 FD CA