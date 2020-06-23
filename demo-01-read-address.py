import minimalmodbus
import serial

instrument = minimalmodbus.Instrument('com25',  0, debug = True) #note 0 as broadcast adress
instrument.serial.bytesize = 8
instrument.serial.baudrate = 9600
instrument.serial.stopbits = 1
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.timeout = 1

address = instrument.read_register(0x0000, functioncode=3)
print(f"device address is {address}")

instrument.serial.close()
