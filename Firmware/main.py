import board
import busio
import neopixel
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros


keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# 3 keys wired to these pins
PINS = [board.D3, board.D4, board.D2]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.DELETE,
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),
    ]
]

# LEDs (2 SK6812 chained, data on A3)
LED_PIN = board.A3
NUM_LEDS = 2

leds = neopixel.NeoPixel(
    LED_PIN,
    NUM_LEDS,
    brightness=0.25,
    auto_write=True
)

leds.fill((0, 50, 150))

# OLED display
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.text("Simon's Pad", 0, 0, 1)
oled.text("Ready", 0, 12, 1)
oled.show()


if __name__ == '__main__':
    keyboard.go()
