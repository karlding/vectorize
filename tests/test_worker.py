"""Unit tests for worker"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image
import os

from vectorize.worker import Worker
from vectorize.shape.rectangle import Rectangle

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def test_initialization():
    image = Image.open(os.path.join(os.path.sep, DIR_PATH, "black.png"))
    worker = Worker(image)

    width, height = image.size

    assert worker.width == width
    assert worker.height == height
    assert worker.steps == 0
