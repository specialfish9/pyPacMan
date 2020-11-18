import pygame
from sprite import Sprite

class Player(Sprite):
    STEP = 0.5

    def __init__(self, x, y):
        self.dimension = 20
        super().__init__(x, y)

    def render(self, screen):
        pygame.draw.circle(screen, (255,255,0), (self.x, self.y), self.dimension)