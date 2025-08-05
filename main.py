# Alle benötigten Imports
from gpiozero import Button, LED
from time import sleep
import cups


# Setup der Umgebung & Pins
button = Button(2)
led = LED(17)

# Setup des Druckers, hier bei printer_name den Druckernamen aus CUPS eintragen
conn = cups.Connection()
printer_name = 'MFCL2710DN'


# 3mal Blinken der LED, damit man weiß dass es betriebsbereit ist
for x in range(0, 3):
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

# Endlosschleife wartet auf Betätigung des Buttons
while True:
    button.wait_for_press()

    # Druckt leeres PNG und gibt auf der Konsole eine Rückmeldung
    conn.printFile(printer_name, '/home/pi/eiserne-lappen/assets/white.png', ' ', {})
    print('Push, Push!')

    # LED gibt Rückmeldung, damit man weiß dass das Script noch ordnungsgemäß läuft
    led.on()
    sleep(1)
    led.off()