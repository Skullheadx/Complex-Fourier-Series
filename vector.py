from math import cos, sin, sqrt, pow, radians


class Vector:

    def __init__(self, x, y, frequency=None):
        self.x = x
        self.y = y
        self.length = sqrt(pow(self.x, 2) + pow(self.y, 2))
        self.frequency = frequency

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def rotate(self, rad):
        return Vector(self.length * cos(rad), self.length * sin(rad))


class VectorManager:
    def __init__(self, filename):
        with open(filename, "r") as f:
            contents = f.read().split('\n')
        contents = [tuple(map(int, i.split(" "))) for i in contents]
        self.vectors = [Vector(i, j, k) for i, j, k in contents]

        self.buffer = []

    def update(self, delta):
        end = Vector(0, 0)
        for vector in self.vectors:
            end += vector.rotate(delta * vector.frequency)
        self.buffer.append(end)
