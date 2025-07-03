import os
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

<<<<<<< HEAD
# 🛠 Set slowdown BEFORE matrix init (to prevent flickering/garbage)
os.environ["LED_SLOWDOWN_GPIO"] = "4"

# ✅ Matrix configuration (matches working runtext.py)
=======
# MATRIX CONFIG — known working settings
>>>>>>> b4515556fafee27445455ae4df8c1b57f87bbc0d
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.scan_mode = 0
options.pwm_bits = 8
options.brightness = 70
<<<<<<< HEAD
options.hardware_mapping = 'adafruit-hat'

# ✅ Initialize matrix
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# ✅ Load font
font = graphics.Font()
font.LoadFont("/usr/share/fonts/rgbmatrix/7x13.bdf")

# ✅ Define text color
=======
options.hardware_mapping = 'adafruit-hat'  # This replaces gpio_mapping

# INIT MATRIX
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# FONT SETUP
font = graphics.Font()
try:
    font.LoadFont("/usr/share/fonts/rgbmatrix/7x13.bdf")
except Exception as e:
    print("Font load failed:", e)
    exit(1)
>>>>>>> b4515556fafee27445455ae4df8c1b57f87bbc0d
text_color = graphics.Color(255, 0, 0)

<<<<<<< HEAD
# ✅ Example fixed message
lines = ["TEST OK", "DISPLAY RUNS"]

# ✅ Main loop
while True:
    canvas.Clear()
    for i, line in enumerate(lines):
        graphics.DrawText(canvas, font, 2, 16 + i * 12, text_color, line)
    canvas = matrix.SwapOnVSync(canvas)
    time.sleep(1)
=======
# LOAD TEXT LINES FROM FILE
def read_tram_text():
    try:
        with open("ratikka_info.txt", "r") as f:
            return f.read().strip().split("\n")
    except Exception:
        return ["Virhe", "Ei tietoa"]

# MAIN DRAW LOOP
while True:
    lines = read_tram_text()
    canvas.Clear()
    for i, line in enumerate(lines):
        print("Drawing:", line)
        graphics.DrawText(canvas, font, 2, text_y + i * 14, text_color, line)
        graphics.DrawText(canvas, font, 2, text_y + i * 14, text_color, line)
    canvas = matrix.SwapOnVSync(canvas)
    time.sleep(5)
>>>>>>> b4515556fafee27445455ae4df8c1b57f87bbc0d
