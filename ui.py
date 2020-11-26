import pygame
from bonus import Bonus

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 750
WALL_DIM = 30
WALL_COLOR = (0,0,255)

def init():
    screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    return screen

def draw(screen):
    screen.fill((0, 0, 0))


def render_grid(screen):
    i = 0
    walls = []
    
    hsh = SCREEN_HEIGHT / 2
    hsw = SCREEN_WIDTH / 2
    cspc = WALL_DIM*5

    #border
    while i < SCREEN_HEIGHT:
        j = 0
        while j < SCREEN_WIDTH:
            if i >= (hsh - cspc) and j >= (hsw - cspc) and i <= (hsh + cspc) and j <= (hsw + cspc):
                j += WALL_DIM
            if i == 0 or j == 0 or i == (SCREEN_HEIGHT - WALL_DIM) or j == (SCREEN_WIDTH - WALL_DIM):
                r =  pygame.Rect(i, j, WALL_DIM, WALL_DIM)
                walls.append(r)
                pygame.draw.rect(screen, WALL_COLOR,r)
            if i % (4 * WALL_DIM) == 0 and j % (4 * WALL_DIM) == 0:
                r =  pygame.Rect(i, j, WALL_DIM, WALL_DIM)
                walls.append(r)
                pygame.draw.rect(screen, WALL_COLOR,r)

            if i  % (3 * WALL_DIM) == 0 and (j + WALL_DIM) % (4 * WALL_DIM) > 1:
                r =  pygame.Rect(i, j, WALL_DIM, WALL_DIM)
                walls.append(r)
                pygame.draw.rect(screen, WALL_COLOR,r)
            
            j += WALL_DIM
        i += WALL_DIM 
    
    return walls

  
def render_grid_from_file(screen):
    walls = []
    bonus = []
    
    hsh = SCREEN_HEIGHT / 2
    hsw = SCREEN_WIDTH / 2
    cspc = WALL_DIM*5
    
    f = open("grid.txt", "r")
    
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '#':
                r =  pygame.Rect(j * WALL_DIM, i * WALL_DIM, WALL_DIM, WALL_DIM)
                walls.append(r)
                pygame.draw.rect(screen, WALL_COLOR,r)
    f.close()

    return walls 

