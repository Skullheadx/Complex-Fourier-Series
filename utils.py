import math
import numpy as np


def to_polar(x, y):
    return math.hypot(x, y), math.atan2(y, x)


def to_components(magnitude, direction):
    return magnitude * math.cos(direction), magnitude * math.sin(direction)
