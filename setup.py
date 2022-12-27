import math
import numpy as np
import os
import cv2

FILENAME = "circle.png"
PATH = "images/"
FILEPATH = os.path.join(PATH, FILENAME)

SAMPLE_SIZE = 5000

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def to_polar(x, y):
    return math.hypot(x, y), math.atan2(y, x)


def to_components(magnitude, direction):
    return magnitude * math.cos(direction), magnitude * math.sin(direction)
