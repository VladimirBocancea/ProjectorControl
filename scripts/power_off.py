#!/usr/bin/env python
#turn Power Off
import sys
import serial


port = serial.Serial('/dev/ttyAMA0', baudrate=38400, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=5)
port.open
#this is the code sent to the projector.  Replace it for your model
port.write("\x02\x01\x00\x00\x00\x03")
received = port.read(8)
print received # newline is printed
port.close
