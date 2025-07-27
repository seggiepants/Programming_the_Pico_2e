from machine import Pin
from utime  import sleep

led = Pin('LED', Pin.OUT)

def dot(led):
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    
def dash(led):
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)

while True:
    # S
    for i in range(3):
        dot(led)
    sleep(0.4)

    # O
    for i in range(3):
        dash(led)
