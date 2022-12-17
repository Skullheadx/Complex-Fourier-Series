from setup import *
from vector import VectorManager


screen = pygame.display.set_mode((720, 720))

clock = pygame.time.Clock()
delta = 0
is_running = True
scene = VectorManager("tests/test1.txt")
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    scene.update(delta/1000)

    screen.fill(WHITE)
    scene.draw(screen)

    pygame.display.flip()
    delta = clock.tick(fps)
