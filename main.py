from setup import *
from vector import VectorManager, Vector


screen = pygame.display.set_mode((720, 720))

offset = Vector(WIDTH/2,HEIGHT/2)

clock = pygame.time.Clock()
delta = 0
is_running = True
scene = VectorManager("test.txt")
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    scene.update(delta/1000)

    screen.fill(WHITE)
    prev = offset
    for i in scene.vectors:
        pygame.draw.line(screen,RED,prev.pair(),(prev+i).pair(),3)
        prev += i
    if len(scene.buffer) > 1:
        points = []
        for i in scene.buffer:
            points.append((offset + i).pair())
        # print(points)
        pygame.draw.lines(screen,BLACK,False,points,3)

    pygame.display.flip()
    delta = clock.tick(fps)