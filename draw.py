from setup import *
import pygame


def draw(series):
    WIDTH, HEIGHT = 640, 640
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    OFFSET = (WIDTH / 2, HEIGHT / 2)
    clock = pygame.time.Clock()
    is_running = True
    points = []
    delta = 0
    time = 0
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        time += delta
        for start, end in series.get_vectors(time):
            pygame.draw.line(screen, RED, start, end, 1)

        new_point = series.evaluate(time)
        if new_point not in points:
            points.append(new_point)

        screen.fill(WHITE)
        if len(points) > 1:
            pygame.draw.lines(screen, BLUE, True, points, 1)

        pygame.display.flip()
        delta = clock.tick(60) / 1000 # seconds
