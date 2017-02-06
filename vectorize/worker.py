from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image, ImageDraw

from datetime import datetime

class Worker(object):

    def __init__(self, image):
        self.width, self.height = image.size
        self.target = image
        self.steps = 0
        self.seed = datetime.now()
