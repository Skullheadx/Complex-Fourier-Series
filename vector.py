from setup import *

class Vector:
    def __init__(self, size, angle, n):
        self.vector = pygame.Vector2(center)
        self.vector.scale_to_length(size)
        self.vector.rotate_ip(angle)
        self.n = n

    def update(self, delta, prev):
        self.start = prev.copy()
        self.vector = self.vector.rotate(delta * self.n)

    def draw(self,surf):
        pygame.draw.line(surf, RED, center + self.start, center + self.start + self.vector)

class VectorManager:
    update_time = 0
    buffer_size = 5000
    def __init__(self, filename):
        with open(filename,"r") as f:
            contents = f.read().split('\n')
        contents = [tuple(map(int,i.split(" "))) for i in contents]
        self.vectors = [Vector(i, j, k) for i, j, k in contents]

        self.buffer = []
        self.time = 0
    def update(self, delta):
        prev=pygame.Vector2(0,0)
        for vector in self.vectors:
            vector.update(delta, prev)
            prev += vector.vector
        if self.time >= self.update_time:
            self.time -= self.update_time
            self.buffer.append(prev + center)
            if len(self.buffer) > self.buffer_size:
                del self.buffer[0]
        self.time += delta
    def draw(self, surf):
        for vector in self.vectors:
            vector.draw(surf)
        if len(self.buffer) > 1:
            pygame.draw.lines(surf,BLACK,False, self.buffer,3)
