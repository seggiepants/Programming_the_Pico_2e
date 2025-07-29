from machine import Pin, PWM

# Following line didn't work in the book. I went to docs.micropython.org
# to figure out how to fix it.
led = PWM(Pin('LED', Pin.OUT),freq=60, duty_u16=8192)

while True:
    #brightness_str = input('brightness (0-65534): ')
    #brightness = int(brightness_str)
    brightness_str = input('brightness (0-100): ')
    brightness = int(int(brightness_str) * 65534 / 100)
    led.duty_u16(brightness)

