from machine import Pin, SoftI2C
from lib_lcd1602_2004_with_i2c import LCD
sda_pin = 27
scl_pin = 26
char_arrow_fwd = [
    0b10000,
    0b11000,
    0b11100,
    0b11110,
    0b11110,
    0b11100,
    0b11000,
    0b10000,
]
char_arrow_rev = [
    0b00001,
    0b00011,
    0b00111,
    0b01111,
    0b01111,
    0b00111,
    0b00011,
    0b00001,
]

lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))
lcd.create_charactor(1, char_arrow_fwd)
lcd.create_charactor(2, char_arrow_rev)
lcd.puts("100 Days of Code")
message2 = " " + chr(1) + chr(1) + " Day 100 " + chr(2) + chr(2)
lcd.puts(message2, 1)