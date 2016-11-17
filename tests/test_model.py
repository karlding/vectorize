"""Unit tests for model"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image
import os

from vectorize.model import Model
from vectorize.shape.rectangle import Rectangle

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def test_initialization():
    image = Image.open(os.path.join(os.path.sep, DIR_PATH, "white.png"))
    m = Model(image, 1)

    assert m.width == 200
    assert m.height == 200


def test_scaled_down_initialization():
    image = Image.open(os.path.join(os.path.sep, DIR_PATH, "black.png"))
    m = Model(image, 2)

    assert m.width == 100
    assert m.height == 100


def test_scaled_up_initialization():
    image = Image.open(os.path.join(os.path.sep, DIR_PATH, "black.png"))
    m = Model(image, 0.5)

    assert m.width == 400
    assert m.height == 400


def test_rasterize_basic():
    image = Image.open(os.path.join(os.path.sep, DIR_PATH, "black.png"))
    m = Model(image, 1)
    result = m.rasterize()

    image = image.convert('RGBA')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            assert image.getpixel((x, y)) == result.getpixel((x, y))


def test_rasterize_checkerboard():
    image = Image.open(os.path.join(os.path.sep, DIR_PATH, "black.png"))
    m = Model(image, 1)
    colour_white = (255, 255, 255, 255)

    expect = Image.open(os.path.join(os.path.sep, DIR_PATH, "checkers.png"))

    # row 1
    m.add_shape(Rectangle(((0, 0), (50, 50)), colour_white))
    m.add_shape(Rectangle(((100, 0), (150, 50)), colour_white))

    # row 2
    m.add_shape(Rectangle(((50, 50), (100, 100)), colour_white))
    m.add_shape(Rectangle(((150, 50), (200, 100)), colour_white))

    # row 3
    m.add_shape(Rectangle(((0, 100), (50, 150)), colour_white))
    m.add_shape(Rectangle(((100, 100), (150, 150)), colour_white))

    # row 4
    m.add_shape(Rectangle(((50, 150), (100, 200)), colour_white))
    m.add_shape(Rectangle(((150, 150), (200, 200)), colour_white))

    result = m.rasterize()

    width, height = image.size
    for x in range(width):
        for y in range(height):
            assert result.getpixel((x, y)) == expect.getpixel((x, y))
