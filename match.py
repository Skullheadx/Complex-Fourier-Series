from setup import *

def image_to_list(path):
    image = pygame.image.load(path)
    return pygame.surfarray.pixels2d(image)


print(image_to_list("images/circle.png"))