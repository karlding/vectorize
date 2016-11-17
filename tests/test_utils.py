"""Unit tests for utils"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image
import os

from vectorize import utils
from vectorize.utils import average_image_colour

import py.test

def test_average_image_colour_white():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image = Image.open(os.path.join(os.path.sep, dir_path, "white.png"))
    image = image.convert('RGBA')
    average_colour = utils.average_image_colour(image)
    assert average_colour[0] == 255
    assert average_colour[1] == 255
    assert average_colour[2] == 255

def test_average_image_colour_black():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image = Image.open(os.path.join(os.path.sep, dir_path, "black.png"))
    image = image.convert('RGBA')
    average_colour = utils.average_image_colour(image)
    assert average_colour[0] == 0
    assert average_colour[1] == 0
    assert average_colour[2] == 0

def test_image_rms_diff_same_image():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image = Image.open(os.path.join(os.path.sep, dir_path, "black.png"))
    image = image.convert('RGBA')

    assert utils.image_rms_diff(image, image) == 0

def test_image_rms_diff():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    black = Image.open(os.path.join(os.path.sep, dir_path, "black.png"))
    black = black.convert('RGBA')
    white = Image.open(os.path.join(os.path.sep, dir_path, "white.png"))
    white = white.convert('RGBA')

    assert utils.image_rms_diff(black, white) == 1
