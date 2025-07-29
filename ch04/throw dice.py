from machine import Pin
from utime import sleep
from random import randint

led = Pin('LED', Pin.OUT)

def throw_dice(num_dice=1):
    total = 0
    for i in range(num_dice):
        total += randint(1, 6)
    return total

def blink(times, delay):
    for x in range(1, times + 1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    input()
    dice_throw = throw_dice()
    print(dice_throw)
    blink(dice_throw, 0.2)
    
    
    