import pygame

def draw():
    WIDTH, HEIGHT = 640, 640
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    is_running = True
    img = pygame.image.load("images/circle.png")
    with open("generations/gen100 buffer.txt", "r") as f:
        contents = f.read().split("\n")
    buffer = [tuple(map(float, i.split(" "))) for i in contents]
    for i in range(len(buffer)):
        buffer[i] = (buffer[i][0] + WIDTH / 2, buffer[i][1] + HEIGHT / 2)
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((255,255,255))
        screen.blit(img,img.get_rect(center=(WIDTH/2,HEIGHT/2)))
        pygame.draw.lines(screen, (0,0,255), True, buffer, 1)

        pygame.display.flip()
        clock.tick(60)

draw()