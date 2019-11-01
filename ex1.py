import board
import adafruit_ws2801

leds = adafruit_ws2801.WS2801(board.D2, board.D0, 25)
leds.fill((0x80, 0, 0))
