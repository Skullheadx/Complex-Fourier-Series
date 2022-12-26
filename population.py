from series import Series
from match import match, image_to_list
import random


class Population:
    population_size = 30
    mutation_rate = 0.0005

    def __init__(self, image_path):
        self.series = [Series() for _ in range(self.population_size)]
        self.top_fitness = 0
        self.target = image_to_list(image_path)
        self.sample_size = len(self.target)
        self.generation = 0

    def get_next_generation(self):
        fitnesses = []
        best_fitness = 0
        for series in self.series:
            score = match(self.target, series.get_buffer(self.sample_size))
            fitnesses.append(score)
            best_fitness = max(score, best_fitness)
        self.top_fitness = max(self.top_fitness, best_fitness)

        while sum(fitnesses) <= 0:
            self.series = [Series() for _ in range(self.population_size)]
            print("-----reset----")
            self.get_next_generation()

        print(f"{best_fitness=} {self.top_fitness=}")

        if self.generation % 10 == 0:
            self.series[0].equation.write_polar_to_file("generations/", f"gen{self.generation} polar.txt")
            self.series[0].equation.write_buffer_to_file("generations/", f"gen{self.generation} buffer.txt")
        self.generation += 1
        parentsA = random.choices(self.series, fitnesses, k=self.population_size)
        parentsB = random.choices(self.series, fitnesses, k=self.population_size)
        children = []

        for i in range(self.population_size):
            children.append(self.get_child(parentsA[i], parentsB[i]))
        self.series = children

    def get_child(self, parentA, parentB):
        new_dna = []
        for i in range(15):
            if random.random() < 0.5:
                new_dna.append(parentA.dna[i])
            else:
                new_dna.append(parentB.dna[i])

            if random.random() < self.mutation_rate:
                new_dna[i] = (random.uniform(1, 50), random.uniform(0, 360), random.randint(0, 50))

        return Series(new_dna)
