from series import Series
from match import match, image_to_list
from to_image import draw


class Population:
    population_size = 30
    mutation_rate = 0.0005

    def __init__(self, image_path):
        self.series = [Series() for _ in range(self.population_size)]
        self.top_fitness =0
        self.target = image_to_list(image_path)
        self.sample_size = len(self.target)

    def get_next_generation(self, target):
        fitnesses = []
        best_fitness = 0
        for series in self.series:
            score = match(self.target,series.get_buffer(self.sample_size))
            best_fitness = max(score, best_fitness)
        self.top_fitness = max(self.top_fitness, best_fitness)
        print(f"{best_fitness=} {self.top_fitness=}")
        parentsA = choices(self.rockets, fitnesses, k = self.population_size)
        parentsB = choices(self.rockets, fitnesses, k = self.population_size)
