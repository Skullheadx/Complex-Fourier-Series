from setup import *


def draw():
    screen = pygame.display.set_mode((720, 720))

    clock = pygame.time.Clock()
    delta = 0
    is_running = True

    with open("output.txt", "r") as f:
        contents = f.read().split("\n")
    buffer = [tuple(map(float, i.split(" "))) for i in contents]
    for i in range(len(buffer)):
        buffer[i] = (buffer[i][0] + WIDTH / 2, buffer[i][1] + HEIGHT / 2)
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill(WHITE)
        pygame.draw.lines(screen, BLACK, True, buffer, 3)

        pygame.display.flip()
        delta = clock.tick(60)
