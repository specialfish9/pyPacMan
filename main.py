import pygame
import random

import ui as ui
from player import Player
from ghost import Ghost
from bonus import Bonus

def render_ghosts(ghosts, screen):
    for ghost in ghosts:
        ghost.render(screen)

def move_ghost(ghosts, walls):
    for ghost in ghosts:
        for i in range(2):
            ghost.move()
        ghost.checkWalls(walls)

def check_collision(player, ghosts):
    exist = False
    for ghost in ghosts:
        exist = exist or ghost.isCollidedWithSprite(player)
    return exist

def create_ghosts(number):
    ghosts = []
    random.seed()
    for i in range(number):
        x = random.randint(0, ui.SCREEN_WIDTH)
        y = random.randint(0, ui.SCREEN_HEIGHT)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        ghosts.append(Ghost(ui.SCREEN_HEIGHT / 2, ui.SCREEN_WIDTH /2, (r, g, b)))
    return ghosts

def check_player_position(walls, player):
        if player.x < 0:
            player.x = ui.SCREEN_WIDTH
            return
        elif player.x > ui.SCREEN_WIDTH:
            player.x = 0
            return
        elif player.y <= 0:
            player.y = 0
            return
        elif player.y >= ui.SCREEN_HEIGHT:
            player.y = ui.SCREEN_HEIGHT
            return
        collided = player.checkWalls(walls)
        if collided:
            player.set

def draw_bonus(bonus, screen):
    for b in bonus:
        b.render(screen)

def check_bonus(bonus, player, p):
    for b in bonus:
        if b.isCollidedWithSprite(player):
          p += b.points  
    print("POINTS: " + str(p))

def main():
    pygame.init()
    screen = ui.init()
    running = True
    
    g_points = 0

    player = Player(ui.SCREEN_HEIGHT / 2, ui.SCREEN_WIDTH / 2)
    #ghosts = [
     #   Ghost(250,250, (255,0,0)),
      #  Ghost(250,250, (0,0,255)),
       # Ghost(250,250, (255,0,255)),
        #Ghost(250,250, (0,255,255))
    #]
    ghosts = create_ghosts(4)

    while running:
        ui.draw(screen)
        walls, bonus = ui.render_grid_from_file(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeftSafe(walls)
        elif keys[pygame.K_RIGHT]:
            player.moveRightSafe(walls)
        elif keys[pygame.K_UP]:
            player.moveUpSafe(walls)
        elif keys[pygame.K_DOWN]:
            player.moveDownSafe(walls)

        draw_bonus(bonus, screen)
        player.render(screen)
        move_ghost(ghosts, walls)
        render_ghosts(ghosts, screen)
        #check_player_position(player=player, walls=walls)

        #if check_collision(player, ghosts):
        #    print("collision!!!")
        check_bonus(bonus, player, g_points)

        pygame.display.flip()

    pygame.quit()    

if __name__ == "__main__":
    main()
