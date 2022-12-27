from setup import *


class Series:
    def __init__(self, waves):
        self.waves = waves
        self.buffer = []

    def evaluate(self, time):
        x, y = 0, 0
        for magnitude, direction, frequency in self.waves:
            temp = time * frequency * 2 * math.pi + direction
            x += magnitude * math.cos(temp)
            y += magnitude * math.sin(temp)
        return x, y

    def get_vectors(self, time):
        output = []
        x, y = 0, 0
        for magnitude, direction, frequency in self.waves:
            temp = time * frequency * 2 * math.pi + direction
            start = (x, y)
            x += magnitude * math.cos(temp)
            y += magnitude * math.sin(temp)
            output.append((start, (x, y)))
        return output

    def get_points(self, sample_size):
        self.buffer = []
        n = 1 / sample_size
        for i in range(sample_size):
            self.buffer.append(self.evaluate(i * n))
        return np.array(self.buffer)

    def write_points_to_file(self, path, filename):
        with open(os.path.join(path, filename), "w") as f:
            output = ""
            for x, y in self.buffer:
                output += f"{x} {y}\n"
            output = output[:-1]
            f.write(output)

    def write_polar_to_file(self, path, filename):
        with open(os.path.join(path, filename), "w") as f:
            output = ""
            for magnitude, direction, frequency in self.waves:
                output += f"{magnitude} {direction} {frequency}\n"
            output = output[:-1]
            f.write(output)
