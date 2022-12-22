from math import cos, sin, hypot, atan2
from utils import to_components


class Vector:

    def __init__(self, magnitude, direction, frequency=1):
        self.frequency = frequency
        self.length = magnitude
        self.angle = direction

    def __add__(self, other):
        x = self.x_component() + other.x_component()
        y = self.y_component() + other.y_component()
        return Vector(hypot(x, y), atan2(y, x), self.frequency)

    def rotate(self, rad):
        self.angle += rad * self.frequency

    def x_component(self):
        return self.length * cos(self.angle)

    def y_component(self):
        return self.length * sin(self.angle)

    def components(self):
        return self.x_component(), self.y_component()


class VectorManager:
    def __init__(self, filename):
        with open(filename, "r") as f:
            contents = f.read().split('\n')
            mode = contents[0]
            contents = contents[1:]
        contents = [tuple(map(int, i.split(" "))) for i in contents]
        if mode == "polar":
            for i, val in enumerate(contents):
                x,y =to_components(val[0],val[1])
                contents[i] = (x,y,val[2])
        self.vectors = [Vector(i, j, k) for i, j, k in contents]

        self.buffer = []

    def update(self, delta):
        end = Vector(0, 0)
        for vector in self.vectors:
            vector.rotate(delta)
            end += vector
        self.buffer.append(end)
