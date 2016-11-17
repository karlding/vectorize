"""Utility functions used across Vectorize"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import math


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


def image_rms_diff(src, dest):
    """Calculate the difference between two images using normalized RMS"""
    total = 0
    width, height = src.size
    for x in range(width):
        for y in range(height):
            s_r, s_g, s_b, s_a = src.getpixel((x, y))
            d_r, d_g, d_b, d_a = dest.getpixel((x, y))

            diff_r = s_r - d_r
            diff_g = s_g - d_g
            diff_b = s_b - d_b

            total = total + (diff_r ** 2) + (diff_g ** 2) + (diff_b ** 2)
    return math.sqrt(total / (width * height * 3)) / 255
