import os
os.environ["LED_SLOWDOWN_GPIO"] = "4"

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.scan_mode = 0
options.pwm_bits = 8
options.brightness = 70
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

font = graphics.Font()
font.LoadFont("/usr/share/fonts/rgbmatrix/7x13.bdf")
color = graphics.Color(255, 0, 0)

while True:
    canvas.Clear()
    graphics.DrawText(canvas, font, 2, 20, color, "TEST OK")
    canvas = matrix.SwapOnVSync(canvas)
    time.sleep(1)
