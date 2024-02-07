#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:31:31 2024

@author: joaking
"""

import pygame

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
        x = 10-value
        self.rect = self.image.get_rect(center = ((x*82),120))
    
    def getIsSelected(self):
        return self.isSelected
    
    def getValue(self):
        return self.value
    
    #continue this method
    def playerEvent(self):
        pass
    
    def tileAnimation(self):
        if self.isSelected:
            self.image = self.tile_frame[1]
        elif self.isUsed:
            self.image = self.tile_frame[2]
        else:
            self.image = self.tile_frame[0]
            
    def update(self):
        self.tileAnimation()