import serial
import io
import smtplib
import winsound
import datetime

ser = serial.Serial('COM7', 9600, timeout=5)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
hello = sio.readline()
fo = open("logs.txt", "w")

try:
    while True:
        while (hello == "ok\n"):
            print hello
            hello = sio.readline()
        while (hello == "nk\n"):
            winsound.Beep(3000,1000)
            timenow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
            jsonn = "{'Pacient':'Mitica','Time':'"
            jsonn += timenow
            jsonn += "'}\n"
            fo.write(jsonn)
            
except KeyboardInterrupt:
    print 'interrupted!'
    ser.close()
    fo.close()

