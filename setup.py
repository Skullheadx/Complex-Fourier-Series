import pygame


pygame.init()

# Info from https://www.youtube.com/watch?v=r6sGWTCMz2k
WIDTH, HEIGHT = 640,640
dimensions = pygame.Vector2(WIDTH,HEIGHT)
center = pygame.Vector2(WIDTH/2,HEIGHT/2)

pygame.display.set_caption("Complex Fourier Series")
fps = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
