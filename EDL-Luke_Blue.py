import pyfirmata
import time

board = pyfirmata.Arduino('/dev/tnt0')


board = pyfirmata.Arduino('/dev/tnt0')

while True:
    board.digital[13].write(1)
    time.sleep(0.5)
    board.digital[13].write(0)
    time.sleep(0.5)


from components import UltrasonicSensor, LED
from time import sleep

#If your kit doesn't automtically detect the port being used, you can specify
ultrasonic = UltrasonicSensor("SR04-15")board.digital[9][10]


while True:
    distance = ultrasonic.distance
    print(distance)
    sleep(0.1)


red_led = LED("Led-12")board.digital[5]
orange_led = LED("Led11")board.digital[6]
green_led = LED("Led-10")board.digital[7]

if distance < 100:
    red_led.on()
    yellow_led.on()
    green_led.on()
elif distance < 50:
    red_led.off()
    yellow_led.on()
    green_led.on()
else:
    red_led.off()
    yellow_led.off()
    green_led.on()
