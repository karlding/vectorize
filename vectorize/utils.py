"""Utility functions used across Vectorize"""
from PIL import Image

def average_image_colour(image):
    image = image.convert('RGBA')
    red = 0
    green = 0
    blue = 0
    count = 0
    for r, g, b, a in image.getdata():
        red = red + r
        green = green + g
        blue = blue + b
        count = count + 1
    return int(red / count), int(green / count), int(blue / count)

