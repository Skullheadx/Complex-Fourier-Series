from population import Population
IMAGE_PATH = "images/circle.png"

p = Population(IMAGE_PATH)

for i in range(1001):
    p.get_next_generation()