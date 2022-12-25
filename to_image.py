import pygame

def draw():
    WIDTH, HEIGHT = 720,720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
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

        screen.fill((255,255,255))
        pygame.draw.lines(screen, (0,0,0), True, buffer, 3)

        pygame.display.flip()
        clock.tick(60)
