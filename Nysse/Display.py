import os
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# 🛠 Set slowdown BEFORE matrix init (to prevent flickering/garbage)
os.environ["LED_SLOWDOWN_GPIO"] = "4"

# ✅ Matrix configuration (matches working runtext.py)
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.scan_mode = 0
options.pwm_bits = 8
options.brightness = 70
options.hardware_mapping = 'adafruit-hat'

# ✅ Initialize matrix
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# ✅ Load font
font = graphics.Font()
font.LoadFont("/usr/share/fonts/rgbmatrix/7x13.bdf")

# ✅ Define text color
text_color = graphics.Color(255, 0, 0)

# ✅ Example fixed message
lines = ["TEST OK", "DISPLAY RUNS"]

# ✅ Main loop
while True:
    canvas.Clear()
    for i, line in enumerate(lines):
        graphics.DrawText(canvas, font, 2, 16 + i * 12, text_color, line)
    canvas = matrix.SwapOnVSync(canvas)
    time.sleep(1)
