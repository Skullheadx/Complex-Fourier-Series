from equation import Equation
from setup import *
from vector import VectorManager, Vector

screen = pygame.display.set_mode((720, 720))

m, d = to_polar(WIDTH / 2, HEIGHT / 2)
offset = Vector(m, d)

clock = pygame.time.Clock()
delta = 0
t = 0
is_running = True
scene = VectorManager("test.txt")
eqn = Equation(filename='test.txt')
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    if not scene.is_finished(delta / 1000):
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
        t += delta
        pygame.draw.circle(screen, (0, 0, 255), pygame.Vector2(eqn.evaluate(t / 1000)) + center, 10, width=4)

    pygame.display.flip()
    delta = clock.tick() / 2
