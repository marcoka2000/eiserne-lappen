from gpiozero import Button
from gpiozero import LED
from time import sleep
import cups

button = Button(2)
led = LED(17)

conn = cups.Connection()
printer_name = 'MFCL2710DN'

for x in range(0, 3):
    led.on()
    sleep(0.5)
    led.off()

while True:
    button.wait_for_press()

    conn.printFile(printer_name, '/home/pi/eiserne-lappen/white.png', ' ', {}))
    print('Push, Push!')
    led.on()
    sleep(1)
    led.off()