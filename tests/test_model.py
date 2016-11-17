"""Unit tests for model"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image
import os

from vectorize.model import Model


def test_initialization():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image = Image.open(os.path.join(os.path.sep, dir_path, "white.png"))
    m = Model(image, 1)

    assert m.width == 200
    assert m.height == 200


def test_scaled_down_initialization():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image = Image.open(os.path.join(os.path.sep, dir_path, "black.png"))
    m = Model(image, 2)

    assert m.width == 100
    assert m.height == 100


def test_scaled_up_initialization():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image = Image.open(os.path.join(os.path.sep, dir_path, "black.png"))
    m = Model(image, 0.5)

    assert m.width == 400
    assert m.height == 400
