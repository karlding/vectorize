from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from vectorize.utils import average_image_colour

class Model(object):
    def __init__(self, target_image, scale_factor):
        self.shapes = []
        self.current = []
        self.target = target_image.convert('RGBA')
        self.scale_factor = scale_factor
        self.background_colour = average_image_colour(self.target)

        width, height = target_image.size
        self.width = int(width / self.scale_factor)
        self.height = int(height / self.scale_factor)

    def add_shape(self, shape):
        """Add a shape in front"""
        shapes.append(shape)

    def step(self):
        return

    def mutate(self):
        return
