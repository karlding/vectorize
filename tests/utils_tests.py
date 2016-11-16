"""Unit tests for utils"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image
import os
import vectorize
from vectorize import utils
import unittest

class UtilsTestCase(unittest.TestCase):
    def test_average_image_colour_white(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        image = Image.open(os.path.join(os.path.sep, dir_path, "white.png"))
        average_colour = utils.average_image_colour(image)
        assert average_colour[0] == 255
        assert average_colour[1] == 255
        assert average_colour[2] == 255

    def test_average_image_colour_black(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        image = Image.open(os.path.join(os.path.sep, dir_path, "black.png"))
        average_colour = utils.average_image_colour(image)
        assert average_colour[0] == 0
        assert average_colour[1] == 0
        assert average_colour[2] == 0
