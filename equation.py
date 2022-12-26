import math
import numpy as np
from utils import to_polar
import os


class Equation:
    def __init__(self, contents):
        self.contents = contents
        self.buffer = []

    def evaluate(self, time):
        x = 0
        y = 0
        for magnitude, direction, frequency in self.contents:
            temp = time * frequency * 2 * math.pi + direction
            x += magnitude * math.cos(temp)
            y += magnitude * math.sin(temp)
        return x, y

    def get_buffer(self, sample_size):
        self.buffer = []
        n = 1 / sample_size
        for i in range(sample_size):
            self.buffer.append(self.evaluate(i * n))
        return np.array(self.buffer)

    def write_buffer_to_file(self, path, filename):
        with open(os.path.join(path, filename), "w") as f:
            output = ""
            for x, y in self.buffer:
                output += f"{x} {y}\n"
            output = output[:-1]
            f.write(output)

    def write_polar_to_file(self, path, filename):
        with open(os.path.join(path, filename), "w") as f:
            output = ""
            for i in self.buffer:
                output += str(i) + "\n"
            output = output[:-1]
            f.write(output)
