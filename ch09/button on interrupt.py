from machine import Pin
from utime import sleep

button = Pin(12, Pin.IN, Pin.PULL_UP)

def handle_button(ignore):
    print('Button pressed.')
    
button.irq(handle_button, Pin.IRQ_FALLING)
i = 0

while True:
    i += 1
    print(i)
    sleep(0.2)

