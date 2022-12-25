import math
import numpy as np
from utils import to_polar


class Equation:
    def __init__(self, contents=None, filename=None):
        self.period = 1

        if contents is None or filename is not None:
            with open("test.txt", "r") as f:
                self.contents = f.read().split('\n')
                mode = self.contents[0]
                self.contents = self.contents[1:]
            self.contents = [tuple(map(float, i.split(" "))) for i in self.contents]
            if mode == "components":
                for i, val in enumerate(self.contents):
                    x, y = to_polar(val[0], val[1])
                    self.contents[i] = (x, y, val[2])
                    self.period *= val[2]
        else:
            self.contents = contents

    def evaluate(self, time):
        x = 0
        y = 0
        for magnitude, direction, frequency in self.contents:
            temp = time * frequency * 2 * math.pi + direction
            x += magnitude * math.cos(temp)
            y += magnitude * math.sin(temp)
        return x, y

    def get_buffer(self, sample_size):
        buffer = []
        n = self.period / sample_size
        for i in range(sample_size):
            buffer.append(self.evaluate(i * n))
        return np.array(buffer)
