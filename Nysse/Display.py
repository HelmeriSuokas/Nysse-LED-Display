from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

# MATRIX CONFIG — known working settings
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.scan_mode = 0
options.pwm_bits = 8
options.brightness = 70
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
text_color = graphics.Color(255, 0, 0)
text_y = 14

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