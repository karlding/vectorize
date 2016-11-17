from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from vectorize.shape.shape import Shape


class Rectangle(Shape):
    def __init__(self, bounding_box, colour):
        super(Rectangle, self).__init__()
        self.bounding_box = bounding_box
        self.colour = colour

    def rasterize(self, ctxt):
        ctxt.rectangle(self.bounding_box, fill=self.colour)
