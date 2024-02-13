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

#Constant position
MSG_POS_XY = (380, 335)
MSG_BLOCK_XY = (350, 325)
INFO_BOX_XY = (995,30)

#Booleans
boolFirstRoll = True
boolDiceRolling = False
# Loop until the user clicks the close button.
boolGameDone = False

pygame.init()
 
title_font = pygame.font.Font(None, 80)
msg_font = pygame.font.SysFont("garamond", 28)


# Set the width and height of the screen [width, height]
size = (1025, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Trac Game')
bg_surf = pygame.image.load("art/card_table.jpg").convert_alpha()
bg_surf = pygame.transform.smoothscale(bg_surf, size)


#info button
info_box = pygame.image.load("art/info_box.png").convert_alpha()
info_box_rect = info_box.get_rect(center = INFO_BOX_XY)

#Game screen
roll_msg = msg_font.render("Press space to roll dices", False, BLACK)
roll_msg_rect = roll_msg.get_rect(topleft = MSG_POS_XY)
msg_block = pygame.image.load("art/msg_block.png").convert_alpha()
msg_block_rect = msg_block.get_rect(topleft = MSG_BLOCK_XY)

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
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rollTimer = pygame.USEREVENT + 1
 
# -------- Main Program Loop -----------
while not boolGameDone:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boolGameDone = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not boolDiceRolling:
                #player press SPACE to roll dices
                if boolFirstRoll:
                    boolFirstRoll = False
                    
                pygame.time.set_timer(rollTimer, 1000)
                boolDiceRolling = True
                for dice in dice_group:
                    dice.setRolling(True)
                    dice.roll()
                    #checks value and face number
                    #print(f"Dice {dice.getDiceNumber()} : value {dice.getDiceFace()}")

        
        if event.type == rollTimer:
            #stop rolling dices
            boolDiceRolling = False
            for dice in dice_group:
                dice.setRolling(False)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not boolDiceRolling:
                if info_box_rect.collidepoint(pygame.mouse.get_pos()):
                    #put code in method that reset all game information
                    boolFirstRoll = True
                
            for tile in tile_group:
                if tile.checkCollision(pygame.mouse.get_pos()):
                    tile.isClicked()
        
    #table background
    screen.blit(bg_surf, (0,0))
 
        
    dice_group.update()
    tile_group.update()
    dice_group.draw(screen)
    tile_group.draw(screen)
    screen.blit(msg_block, msg_block_rect)
    screen.blit(info_box,info_box_rect)
    if boolFirstRoll:
        screen.blit(roll_msg, roll_msg_rect)

 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()