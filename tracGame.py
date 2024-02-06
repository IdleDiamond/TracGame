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
from random import randint


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

class Dice(pygame.sprite.Sprite):
    def __init__(self, diceNumber):
        super().__init__()
        dice_1 = pygame.image.load('art/dice_1.png').convert_alpha()
        dice_2 = pygame.image.load('art/dice_2.png').convert_alpha()
        dice_3 = pygame.image.load('art/dice_3.png').convert_alpha()
        dice_4 = pygame.image.load('art/dice_4.png').convert_alpha()
        dice_5 = pygame.image.load('art/dice_5.png').convert_alpha()
        dice_6 = pygame.image.load('art/dice_6.png').convert_alpha()
        
        self.diceFace = 0
        self.diceNumber = diceNumber
        self.frames = (dice_1, dice_2, dice_3, dice_4, dice_5, dice_6)
        self.image = self.frames[self.diceFace]

        
        if self.diceNumber == 1:
            self.rect = self.image.get_rect(midbottom = (80, 410))
        else:
            self.rect = self.image.get_rect(midbottom = (140, 410))
        
    def show(self):
        self.image = self.frames[self.diceFace]
        
    def roll(self):
        #Result from rolling the diec
        self.diceFace = randint(0,5)
        
    def player_event(self):
        pass
    
    def getDiceFace(self):
        return self.diceFace + 1
    
    def dice_animation(self):
        if ROLLING_DICE:
            rolling_face = randint(0,5)
            self.image = self.frames[rolling_face]
        else:
            self.show()
        
    def update(self):
        self.player_event()
        self.dice_animation()
        

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

GAME_ACTIVE = False
ROLLING_DICE = False


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
roll_msg_rect = roll_msg.get_rect(topleft = (230, 335))
msg_block = pygame.image.load("art/msg_block.png").convert_alpha()
msg_block_rect = msg_block.get_rect(topleft = (200, 325))

#Groups
dice_group = pygame.sprite.Group()
dice_group.add(Dice(1))
dice_group.add(Dice(2))

 
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
                ROLLING_DICE = True
                for dice in dice_group:
                    dice.roll()     
            else:
                #player started game
                GAME_ACTIVE = True
        
        if event.type == rollTimer:
            #stop rolling dices
            ROLLING_DICE = False
        
    #table background
    screen.blit(bg_surf, (0,0))
 
    #different game screens
    if GAME_ACTIVE:
        
        dice_group.update()
        dice_group.draw(screen)
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