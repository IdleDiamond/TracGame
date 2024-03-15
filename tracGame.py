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

#pylint: disable=invalid-name
#pylint: disable=no-member

import pygame
from lib.dice import Dice
from lib.tile import Tile


def checkGameEnd():
    """Checks if with dice result the game is still possible"""
    
    
    POSSIBILITY_DICT = {12: [{9,3}, {9,2,1}, {8,4}, {8,3,1}, {7,5}, {7,3,2}, {7,4,1}, {6,5,1}, {6,4,2}, {6,3,2,1}, {5,4,3}],
                       11: [{9,2}, {8,3}, {8,2,1}, {7,4}, {7,3,1}, {6,5}, {6,4,1}, {6,3,2}, {5,4,2}, {5,3,2,1}],
                       10: [{9,1}, {8,2}, {7,3}, {7,2,1}, {6,4}, {6,3,1}, {5,4,1}, {5,3,2}, {4,3,2,1}],
                       9: [{9}, {8,1}, {7,2}, {6,3}, {6,2,1}, {5,4}, {5,3,1}, {4,3,2}],
                       8: [{8}, {7,1}, {6,2}, {5,3}, {5,2,1}, {4,3,1}],
                       7: [{7}, {6,1}, {5,2}, {4,3}, {4,2,1}],
                       6: [{6}, {5,1}, {4,2}, {3,2,1}],
                       5: [{5}, {4,1}, {3,2}],
                       4: [{4}, {3,1}],
                       3: [{3}, {2,1}],
                       2: [{2}],
                       1: [{1}]}
    
    isGameImpossible = True
    posList = POSSIBILITY_DICT[diceResult]
    
    
    for count, setPos in enumerate(posList):
        
        if setPos.issubset(set(tilesInPlay)):
            isGameImpossible = False
    
    return isGameImpossible


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
isFirstRoll = True
isDiceRolling = False
isGameDone = False
isPlayerTurn = False

#variables
diceResult = 0
tilesInPlay = [9,8,7,6,5,4,3,2,1]

pygame.init()

#title_font = pygame.font.Font(None, 80)
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
dice_result = msg_font.render(f"{diceResult}", False, BLACK)
dice_result_rect = dice_result.get_rect(topleft = MSG_POS_XY)

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
while not isGameDone:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameDone = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not isPlayerTurn:
                if not isDiceRolling:
                    #player press SPACE to roll dices
                    if isFirstRoll:
                        isFirstRoll = False

                    pygame.time.set_timer(rollTimer, 1000, 1)
                    isDiceRolling = True
                    isPlayerTurn = True
                    for dice in dice_group:
                        dice.setRolling(True)
                        dice.roll()

        if event.type == rollTimer:
            #stop rolling dices
            isDiceRolling = False
            for dice in dice_group:
                dice.setRolling(False)
                diceResult += dice.getDiceFace()
            dice_result = msg_font.render(f"{diceResult}", False, BLACK)
            
            if checkGameEnd():
                print("Game ends, call ending function")
            
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not isDiceRolling:
                if info_box_rect.collidepoint(pygame.mouse.get_pos()):
                    #put code in method that reset all game information
                    #isFirstRoll = True
                    pass

            if isPlayerTurn:
                for count, tile in enumerate(tile_group, 1):
                    if tile.checkCollision(pygame.mouse.get_pos()):
                        tile.isClicked()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if isPlayerTurn:
                tileSelection = []
                sumSelected = 0
                for count, tile in enumerate(tile_group):
                    if not tile.getIsUsed():
                        if (tile.getIsSelected()):
                            # print(f"Value {tile.getValue()}")
                            tileSelection.append(tile)
                            sumSelected += tile.getValue()
                
                if sumSelected == diceResult:
                    # print("same amount")
                    for count, tile in enumerate(tileSelection):
                        tile.setIsUsed(True)
                        tilesInPlay.remove(tile.getValue())
                        
                    isPlayerTurn = False
                    diceResult = 0
                    print(tilesInPlay)
                    
                    


    #table background
    screen.blit(bg_surf, (0,0))


    dice_group.update()
    tile_group.update()
    dice_group.draw(screen)
    tile_group.draw(screen)
    screen.blit(msg_block, msg_block_rect)
    screen.blit(info_box,info_box_rect)
    if isFirstRoll:
        screen.blit(roll_msg, roll_msg_rect)
    if diceResult != 0:
        dice_result_rect = dice_result.get_rect(topleft = MSG_POS_XY)
        screen.blit(dice_result, dice_result_rect)


    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
