from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

# matrix config
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# fontti
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")

text_color = graphics.Color(255, 0, 0)
text_y = 14

# ratikka infojen luku
def read_tram_text():
    try:
        with open("ratikka_info.txt", "r") as f:
            return f.read().strip().split("\n")
    except Exception:
        return ["Virhe", "Ei tietoa"]

while True:
    lines = read_tram_text()

    canvas.Clear()
    for i, line in enumerate(lines):
        graphics.DrawText(canvas, font, 1, text_y + i * 14, text_color, line)

    canvas = matrix.SwapOnVSync(canvas)
    time.sleep(10)
