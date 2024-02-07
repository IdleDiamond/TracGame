#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Created on Thu Feb  1 12:53:48 2024

 @author: joaking

 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
from lib.dice import Dice
from lib.tile import Tile
     

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
XY_MSG_BLOCK = (230, 335)

GAME_ACTIVE = False

pygame.init()
 
title_font = pygame.font.Font(None, 80)
msg_font = pygame.font.SysFont("garamond", 28)


# Set the width and height of the screen [width, height]
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Trac Game')
bg_surf = pygame.image.load("art/card_table.jpg").convert_alpha()
bg_surf = pygame.transform.smoothscale(bg_surf, size)

#initial screen
game_name = title_font.render("Trac Game", False, BLACK)
game_name_rect = game_name.get_rect(midbottom = (400,200))
game_msg = title_font.render("Press space to start", True, BLACK)
game_msg_rect = game_msg.get_rect(midbottom = (400, 330))

#Game screen
roll_msg = msg_font.render("Press space to roll dices", False, BLACK)
roll_msg_rect = roll_msg.get_rect(topleft = XY_MSG_BLOCK)
msg_block = pygame.image.load("art/msg_block.png").convert_alpha()
msg_block_rect = msg_block.get_rect(topleft = (200, 325))

#Groups dice
dice_group = pygame.sprite.Group()
dice_group.add(Dice(1))
dice_group.add(Dice(2))
#9 Tiles, create tile group sprite
tile_group = pygame.sprite.Group()

i = 9
while i > 0:
    tile_group.add(Tile(i))
    i -= 1

 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rollTimer = pygame.USEREVENT + 1
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #player press SPACE to roll dices
            if GAME_ACTIVE:
                pygame.time.set_timer(rollTimer, 1000)
                for dice in dice_group:
                    dice.setRolling(True)
                    dice.roll()     
                    #print(f"Dice {dice.getDiceNumber()} : value {dice.getDiceFace()}")
                    
            else:
                #player started game
                GAME_ACTIVE = True
        
        if event.type == rollTimer:
            #stop rolling dices
            for dice in dice_group:
                dice.setRolling(False)
        
    #table background
    screen.blit(bg_surf, (0,0))
 
    #different game screens
    if GAME_ACTIVE:
        
        dice_group.update()
        dice_group.draw(screen)
        tile_group.draw(screen)
        screen.blit(msg_block, msg_block_rect)
        screen.blit(roll_msg, roll_msg_rect)
        
    else:
        screen.blit(game_name, game_name_rect)
        screen.blit(game_msg, game_msg_rect)
 
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()