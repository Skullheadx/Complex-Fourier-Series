from math import cos, sin,hypot, asin


class Vector:

    def __init__(self, x, y, frequency=0):
        self.x = x
        self.y = y
        self.length = hypot(self.x,self.y)#sqrt(pow(self.x, 2) + pow(self.y, 2))
        self.angle = asin(self.y/self.length)
        self.frequency = frequency

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def rotate(self, rad):
        self.angle += rad
        self.x, self.y = self.length * cos(self.angle), self.length * sin(self.angle)

    def pair(self):
        return (self.x,self.y)

class VectorManager:
    def __init__(self, filename):
        with open(filename, "r") as f:
            contents = f.read().split('\n')
            contents = contents[1:]
        contents = [tuple(map(int, i.split(" "))) for i in contents]
        self.vectors = [Vector(i, j, k) for i, j, k in contents]

        self.buffer = []

    def update(self, delta):
        end = Vector(0, 0)
        for vector in self.vectors:
            vector.rotate(delta * vector.frequency)
            end += vector
        if end not in self.buffer:
            self.buffer.append(end)
        # print(end.pair())

