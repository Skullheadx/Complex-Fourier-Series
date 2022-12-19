from setup import *
from vector import VectorManager, Vector

screen = pygame.display.set_mode((720, 720))

m, d = to_polar(WIDTH / 2, HEIGHT / 2)
offset = Vector(m, d)

clock = pygame.time.Clock()
delta = 0
is_running = True
scene = VectorManager("tests/test1.txt")
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    scene.update(delta / 1000)

    screen.fill(WHITE)

    if len(scene.buffer) > 1:
        points = []
        for i in scene.buffer:
            points.append((offset + i).components())
        pygame.draw.lines(screen, BLACK, False, points, 3)
    prev = offset
    for i in scene.vectors:
        pygame.draw.line(screen, RED, prev.components(), (prev + i).components(), 3)
        prev += i
    pygame.display.flip()
    delta = clock.tick()
