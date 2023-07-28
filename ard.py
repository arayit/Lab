import serial

arduino = serial.Serial(port='/dev/tty.usbserial-10', baudrate=115200, timeout=.1)

while True:
    x = input()
    arduino.write(bytes(x, 'utf-8'))