import random
from equation import Equation

class Series:

    def __init__(self, dna=None):
        if dna is None:
            self.dna = []
            for _ in range(random.randint(1, 100)):
                self.dna.append((random.uniform(1, 50), random.uniform(0, 360), random.randint(0, 50)))
        else:
            self.dna = dna
        self.equation = Equation(contents=dna)

    def get_buffer(self, sample_size):
        return self.equation.get_buffer(sample_size)
