import pygame

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
WALL_DIM = 20
WALL_COLOR = (0,0,255)

def init():
    screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    return screen

def draw(screen):
    screen.fill((0, 0, 0))


def render_grid(screen):
    i = 0
    walls = []
    while i < SCREEN_HEIGHT:
        j = 0
        while j < SCREEN_WIDTH:
            if i == 0 or j == 0 or i == (SCREEN_HEIGHT - WALL_DIM) or j == (SCREEN_WIDTH - WALL_DIM):
                r =  pygame.Rect(i, j, WALL_DIM, WALL_DIM)
                walls.append(r)
                pygame.draw.rect(screen, WALL_COLOR,r)
            j += WALL_DIM
        i += WALL_DIM 
    return walls

  