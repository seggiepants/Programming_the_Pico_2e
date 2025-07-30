from machine import Pin, PWM
from utime import sleep

frequency = 60
duty = 8192
red_ch = PWM(Pin(16, Pin.OUT), freq=frequency, duty_u16=duty)
green_ch = PWM(Pin(17, Pin.OUT), freq=frequency, duty_u16=duty)
blue_ch = PWM(Pin(15, Pin.OUT), freq=frequency, duty_u16=duty)

button = Pin(12, Pin.IN, Pin.PULL_UP)
colors = [[255, 0, 0],
          [127, 127, 0],
          [0, 255, 0],
          [0, 127, 127],
          [0, 0, 255],
          [127, 0, 127]]

def set_color(rgb):
    red_ch.duty_u16(rgb[0] * 255)
    green_ch.duty_u16(rgb[1] * 255)
    blue_ch.duty_u16(rgb[2] * 255)
    
index = 0
set_color(colors[index])
#set_color([255, 127, 127])

while True:
    if button.value() == 0:
        print('click')
        index += 1
        if index >= len(colors):
            index = 0
        set_color(colors[index])
        sleep(0.5)