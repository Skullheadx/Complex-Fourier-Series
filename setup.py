import pygame


pygame.init()
# Info from https://www.youtube.com/watch?v=r6sGWTCMz2k
dimensions = pygame.Vector2(640,640)
center = pygame.Vector2(dimensions.x/2,dimensions.y/2)

pygame.display.set_caption("Complex Fourier Series")
fps = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
