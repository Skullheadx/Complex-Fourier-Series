import pygame
import math

pygame.init()

# Info from https://www.youtube.com/watch?v=r6sGWTCMz2k
WIDTH, HEIGHT = 640, 640
dimensions = pygame.Vector2(WIDTH, HEIGHT)
center = pygame.Vector2(WIDTH / 2, HEIGHT / 2)

pygame.display.set_caption("Complex Fourier Series")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def to_polar(x, y):
    return math.hypot(x, y), math.atan2(y, x)


def to_components(magnitude, direction):
    return magnitude * math.cos(direction), magnitude * math.sin(direction)
