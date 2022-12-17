import pygame

# Info from https://www.youtube.com/watch?v=r6sGWTCMz2k
dimensions = pygame.Vector2(640,640)
center = pygame.Vector2(dimensions.x/2,dimensions.y/2)
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Complex Fourier Series")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)


class Arrow:
    def __init__(self, size, angle, n):
        self.arrow = pygame.Vector2(center)
        self.arrow.scale_to_length(size)
        self.arrow.rotate_ip(angle)
        self.n = n

    def update(self, delta, prev):
        self.start = prev.copy()
        self.arrow = self.arrow.rotate(delta*self.n)

    def draw(self,surf):
        pygame.draw.line(surf,RED,center + self.start, center + self.start + self.arrow)

class ArrowManager:
    update_time = 0
    buffer_size = 5000
    def __init__(self, filename):
        with open(filename,"r") as f:
            contents = f.read().split('\n')
        contents = [tuple(map(int,i.split(" "))) for i in contents]
        self.arrows = [Arrow(i,j, k) for i,j,k in contents]

        self.buffer = []
        self.time = 0
    def update(self, delta):
        prev=pygame.Vector2(0,0)
        for arrow in self.arrows:
            arrow.update(delta, prev)
            prev += arrow.arrow
        if self.time >= self.update_time:
            self.time -= self.update_time
            self.buffer.append(prev + center)
            if len(self.buffer) > self.buffer_size:
                del self.buffer[0]
        self.time += delta
    def draw(self, surf):
        for arrow in self.arrows:
            arrow.draw(surf)
        if len(self.buffer) > 1:
            pygame.draw.lines(surf,BLACK,False, self.buffer,3)
fps = 60
clock = pygame.time.Clock()
delta = 0
is_running = True
scene = ArrowManager("tests/test1.txt")
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    scene.update(delta/1000)

    screen.fill(WHITE)
    scene.draw(screen)

    pygame.display.flip()
    delta = clock.tick(fps)
