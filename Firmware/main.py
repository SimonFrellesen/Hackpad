import board
import time
import busio
import neopixel
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# ---------- KMK SETUP ----------
keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.DELETE,
        KC.MACRO("Hello world!"),
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),
    ]
]

# ---------- LED SETUP (SK6812) ----------
LED_PIN = board.A3   # GPIO29 from your schematic
NUM_LEDS = 2

leds = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=0.25, auto_write=True)
leds.fill((0, 50, 150))  # blue color

# ---------- OLED SETUP ----------
i2c = busio.I2C(board.SCL, board.SDA)

while not i2c.try_lock():
    pass
i2c.unlock()

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.text("Simon Pad", 0, 0, 1)
oled.text("OLED OK", 0, 12, 1)
oled.show()

# ---------- START ----------
if __name__ == '__main__':
    keyboard.go()
