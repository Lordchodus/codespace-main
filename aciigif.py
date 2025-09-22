import Pillow 
from PIL import Image, ImageSequence
import time
import os

# ASCII gradient from dark to light
ASCII_CHARS = "@%#*+=-:. "

def pixel_to_ascii(pixel_value):
    # Map pixel (0-255) → index in ASCII_CHARS
    index = pixel_value * (len(ASCII_CHARS) - 1) // 255
    return ASCII_CHARS[index]

def frame_to_ascii(frame, new_width=80):
    # Convert to grayscale
    gray = frame.convert("L")
    
    # Resize with aspect ratio correction
    width, height = gray.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 fixes ASCII aspect
    gray = gray.resize((new_width, new_height))
    
    # Build ASCII string
    ascii_str = ""
    for y in range(new_height):
        for x in range(new_width):
            ascii_str += pixel_to_ascii(gray.getpixel((x, y)))
        ascii_str += "\n"
    return ascii_str

def gif_to_ascii(path):
    gif = Image.open(path)
    for frame in ImageSequence.Iterator(gif):
        ascii_frame = frame_to_ascii(frame)
        os.system("cls" if os.name == "nt" else "clear")  # clear screen
        print(ascii_frame)
        time.sleep(0.1)  # delay between frames

# Run
gif_to_ascii("example.gif")
