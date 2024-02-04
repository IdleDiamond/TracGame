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
        
        self.frames = (dice_1, dice_2, dice_3, dice_4, dice_5, dice_6)
        self.dice_face = 0
        self.image = self.frames[self.dice_face]
        
        if diceNumber == 1:
            self.rect = self.image.get_rect(midbottom = (80, 430))
        else:
            self.rect = self.image.get_rect(midbottom = (140, 430))
        
    def show(self):
        self.image = self.frames[self.dice_face]
        
    def roll(self):
        #use random
        #call animation??
        self.dice_face = 3
        
    def player_event(self):
        #if space press then roll 
        pass
    
    def dice_animation(self):
        #when roll event
        pass
        
    def update(self):
        self.player_event()
        self.show()
        

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

GAME_ACTIVE = True

 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Trac Game')
bg_surf = pygame.image.load("art/card_table.jpg").convert_alpha()
bg_surf = pygame.transform.smoothscale(bg_surf, size)


#Groups
dice_group = pygame.sprite.Group()
dice_group.add(Dice(1))
dice_group.add(Dice(2))

 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.blit(bg_surf, (0,0))
 
    if GAME_ACTIVE:
        dice_group.update()
        dice_group.draw(screen)
        
    else:
        pass
 
    
 
    
    
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()