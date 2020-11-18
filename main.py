import pygame
import random

import ui as ui
from player import Player
from ghost import Ghost


def render_ghosts(ghosts, screen):
    for ghost in ghosts:
        ghost.render(screen)

def move_ghost(ghosts, walls):
    for ghost in ghosts:
        ghost.move()
        ghost.checkWalls(walls)

def check_collision(player, ghosts):
    exist = False
    for ghost in ghosts:
        exist = exist or ghost.isCollidedWithSprite(player)
    return exist


def main():
    pygame.init()
    screen = ui.init()
    running = True

    player = Player(0, 250)
    ghosts = [
        Ghost(250,250, (255,0,0)),
        Ghost(250,250, (0,0,255)),
        Ghost(250,250, (255,0,255)),
        Ghost(250,250, (0,255,255))
    ]
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft()
        elif keys[pygame.K_RIGHT]:
            player.moveRight()
        elif keys[pygame.K_UP]:
            player.moveUp()
        elif keys[pygame.K_DOWN]:
            player.moveDown()

        if player.x < 0:
            player.x = ui.SCREEN_WIDTH
        
        if player.x > ui.SCREEN_WIDTH:
            player.x = 0

        if player.y <= 0:
            player.y = 0
        
        if player.y >= ui.SCREEN_HEIGHT:
            player.y = ui.SCREEN_HEIGHT
        
        ui.draw(screen)
        walls = ui.render_grid(screen)
        player.render(screen)
        move_ghost(ghosts, walls)
        render_ghosts(ghosts, screen)

        if check_collision(player, ghosts):
            print("collision!!!")

        pygame.display.flip()

    pygame.quit()    

if __name__ == "__main__":
    main()
