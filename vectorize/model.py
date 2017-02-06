from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image, ImageDraw

from vectorize.utils import average_image_colour


class Model(object):
    def __init__(self, target_image, scale_factor, workers):
        self.current = []
        self.shapes = []
        self.target = target_image.convert('RGBA')
        self.scale_factor = scale_factor
        self.background_colour = average_image_colour(self.target)

        width, height = target_image.size
        self.width = int(width / self.scale_factor)
        self.height = int(height / self.scale_factor)

        self.workers = []
        for i in range(workers):
            self.workers.append(Worker(target_image))

    def rasterize(self):
        result = Image.new(mode='RGBA',
                           size=(self.width, self.height),
                           color=self.background_colour)

        ctxt = ImageDraw.Draw(result)
        for shape in self.shapes:
            shape.rasterize(ctxt)

        del ctxt
        return result

    def add_shape(self, shape):
        """Add a polygon shape in front"""
        self.shapes.append(shape)

    def step(self):
        return

    def mutate(self):
        return
