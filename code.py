import time
import board
import busio
from adafruit_seesaw.seesaw import Seesaw
import neopixel
print("Libraries loaded")

# Set up the NeoPixel strip using the SPI connection
pixel_pin = board.GP16  # Change this to the correct pin for your board
num_pixels = 8  # Change this to the number of pixels on your NeoPixel stick
neopixel_strip = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)
