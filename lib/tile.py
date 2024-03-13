#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:31:31 2024

@author: joaking

Card pixelart from Andrew Tidey andrewtidey.blogspot.co.uk
"""

#pylint: disable=invalid-name

import pygame

TILE_X_POS = 21
TILE_Y_POS = 130

class Tile(pygame.sprite.Sprite):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.isSelected = False
        self.isUsed = False
        tile = pygame.image.load(f'art/{value}.png').convert_alpha()
        tile_selected = pygame.image.load(f'art/{value}sel.png').convert_alpha()
        tile_used = pygame.image.load('art/used.png').convert_alpha()
        self.tile_frame = (tile, tile_selected, tile_used)
        self.image = self.tile_frame[0]
        cardIndex = 10-value
        self.rect = self.image.get_rect(midleft = (TILE_X_POS+(110*(cardIndex-1)),TILE_Y_POS))


    def getIsSelected(self):
        return self.isSelected

    #not used yet
    def setIsSelected(self, value):
        self.isSelected = value

    def isClicked(self):
        if not self.isUsed:
            if self.isSelected:
                self.isSelected = False
            else:
                self.isSelected = True


    def getIsUsed(self):
        return self.isUsed
    
    def setIsUsed(self, value):
        self.isUsed = value

    def getValue(self):
        return self.value

    def tileAnimation(self):
        if self.isUsed:
            self.image = self.tile_frame[2]
        elif self.isSelected:
            self.image = self.tile_frame[1]
        else:
            self.image = self.tile_frame[0]

    def checkCollision(self, pos):
        return self.rect.collidepoint(pos)

    def update(self):
        self.tileAnimation()
        