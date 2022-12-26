import random
from equation import Equation

class Series:

    def __init__(self, dna=None):
        if dna is None:
            self.dna = []
            for _ in range(15):
                self.dna.append((random.uniform(1, 100), random.uniform(0, 6), random.randint(0, 50)))
        else:
            self.dna = dna
        self.equation = Equation(contents=self.dna)

    def get_buffer(self, sample_size):
        return self.equation.get_buffer(sample_size)
