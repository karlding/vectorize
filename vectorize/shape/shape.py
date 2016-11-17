from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class Shape(object):
    def rasterize(self):
        """Rasterize the shape, by drawing itself on the Image context"""
        raise NotImplementedError('Subclasses must override rasterize()')
